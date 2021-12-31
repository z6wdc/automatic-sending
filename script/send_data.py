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

    driver = webdriver.Chrome(executable_path='./tool/chromedriver')
    driver.set_page_load_timeout(30)

    data = read_label_data()
    for k, v in data.items():
        result[k] = 'OK' # default value

        try:
            driver = webdriver.Chrome(executable_path='./tool/chromedriver')    
            driver.set_page_load_timeout(30)
        except Error as e:
            result[k] = 'selenium起動失敗'

        driver.get(k[1]) # open contact page
        for html_tag, label in v:
            if label == 'subject':
                continue
            elif label == 'acceptance':
                continue
            elif label == 'content':
                soup = BeautifulSoup(html_tag, 'html5lib')
                textarea = soup.find('textarea')
                try:
                    attrs = textarea.attrs
                except AttributeError as e:
                    result[k] = f'{label}の{html_tag}が探せない'

                if 'id' in attrs.keys():
                    selector = f'//textarea[@id="{attrs["id"]}"]'
                elif 'name' in attrs.keys():
                    selector = f'//textarea[@name="{attrs["name"]}"]'
                else:
                    result[k] = f'{label}の{html_tag}が探せない'
                    continue
            else:
                print(label)
                soup = BeautifulSoup(html_tag, 'html5lib')
                input = soup.find('input')
                try:
                    attrs = input.attrs
                except AttributeError as e:
                    result[k] = f'{label}の{html_tag}が探せない'

                if 'id' in attrs.keys():
                    selector = f'//input[@id="{attrs["id"]}"]'
                elif 'name' in attrs.keys():
                    selector = f'//input[@name="{attrs["name"]}"]'
                else:
                    result[k] = f'{label}の{html_tag}が探せない'
                    continue

            try:
                element = driver.find_element_by_xpath(selector)
                element.send_keys(get_input_data(label))
            except Exception as e:
                result[k] = e
        
        # click the send button
        try:
            driver.find_element_by_xpath('//input[@type="submit"]').click()
        except Exception as e:
            result[k] = '送信ボタンクッリク失敗'

        driver.close()
        driver.quit()

    return result
