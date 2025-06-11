##Product Review GeneratorBased on Features

```markdown
# Product Review Generator

Product Review Generator is a minimal Python web application built with Flask that automatically scrapes product details from a provided URL and generates a custom review. The review includes product features along with a value-for-money comment based on the product’s price. If the automatic extraction fails, you have the option to input product details manually.

## Features

- **Automated Extraction:**  
  The app uses CloudScraper to bypass basic anti-scraping protection and BeautifulSoup to parse HTML. It supports extracting product title, features (e.g., bullet points), and price from supported websites like Amazon and Desertcart.

- **Custom Review Generation:**  
  Based on the extracted or manually entered data, the app generates a review. If a price is provided, it analyzes the numeric value and adds a comment on whether the product is very affordable, offers great value, or is slightly expensive but justified by quality.

- **Multiple Tones:**  
  Users can choose among several review tones—Neutral, Formal, Casual, Enthusiastic, or Technical—to match the style of the review.

- **Fallback Input:**  
  When extraction fails due to website restrictions or layout differences, you can manually enter the product name, features, and price.

- **Simple Web Interface:**  
  The application provides a straightforward form where you can either enter a product URL or fill in details manually, view the generated review, and see a list of all created reviews.

## Requirements

- Python 3.x  
- Flask  
- requests  
- beautifulsoup4  
- cloudscraper  

All dependencies are listed in the `requirements.txt` file.

## Installation

1. **Clone the Repository:**

   Open a terminal and run:

   ```bash
   git clone https://github.com/<your-username>/Product_Review_Generator.git
   cd Product_Review_Generator
   ```

2. **Install Dependencies:**

   Ensure you have Python 3 installed, then install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run

1. **Start the Application:**

   In your terminal, navigate to the project directory and launch the Flask server by running:

   ```bash
   python app.py
   ```

2. **Access the Web Interface:**

   Open your browser and navigate to:

   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

3. **Using the Interface:**

   - **Product URL:**  
     Enter a product URL from supported websites (e.g., `https://amazon.in/d/<id>` or `https://desertcart.in/products/<id>`).  
     The app will attempt to extract product details (name, features, and price) automatically.
   
   - **Manual Input Option:**  
     If extraction fails (for example, if the website blocks the scraping or the layout has changed), you will see an error message prompting you to enter details manually. Simply fill in:
     - **Product Name:** The product's title.
     - **Features:** A comma-separated list of features (e.g., "long battery life, high-resolution camera").
     - **Price:** The product price (e.g., "₹10,999").
   
   - **Tone & Language:**  
     Choose the tone for your review (Neutral, Formal, Casual, Enthusiastic, or Technical) and specify the language (default is English).
     
   - **Generate Review:**  
     Click the "Generate Review" button. A custom review, along with a summary and a rating, will be displayed along with the value-for-money comment if a price is provided.

## Folder Structure

The repository has the following structure:

```
Product_Review_Generator/
├── app.py                  # Main Flask application file that handles routes and form submissions.
├── review_generator.py     # Module that contains functions for scraping product details and generating reviews.
├── requirements.txt        # The list of Python package dependencies.
├── templates/
│   └── index.html          # HTML template for the web interface.
└── static/
    └── main.css            # CSS file for styling the web interface.
```

## Additional Information

- **Extraction Limitations:**  
  Web scraping can be unreliable due to dynamic content, anti-scraping measures, and frequently changing layouts. This project uses CloudScraper as a simple solution, but for heavy-duty or production use, consider headless browsers (like Selenium or Playwright) or dedicated APIs.

- **Customization:**  
  You are welcome to adjust the review generation logic in `review_generator.py` to change tone thresholds, value comments, or incorporate more sophisticated natural language techniques.

- **Feedback:**  
  Any issues or feature suggestions are welcome—feel free to open an issue or submit a pull request.

Happy coding!
```
