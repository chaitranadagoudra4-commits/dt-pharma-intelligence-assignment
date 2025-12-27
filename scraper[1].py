
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    data = {}
    data["Website"] = url
    data["Timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    title = soup.find("title")
    data["Company Name"] = title.text if title else "Not Found"

    print(data)

if __name__ == "__main__":
    import sys
    scrape(sys.argv[1])
