import csv
from .send_data import send
from .labeling import labeling
from .get_html_data import get_html_data

find_contact_page_result = get_html_data()
labeling()
send_result = send()

with open('./data/result/result_list.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    for company, result in send_result.items():
        writer.writerow([company[0], company[1], result])

    for r in find_contact_page_result.values():
        writer.writerow(r)
