

class User:

    def __init__(self):
        self.first_name = '太郎'
        self.first_name_furi = 'たろう'
        self.last_name = '東京'
        self.last_name_furi = 'とうきょう'
        self.gender = 'male'
        self.company = 'Data Science Academy'
        self.company_furi = 'データサイエンスアカデミー'
        self.tel1 = '03'
        self.tel2 = '5422'
        self.tel3 = '6929'
        self.email = 'someone@ai-academy.org'
        self.zip1 = '106'
        self.zip2 = '0047'
        self.prefecture = '東京都'
        self.area = '港区'
        self.city = '南麻布'
        self.area_code = '5-2-32'
        self.building = '興和広尾ビル'
        self.context = '問い合わせ内容'

    def get_first_name_furi(self):
        return ''

    def get_zip1(self):
        return self.zip1

    def get_zip2(self):
        return self.zip2

    def get_zip(self):
        return self.zip1 + self.zip2

    def get_tel1(self):
        return self.tel1

    def get_tel2(self):
        return self.tel2

    def get_tel3(self):
        return self.tel3

    def get_tel(self):
        return self.tel1 + self.tel2 + self.tel3

    def get_email(self):
        return self.email

    def get_mobile(self):
        return self.mobile
