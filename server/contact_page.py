from selenium import webdriver

browser = webdriver.Chrome(executable_path='./chromedriver')

def open(url):
    browser.get(url)

def input_name(name):
    browser.find_element_by_class_name("").input(name)

def input_email(email):
    browser.find_element_by_class_name("").input(name)

def input_phone(phone):
    browser.find_element_by_class_name("").input(name)

def click_send(phone):
    browser.find_element_by_id("name").click(name)
