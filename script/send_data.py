import csv
from .user_data import get_input_data
from bs4 import BeautifulSoup
from selenium import webdriver
from collections import defaultdict

def read_label_data():
    data = defaultdict(list)
    with open('./data/result/labeled_data.csv') as f:
            reader = csv.reader(f)
            for index, row in enumerate(reader):
                if index == 0:
                    continue
                """
                row[0]: company name
                row[1]: company url
                row[2]: company contact page url
                row[3]: html tag
                row[4]: label
                """
                data[row[0], row[2]].append((row[3], row[4]))

    return data

def send():

    result = {}

    try:
        driver = webdriver.Chrome(executable_path='./tool/chromedriver')
        driver.set_page_load_timeout(30)
    except Exception as e:
        print(e)


    data = read_label_data()
    for k, v in data.items():
        driver.get(k[1])

        for html_tag, label in v:
            if label == 'subject':
                pass
            else:
                print(html_tag, label)
                soup = BeautifulSoup(html_tag, 'html5lib')
                input = soup.find('input')
                try:
                    attrs = input.attrs
                except AttributeError:
                    print(AttributeError)

                if 'id' in attrs.keys():
                    selector = f'//input[@id="{attrs["id"]}"]'
                elif 'name' in attrs.keys():
                    selector = f'//input[@name="{attrs["name"]}"]'
                else:
                    print(f'{html_tag}が指定できない')
                    result[k[0]] = f'{html_tag}が指定できない'
                    continue

                try:
                    element = driver.find_element_by_xpath(selector)
                    element.send_keys(get_input_data(label))
                except Exception as e:
                    print(e)
                    result[k[0]] = e
            
        print(result)
        input()
        break

    driver.close()
