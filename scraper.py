# import dependencies needed to download an HTML file and parse it.
import urllib.request
from bs4 import BeautifulSoup
import sys

# thegamesdb.net base URLs (Searching, platform listing, anything else needed)
base_search = "https://thegamesdb.net/search.php?platform_id%5B%5D=0&name="

def get_html_search(searchterm):
    search_page = urllib.request.urlopen(base_search + searchterm)
    html = BeautifulSoup(search_page, "html.parser")
    print(html)

if len(sys.argv) < 2:
    print("Usage: scraper.py <search term>")
    sys.exit()
get_html_search(sys.argv[1])