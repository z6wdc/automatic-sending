import requests
from bs4 import BeautifulSoup

def get_all_links(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.find_all('a')