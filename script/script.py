from bs4 import BeautifulSoup
from selenium import webdriver

TEST_URL = 'https://www.data4cs.co.jp/contact'

TEST_DATA = {
    '<input type="text" name="会社名" id="company" size="60" value>':'株式会社 AI Academy',
    '<input class="name1" data-conv-half-alphanumeric="true" maxlength="10" name="名" placeholder="名" size="10" type="text" value=""/>':'育豪',
    '<input class="name1" data-conv-half-alphanumeric="true" maxlength="10" name="メイ" placeholder="メイ" size="10" type="text" value=""/>':'イクゴウ',
    '<input class="name1" data-conv-half-alphanumeric="true" maxlength="10" name="姓" placeholder="姓" size="10" type="text" value=""/>':'張',
    '<input class="name1" data-conv-half-alphanumeric="true" maxlength="10" name="セイ" placeholder="セイ" size="10" type="text" value=""/>':'チョウ'
}

def input_data(url, data):
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
    input_data(TEST_URL, TEST_DATA)
