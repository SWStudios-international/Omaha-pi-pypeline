from modules.vin_decoder import decode_vin
from modules.craigslist_scraper import craigslist_search
from modules.bing_news import bing_news_search
from modules.db_logger import save_results
# Import more modules as you build them:
# from modules.douglas_assessor_scraper import assessor_search

def main():
    vin = input("VIN (optional): ").strip()
    keywords = input("Keywords / Plate / Address (optional): ").strip()

    # Run VIN lookup
    if vin:
        vin_info = decode_vin(vin)
        print("\n[VIN Lookup]")
        print(vin_info)
        save_results('db/vin_results.csv', [vin_info], list(vin_info.keys()))

    # Run Craigslist search
    if keywords:
        craigslist_results = craigslist_search(keywords)
        print("\n[Craigslist Results]")
        for result in craigslist_results:
            print(result)
        if craigslist_results:
            save_results('db/craigslist_results.csv', craigslist_results, craigslist_results[0].keys())

        # Run Bing News search
        news_results = bing_news_search(keywords)
        print("\n[Bing News Results]")
        for result in news_results:
            print(result)
        if news_results:
            save_results('db/news_results.csv', news_results, news_results[0].keys())

    # Example: run assessor search (if you have it)
    # if keywords:
    #     assessor_results = assessor_search(keywords)
    #     print("\n[Assessor Search Results]")
    #     for result in assessor_results:
    #         print(result)
    #     if assessor_results:
    #         save_results('db/assessor_results.csv', assessor_results, assessor_results[0].keys())

if __name__ == "__main__":
    main()
