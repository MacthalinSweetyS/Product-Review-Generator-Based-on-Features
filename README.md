# Product-Review-Generator-Based-on-Features
---

```markdown
# Product Review Generator

A Python-based AI-powered product review generator that scrapes product details from provided URLs (e.g., Amazon, Desertcart) and generates a custom review. The review includes product features and a "value-for-money" comment based on the product’s price. If data extraction fails due to anti-scraping measures or layout differences, users can manually input the product information.

## Features

- **Automated Data Extraction**  
  Uses [CloudScraper](https://github.com/Velegol/cloudscraper) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) to scrape product names, features, and prices from shopping websites.
  
- **Review Generation**  
  Generates a custom review that includes comments on product features and, when available, a value-for-money statement based on the price.
  
- **Multiple Tone Options**  
  Supports multiple review tones: Neutral, Formal, Casual, Enthusiastic, and Technical.
  
- **Manual Input Option**  
  If extraction fails, the user can manually enter the product name, features, and price.

- **Flask Web Interface**  
  Provides an interactive web form to input product URLs or details and view generated reviews.

## Folder Structure

```
Product_Review_Generator/
├── app.py
├── review_generator.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── main.css
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/<your-username>/Product_Review_Generator.git
   cd Product_Review_Generator
   ```

2. **Install the required dependencies:**

   Ensure you have [Python 3](https://www.python.org/) installed, then run:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file includes:
   
   - Flask==2.2.5
   - requests
   - beautifulsoup4
   - cloudscraper

## Usage

1. **Start the Flask Server**

   In your terminal, navigate to the project folder and run:

   ```bash
   python app.py
   ```

2. **Open Your Browser**

   Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

3. **Use the Interface**

   - **Product URL:**  
     Enter a URL (e.g., `https://desertcart.in/products/506978174`). The app will try to scrape product details automatically.
     
   - **Manual Input:**  
     If extraction fails, manually enter the **Product Name**, **Features** (comma-separated), and **Price**.
     
   - **Tone & Language:**  
     Choose the desired tone for the review and set the language (default is English).
     
   - **Generate Review:**  
     Click the "**Generate Review**" button to see the generated review, including a value-for-money comment if a price is provided.

## How It Works

- **Scraping:**  
  The application uses CloudScraper to bypass basic anti-scraping blocks and fetch the page content. It then parses the HTML with BeautifulSoup to extract the product title, features, and price.
  
- **Review Generation:**  
  The extracted details are passed to a function that constructs a review. It extracts a numeric value from the price (if present) and adds a tailored comment regarding affordability or value for money.
  
- **Fallback Mechanism:**  
  If scraping fails to return valid details, the application prompts the user to enter the details manually.

## Limitations and Future Improvements

- **Anti-Scraping Measures:**  
  Many shopping sites use protection techniques that can block scraping, even with CloudScraper.
  
- **Dynamic Content:**  
  Some sites load data via JavaScript. A headless browser (Selenium or Playwright) might be required for such pages.
  
- **Variable Layouts:**  
  HTML structures vary between sites and over time. Future improvements may include more site-specific selectors or the use of official APIs.
  
- **Enhanced AI Review Generation:**  
  Future iterations may integrate advanced natural language models (e.g., GPT-based models) for more sophisticated review generation and customization.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [CloudScraper](https://github.com/Velegol/cloudscraper)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

Happy coding!
```

---
