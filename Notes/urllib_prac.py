# Web Exercises

"""
1. Create a python script to extract h1 tag from example.com or any site.
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

def my_scraper():
    # set url to scrape
    url = 'http://www.bloomberg.com/quote/SPX:IND'
    # query the website and return the html to the variable
    page = urlopen(url).read()
    #print(page)
    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')
    #print(soup)
    # Take out the <div> of name and get its value
    name_box = soup.find('h1')
    print(name_box)
    name = name_box.text.strip() # strip() is used to remove starting and trailing
    print(name)
    """ OLD CODE REMOVED: for specific stock price
    (https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe/)
    name_box = soup.find('h1', attrs={'class': 'name'})
    # get the index price
    #price_box = soup.find('div', attrs={'class':'price'})
    #price = price_box.text
    #print(price)
    """

#my_scraper()

def shorter_scape():
    # https://www.w3resource.com/python-exercises/web-scraping/web-scraping-exercise-6.php 
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    html = urlopen('http://www.bloomberg.com/quote/SPX:IND')
    bsh = BeautifulSoup(html.read(), 'html.parser')
    print(bsh.h1)

#shorter_scape()

"""
2. Create a Python script to verify if a given webpage exists or not on the server.
"""
def my_error():
    import urllib.request as request
    import urllib.error as error
    
    try:
        request.urlopen('https://www.python.org/f')
        print('Success')
    except error.URLError as e:
        print('Error Occured: ', e.reason)

# my_error()
"""
3. Create a Python script to check whether a page contains a title or not.
"""

def my_title():
    from bs4 import BeautifulSoup
    from urllib.request import urlopen

    try:
        url = "http://www.py4inf.com/code/romeo-full.txt"  #http://www.google.com
        soup = BeautifulSoup(urlopen(url), 'html.parser')
        print(f'Title: {soup.title.string}')
    except:
        print('No title')

# my_title()

"""
4. Create a Python script to get the number of people visiting a U.S. government website right now. using this information-> Source: https://analytics.usa.gov/data/live/realtime.json
"""

def search_attr():
    import requests
    
    link = "https://analytics.usa.gov/data/live/realtime.json" 
    response = requests.get(link).json() 
    print(response['data'][0]['active_visitors'])


#search_attr()

"""
5. Create a Python Script to a list of all the h1, h2, h3 tags from the site page python.org.
"""
"""
headings = soup.find_all("h1, h2, h3, h4, h5, h6")
http://www.crummy.com/software/BeautifulSoup/bs4/doc/#a-regular-expression
soup.find_all(re.compile(r'h\d+')) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for a in ["h1","h2"]:
  soup.find_all(a)
"""
def list_all():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import re

    html = urlopen('http://www.python.org')
    soup = BeautifulSoup(html.read(), 'html.parser')
    #headings = soup.find_all(re.compile(r'h\d+')) 
    headings = []
    headers = soup.find_all(['h1', 'h2','h3'])
    for x in headers:
        headings.append(x.text.strip())
    print(headings)
    
list_all()

def shorter_find():
    # https://www.w3resource.com/python-exercises/web-scraping/web-scraping-exercise-7.php
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    html = urlopen('http://www.python.org')
    bs = BeautifulSoup(html, "html.parser")
    titles = bs.find_all(['h1', 'h2','h3'])
    print('List all the header tags :', *titles, sep='\n\n')

#shorter_find()
"""
6. Use urllib to retrieve http://www.py4inf.com/code/romeo-full.txt and display up to 3000 characters, and counting the overall characters in the document. Don't worry about the headers for this exercise, simply show the first 3000 characters of the document contents.
"""

def show_count():
    import requests
    link = "http://www.py4inf.com/code/romeo-full.txt"
    r = requests.get(link)
    print(r.text[0:3000])

#show_count()
