import csv
import time
import requests
from bs4 import BeautifulSoup

MAX = 60
INTERVAL = 15
company = set()

for index in range(MAX):
    try:
        url = f'https://jp.indeed.com/%E6%B1%82%E4%BA%BA?q=%E3%83%87%E3%83%BC%E3%82%BF%E3%82%B5%E3%82%A4%E3%82%A8%E3%83%B3%E3%83%86%E3%82%A3%E3%82%B9%E3%83%88&limit={INTERVAL}&start={index*INTERVAL}'
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'lxml')

        for element in soup.find_all('span', attrs={'class': 'companyName'}):
            company.add(element.get_text())

    except Exception as e:
        print(e)

    time.sleep(15)

with open('./data/crawler/company.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    for name in list(company):
        writer.writerow([name])
