import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import defaultdict

def read_label_data():
    data = defaultdict(list)
    with open('./data/training_data/labeled_data2.csv') as f:
            reader = csv.reader(f)
            for index, row in enumerate(reader):
                if index == 0:
                    continue
                data[row[0]].append((row[1], row[2]))

    return data

def input_data(input_data):
    driver = init_webdriver(url)

    for k, v in data.items():
        soup = BeautifulSoup(k, 'html5lib')
        input = soup.find('input')
        attrs = input.attrs
        print(k, attrs)
        if 'id' in attrs.keys():
            selector = f'//input[@id="{attrs["id"]}"]'
        elif 'name' in attrs.keys():
            selector = f'//input[@name="{attrs["name"]}"]'
        else:
            print(f'{k}が指定できない')
            continue

        try:
            element = driver.find_element_by_xpath(selector)
            element.send_keys(v)
        except Exception as e:
            print(e)

    driver.close()

def init_webdriver(url):
    try:
        driver = webdriver.Chrome(executable_path='./script/chromedriver')
        driver.set_page_load_timeout(30)
        driver.get(url)
        return driver
    except Exception as e:
        print(e)

if __name__ == '__main__':
    read_label_data()
