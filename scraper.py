# import dependencies needed to download an HTML file and parse it.
# urllib specifically is imported with Py2 and Py3 cross-compatibility in mind.
import pip
try:
    import urllib.request as urlrequest
except ImportError:
    import urllib as urlrequest
try:
    from bs4 import BeautifulSoup
    import sys
    import requests
    import os
except ImportError:
    with open("requirements.txt") as f:
        for line in f:
            # call pip's main function with each requirement
            pip.main(['install','-U', line])
    from bs4 import BeautifulSoup
    import sys
    import requests
    import os

# thegamesdb.net base URLs (Searching, platform listing, anything else needed)
base_search = "https://thegamesdb.net/search.php?platform_id%5B%5D=0&name="

# Takes a search word as input, the word is then paired with the base URL
# in order to collect HTML Text Data via BeautifulSoup
def get_html_search(searchterm):
    search_page = urlrequest.urlopen(base_search + searchterm)
    html = BeautifulSoup(search_page, "html.parser")
    print(html)

# Using the search term provided by the user, looks through each 'img' tag
# to find & add corresponding URL's which will be used for downloading boxart
def parse_html_search(term):
    html = get_html_search(term)
    parsing_array = html.find_all('img', src=re.compile(r'https://cdn.thegamesdb.net/images/thumb/boxart/'))
    print(parsing_array)
    #save_art(url,filename)

# This function's sole purpose is to download boxart images using the url provided to the filename provided
def save_art(url, filename):
    # TheGamesDB blocks urlopen, so we need to use an alternative method
    
    # Get the art via the URL
    r = requests.get(url) # create HTTP response object 
  
    # Open the image file and write the request data to it.
    with open(filename,'wb') as f: 
        f.write(r.content) 
        f.close()

def open_art(filename):
    os.startfile(filename)

if len(sys.argv) < 2:
    print("Usage: scraper.py <search term>")
    sys.exit()
get_html_search(sys.argv[1])
parse_html_search(sys.argv[1])
#save_art(sys.argv[2], "test.png")
#open_art("test.png")
