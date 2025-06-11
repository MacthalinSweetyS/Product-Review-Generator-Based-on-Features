import random
import re
import cloudscraper
from bs4 import BeautifulSoup

def get_page_content(url):
    """
    Use CloudScraper to fetch page content.
    """
    try:
        scraper = cloudscraper.create_scraper()
        response = scraper.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print("CloudScraper error:", e)
        return ""

def extract_product_details(product_url):
    """
    Extract product details (name, features, price) from the given URL.
    Supports Amazon and Desertcart as examples.
    """
    html = get_page_content(product_url)
    if not html:
        return "Unknown Product", [], ""
    
    soup = BeautifulSoup(html, 'html.parser')
    
    product_name = ""
    features = []
    price = ""
    
    if "amazon." in product_url.lower():
        title_elem = soup.find(id="productTitle")
        if title_elem:
            product_name = title_elem.get_text().strip()
        if not product_name or product_name.lower() in ["amazon", "amazon.in", "amazon.com"]:
            meta_title = soup.find("meta", {"property": "og:title"})
            if meta_title and meta_title.get("content"):
                product_name = meta_title["content"].strip()
        if not product_name or "amazon" in product_name.lower():
            return "Unknown Product", [], ""
        feature_div = soup.find("div", {"id": "feature-bullets"})
        if feature_div:
            features = [li.get_text(strip=True) for li in feature_div.find_all("span", {"class": "a-list-item"}) if li.get_text(strip=True)]
        price_elem = soup.find(id="priceblock_ourprice")
        if not price_elem:
            price_elem = soup.find(id="priceblock_dealprice")
        if price_elem:
            price = price_elem.get_text().strip()
        else:
            meta_price = soup.find("meta", {"property": "product:price:amount"})
            if meta_price and meta_price.get("content"):
                price = meta_price["content"].strip()
    
    elif "desertcart.in" in product_url.lower():
        title_elem = soup.find("h1", {"class": "product_title"}) or soup.find("h1", {"class": "product-title"})
        if title_elem:
            product_name = title_elem.get_text().strip()
        price_elem = soup.find("span", {"class": "money"})
        if price_elem:
            price = price_elem.get_text().strip()
        feature_ul = soup.find("ul", {"class": "product_features"})
        if feature_ul:
            features = [li.get_text(strip=True) for li in feature_ul.find_all("li")]
        if not product_name:
            return "Unknown Product", [], ""
    
    else:
        meta_title = soup.find("meta", {"property": "og:title"})
        if meta_title and meta_title.get("content"):
            product_name = meta_title["content"].strip()
        elif soup.title and soup.title.string:
            product_name = soup.title.string.strip()
        else:
            product_name = "Unknown Product"
        features = ["high-quality design", "excellent performance"]
        price_elem = soup.find("span", {"class": "product-price"})
        if price_elem:
            price = price_elem.get_text().strip()
    
    return product_name, features, price

def generate_review(product_name, features, tone="neutral", language="en", price=""):
    """
    Generate a product review that includes the product's features, and if a price is provided,
    adds a comment on whether the product is worth its cost.
    """
    if not product_name:
        product_name = "The product"
    
    feature_text = ", ".join(features) if features else "its outstanding qualities"
    base_review = f"{product_name} is known for its {feature_text}."
    
    # If price is provided, try to extract a numeric value and comment on value for money.
    price_comment = ""
    if price:
        nums = re.findall(r"[\d,\.]+", price)
        if nums:
            num_str = nums[0].replace(",", "")
            try:
                num_val = float(num_str)
                if num_val < 1000:
                    value_comment = "It's incredibly affordable."
                elif num_val < 5000:
                    value_comment = "It offers great value for money."
                else:
                    value_comment = "While it's on the pricier side, the quality justifies the cost."
            except Exception:
                value_comment = "it appears to offer good value."
        else:
            value_comment = "it appears to offer good value."
        price_comment = f" Priced at {price}, {value_comment}"
    
    if tone == "formal":
        review_text = f"In terms of quality and craftsmanship, {base_review} It demonstrates exceptional performance.{price_comment}"
    elif tone == "casual":
        review_text = f"Hey, check it out! {product_name} totally rocks with its {feature_text}.{price_comment}"
    elif tone == "enthusiastic":
        review_text = f"{product_name} absolutely blows you away with its {feature_text}! Everyone is raving about it.{price_comment}"
    elif tone == "technical":
        review_text = f"Technically speaking, {product_name} excels due to its {feature_text}. Its engineering is top-notch.{price_comment}"
    else:
        review_text = base_review + f" It is appreciated for its reliability and performance.{price_comment}"
    
    summary = review_text.split(".")[0] + "."
    rating = random.randint(3, 5)
    
    return review_text, rating, summary
