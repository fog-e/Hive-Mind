import requests
from bs4 import BeautifulSoup

def fetch_faq():
    url = "https://cobeekeeping.org/faq"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    print("\n=== Scanning page structure for FAQ entries ===\n")

    # Print out tag names and their cleaned text for visual inspection
    for tag in soup.find_all(True):
        tag_name = tag.name
        tag_text = tag.get_text(strip=True)
        if tag_text and len(tag_text) < 120:
            print(f"<{tag_name}>: {tag_text}")

if __name__ == "__main__":
    fetch_faq()
