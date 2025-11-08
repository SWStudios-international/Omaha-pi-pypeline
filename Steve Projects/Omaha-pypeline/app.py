from flask import Flask, request, render_template
from modules.vin_decoder import decode_vin
from modules.craigslist_scraper import craigslist_search
from modules.bing_news import bing_news_search
import os

def flatten_table_data(data):
    """Replace newlines, carriage returns, and tabs in all string values in a list of dicts."""
    if isinstance(data, list):
        for row in data:
            if isinstance(row, dict):
                for k, v in row.items():
                    if isinstance(v, str):
                        row[k] = v.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    return data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = {}
    if request.method == "POST":
        vin = request.form.get("vin", "").strip()
        keywords = request.form.get("keywords", "").strip()
        if vin:
            vin_data = [decode_vin(vin)]
            results["VIN Lookup"] = flatten_table_data(vin_data)
        if keywords:
            cl_results = craigslist_search(keywords)
            news_results = bing_news_search(keywords)
            results["Craigslist Results"] = flatten_table_data(cl_results)
            results["News Results"] = flatten_table_data(news_results)
        # Add other modules here as needed
    return render_template("index.html", results=results)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
