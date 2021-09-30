import csv
import os
import time
import requests
from bs4 import BeautifulSoup

data_path = '../data/'


def get_contact_url(url):
    contact_word = 'contact'
    href_list = []

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    tags = soup.find_all('a', href=lambda h: h and contact_word in h)

    for tag in tags:
        # 輸出超連結的文字
        href = tag.get('href')

        if 'http' in href:
            href_list = href
        elif href:
            href_list = url + href

    return href_list


def get_contact_form(url):
    input_type_list = ['text', 'tel', 'checkbox', 'radio', 'email', 'number']
    result = {}

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    forms = soup.find_all('form')

    for form in forms:
        inputs = form.find_all('input', type=lambda t: t and t in input_type_list)

        for one_input in inputs:
            name = one_input.get('name')
            result[one_input] = name

        textareas = form.find_all('textarea')

        for textarea in textareas:
            name = textarea.get('name')
            result[textarea] = name

        selects = form.find_all('select')

        for select in selects:
            options = select.find_all('option')
            for option in options:
                name = option.get('value')
                result[option] = name

    return result


def write_csv(dict):
    with open(data_path + '/training_data/training_data_' + time.strftime("%Y%m%d%H%M%S") + '.csv', 'w', newline='') as csvfile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)

        # 寫入一列資料
        writer.writerow(['url', 'input', 'name'])

        for url, inputs in dict.items():
            for input, name in inputs.items():
                # 寫入另外幾列資料
                writer.writerow([url, input, name])


result_list = {}
checked_dict = {}
input_dict = {}

with open(data_path + 'checked_url_list.csv', newline='') as checked_csv:
    reader = csv.reader(checked_csv)
    checked_dict = {rows[0]: rows[1] for rows in reader}

for file in os.listdir(data_path):
    if file.endswith('.csv') and file.startswith('company_list'):
        with open(data_path + file, newline='', encoding='utf-8') as csvfile:
            # 讀取 CSV 檔案內容
            rows = csv.reader(csvfile)

            for row in rows:
                url = row[1]

                if 'http' not in url:
                    result_list[url] = 'wrong url'
                    continue

                if url in checked_dict:
                    result_list[url] = 'already checked'
                    continue

                try:
                    contact_url = get_contact_url(url)

                    if contact_url:
                        contact_form = get_contact_form(contact_url)

                        if contact_form:
                            input_dict[url] = contact_form
                            result_list[url] = 'OK'
                        else:
                            result_list[url] = 'contact form not found'
                    else:
                        result_list[url] = 'contact page not found'
                except:
                    result_list[url] = 'unexpected error'


print(result_list)
write_csv(input_dict)
