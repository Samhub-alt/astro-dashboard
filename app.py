from flask import Flask, render_template, jsonify
import requests
from datetime import datetime
import pytz

app = Flask(__name__)

def fetch_astrology_data():
    """
    This is the engine. It calculates the current time and pulls data.
    To make it fully live, you will replace the placeholder strings below 
    with the exact data points from your chosen free API (like VedAstro or FreeAstrologyAPI).
    """
    # Set time to Indian Standard Time (IST)
    ist = pytz.timezone('Asia/Kolkata')
    now = datetime.now(ist)
    
    # Here is where you will add your API call later. 
    # Example: response = requests.get("https://api.freeastrologyapi.com/v1/planets")
    
    return {
        "date_banner": now.strftime("%A • %d %B %Y").upper(),
        "nakshatra_today": "Mrigashira",  # API data goes here
        "nakshatra_details": "till 19:20 IST · then Ardra", # API data goes here
        "planets": {
            "Sun": "29.9° Tau",      # API data goes here
            "Moon": "0.3° Gem",      # API data goes here
            "Mercury": "24.3° Gem",  # API data goes here
            "Venus": "7.8° Can",     # API data goes here
            "Mars": "25.9° Ari",     # API data goes here
            "Jupiter": "2.6° Can",   # API data goes here
            "Saturn": "19.1° Pis",   # API data goes here
            "Rahu": "9.2° Aqu R",    # API data goes here
            "Ketu": "9.2° Leo R"     # API data goes here
        }
    }

@app.route('/')
def dashboard():
    # This serves the HTML face of your website
    return render_template('index.html')

@app.route('/api/live-data')
def live_data():
    # This sends the fresh data to your HTML page automatically
    data = fetch_astrology_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
