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
    import re
    from PIL import Image
except ImportError:
    with open("requirements.txt") as f:
        for line in f:
            # call pip's main function with each requirement
            pip.main(['install','-U', line])
    from bs4 import BeautifulSoup
    import sys
    import requests
    import os
    import re
    from PIL import Image

# thegamesdb.net base URLs (Searching, platform listing, anything else needed)
base_search = "https://thegamesdb.net/search.php?platform_id%5B%5D=0&name="

def get_html_search(searchterm):
    search_page = requests.get(base_search + searchterm)
    html = BeautifulSoup(search_page.content, "html.parser")
    return html
   #print(html)

def parse_html_search(term):
    html = get_html_search(term)
    parsing_array = html.find_all('img', src=re.compile(r'https://cdn.thegamesdb.net/images/thumb/boxart/'))
    art_url = parsing_array[0]['src']
    print(art_url)
    return art_url

def save_art(url, filename):
    #wget.download(url, filename)

    # TheGamesDB blocks urlopen, so we need to use an alternative method

    # Get the art via the URL
    r = requests.get(url) # create HTTP response object 

    # Open the image file and write the request data to it.
    with open(filename,'wb') as f: 
        f.write(r.content)
        f.close()

def open_art(filename):
    try:
        os.startfile(filename)
    except AttributeError:
        im = Image.open(filename)
        im.show()

if len(sys.argv) < 3:
    print("Usage: scraper.py <search term> <filename to save to>")
    sys.exit()

boxart_url = parse_html_search(sys.argv[1])
save_art(boxart_url, sys.argv[2])
open_art(sys.argv[2])
