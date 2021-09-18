from selenium import webdriver

def open(url):
    browser = webdriver.Chrome(executable_path='./chromedriver')
    browser.get(url)