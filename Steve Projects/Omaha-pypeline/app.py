from flask import Flask, request, render_template
from modules.vin_decoder import decode_vin
from modules.craigslist_scraper import craigslist_search
from modules.bing_news import bing_news_search
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = {}
    if request.method == "POST":
        vin = request.form.get("vin", "").strip()
        keywords = request.form.get("keywords", "").strip()
        if vin:
            results["VIN Lookup"] = [decode_vin(vin)]
        if keywords:
            results["Craigslist Results"] = craigslist_search(keywords)
            results["News Results"] = bing_news_search(keywords)
        # Add other modules here as needed
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
