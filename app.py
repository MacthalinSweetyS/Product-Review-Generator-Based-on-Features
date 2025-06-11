from flask import Flask, render_template, request, jsonify
from review_generator import generate_review, extract_product_details

app = Flask(__name__)

# In-memory storage for reviews (demo purposes)
reviews = []

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        product_url = request.form.get('productUrl', '').strip()
        tone = request.form.get('tone', 'neutral')
        language = request.form.get('language', 'en')
        
        if product_url:
            product_name, features_list, price = extract_product_details(product_url)
            if product_name == "Unknown Product" or not features_list:
                error = ("Could not extract valid product details from the provided URL. "
                         "Please enter the product name, features, and price manually.")
        else:
            product_name = request.form.get('productName', '').strip()
            features = request.form.get('features', '')
            features_list = [f.strip() for f in features.split(',') if f.strip()]
            price = request.form.get('price', '').strip()
        
        if not error:
            review_text, rating, summary = generate_review(product_name, features_list, tone, language, price)
            review_entry = {
                'productName': product_name,
                'features': features_list,
                'price': price,
                'generatedReview': review_text,
                'rating': rating,
                'summary': summary,
                'tone': tone,
                'language': language,
                'productUrl': product_url
            }
            reviews.append(review_entry)
            return render_template('index.html', review=review_entry, reviews=reviews, error=error)
    
    return render_template('index.html', reviews=reviews, error=error)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    product_url = data.get('productUrl', '').strip()
    tone = data.get('tone', 'neutral')
    language = data.get('language', 'en')
    
    if product_url:
        product_name, features, price = extract_product_details(product_url)
    else:
        product_name = data.get('productName', '').strip()
        features = data.get('features', [])
        price = data.get('price', '').strip()
    
    review_text, rating, summary = generate_review(product_name, features, tone, language, price)
    review_entry = {
        'productName': product_name,
        'features': features,
        'price': price,
        'generatedReview': review_text,
        'rating': rating,
        'summary': summary,
        'tone': tone,
        'language': language,
        'productUrl': product_url
    }
    reviews.append(review_entry)
    return jsonify(review_entry)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
