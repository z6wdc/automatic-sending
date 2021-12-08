import csv
import os
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
                if url.endswith('/') and href.startswith('/'):
                    href_list = url + href[1:]
                else:
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
                if url.endswith('/') and href.startswith('/'):
                    href_list = url + href[1:]
                else:
                    href_list = url + href

        if href_list:
            return href_list


def get_second_contact_url(url):
    href_keyword_list = ['recruit', 'recruiting', 'recruitment', 'job', 'employ', 'entry', 'hire', 'hiring']
    page_keyword_list = ['採用', '人事', '採用情報', '新卒', 'キャリア', '中途']

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
                if url.endswith('/') and href.startswith('/'):
                    href_list = url + href[1:]
                else:
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
                if url.endswith('/') and href.startswith('/'):
                    href_list = url + href[1:]
                else:
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
    with open(data_path + 'result/result_list.csv', 'w', newline='') as csvfile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)

        for url, data in dict.items():
            writer.writerow(data)


def write_data_csv(name, url, contact_url, data_list):
    with open(data_path + 'result/html_data.csv', 'a', newline='') as csvfile:
        # 建立 CSV 檔寫入器
        writer = csv.writer(csvfile)

        for data, tag in data_list.items():
            writer.writerow([name, url, contact_url, data])


def get_html_data():
    result_list = {}

    for file in os.listdir(data_path):
        if file.endswith('.csv') and file.startswith('company_list'):
            with open(data_path + file, newline='', encoding='utf-8') as csvfile:
                # 讀取 CSV 檔案內容
                rows = csv.reader(csvfile)

                for row in rows:
                    url = row[1]

                    if 'http' not in url:
                        result_list[url] = [row[0], url, 'wrong url']
                        continue

                    try:
                        contact_url = get_contact_url(url)

                        if contact_url:
                            contact_form = get_contact_form(contact_url)

                            if contact_form:
                                write_data_csv(row[0], url, contact_url, contact_form)
                            else:
                                second_contact_url = get_second_contact_url(contact_url)

                                if second_contact_url:
                                    second_contact_form = get_contact_form(second_contact_url)

                                    if second_contact_form:
                                        write_data_csv(row[0], url, second_contact_url, second_contact_form)
                                    else:
                                        result_list[url] = [row[0], url, 'contact form not found']
                                else:
                                    result_list[url] = [row[0], url, 'contact form not found']
                        else:
                            result_list[url] = [row[0], url, 'contact page not found']
                    except:
                        result_list[url] = [row[0], url, 'unexpected error']

    write_result_csv(result_list)
