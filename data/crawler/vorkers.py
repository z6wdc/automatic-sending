import csv
import time
from selenium import webdriver

result = {}

with open('./data/crawler/company.csv') as f:
        reader = csv.reader(f)
        for index, row in enumerate(reader):
            """
            row[0]: company name
            """
            result[row[0]] = 'url not found'


VORKERS_URL = 'https://www.vorkers.com/'

driver = webdriver.Chrome(executable_path='./tool/chromedriver')
driver.set_page_load_timeout(30)

for k in result.keys():

    try:
        driver = webdriver.Chrome(executable_path='./tool/chromedriver')    
        driver.set_page_load_timeout(30)
    except Error as e:
        result[k] = 'selenium起動失敗'

    driver.get(VORKERS_URL)

    try:
        driver.find_element_by_class_name('keywordSearch_input').send_keys(k)
        driver.find_element_by_class_name('pcIcon-searchButton').click()
    except Exception as e:
        result[k] = '入力失敗'

    try:
        driver.find_element_by_link_text(k).click()
    except Exception as e:
        result[k] = '会社名見つからなかった'

    try:
        element = driver.find_element_by_xpath('//a[@data-_v-event-logger-key="company_url_link"]')
        result[k] = element.text
    except Exception as e:
        result[k] = 'URL情報見つからなかった'

    time.sleep(10)
    driver.quit()

with open('./data/crawler/company_url_list.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    for company, url in result.items():
        print(company, url)
        writer.writerow([company, url])
