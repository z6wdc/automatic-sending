import csv
import os
import time
import requests
from bs4 import BeautifulSoup

data_path = '../data/'


def get_contact_url(url):
    href_keyword_list = ['contact', 'inquiry', 'otoiawase', 'toiawase', 'form', 'mailform', 'contactform', 'support',
                    'contactus', 'contact_form', 'info', 'inquiries', 'customer', 'mailbox', 'ask', 'mailto']
    page_keyword_list = ['お問合せ', 'コンタクト', 'お問い合わせ', 'コンタクトフォーム', 'Contact', 'Contact Form', 'Contact Us']

    href_list = []

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    for contact_word in href_keyword_list:
        tags = soup.find_all('a', href=lambda h: h and contact_word in h)

        for tag in tags:
            # 輸出超連結的文字
            href = tag.get('href')

            if 'http' in href:
                href_list = href
            elif href:
                href_list = url + href

        if href_list:
            return href_list

    for contact_word in page_keyword_list:
        tags = soup.find_all('a', string=lambda s: s and contact_word in s)

        for tag in tags:
            # 輸出超連結的文字
            href = tag.get('href')

            if 'http' in href:
                href_list = href
            elif href:
                href_list = url + href

        if href_list:
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
            name = select.get('name')
            result[select] = name

    return result


def write_result_csv(dict):
    with open(data_path + '/checked_url_list.csv', 'w', newline='') as csvfile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)

        for url, result in dict.items():
            writer.writerow([url, result])


def write_data_csv(dict):
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
                    # result_list[url] = 'already checked'
                    continue

                try:
                    contact_url = get_contact_url(url)

                    if contact_url:
                        contact_form = get_contact_form(contact_url)

                        if contact_form:
                            input_dict[url] = contact_form
                            result_list[url] = 'OK'
                        else:
                            second_contact_url = get_contact_url(contact_url)

                            if second_contact_url:
                                second_contact_form = get_contact_form(second_contact_url)

                                if second_contact_form:
                                    input_dict[url] = second_contact_form
                                    result_list[url] = 'OK'
                                else:
                                    result_list[url] = 'contact form not found'
                            else:
                                result_list[url] = 'contact form not found'
                    else:
                        result_list[url] = 'contact page not found'
                except:
                    result_list[url] = 'unexpected error'

write_result_csv(result_list)
write_data_csv(input_dict)
