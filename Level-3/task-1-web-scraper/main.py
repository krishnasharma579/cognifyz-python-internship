import requests
from bs4 import BeautifulSoup
import os
import csv

BASE_DIR = os.path.dirname(__file__)
csv_path = os.path.join(BASE_DIR, "quotes.csv")

#function to scrape quotes from the website
def web_scraper():
    try:
        #send a GET request to the website
        response = requests.get("https://quotes.toscrape.com/", timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        print("Something went wrong. Please check your internet connection.")
        return

    #parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    #find all quote containers
    quotes = soup.find_all("div", class_="quote")

    with open(csv_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author", "Tags"])

        #display each quote with its author and tags
        for index, quote in enumerate(quotes, start=1):
            quote_text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            tags = quote.find_all("a", class_="tag")

            tag_list = ", ".join(tag.text for tag in tags)

            #console output
            print("=" * 50)
            print(f"Quote #{index}")
            print(f"Quote : {quote_text}")
            print(f"Author: {author}")
            print("Tags  :")

            for tag in tags:
                print(f"- {tag.text}")

            print()

            #csv output
            writer.writerow([quote_text, author, tag_list])

    print(f"Quotes saved successfully to:\n{csv_path}")

if __name__ == "__main__":
    web_scraper()