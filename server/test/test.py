import pytest
import scraping
import contact_page

def test_get_all_links():
     links = scraping.get_all_links('https://www.data4cs.co.jp/')

     assert len(links) > 0

def test():
    contact_page.open('https://www.data4cs.co.jp/contact')