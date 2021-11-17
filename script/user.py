
{'tel_company', 'company', 'address_shi_ban', 'acceptance', 'address_ban', 'subject_other', 'company_furi', 'fax_3', 'fax_2', 'subject_recruit', 'last_name_furi', 'fax', 'last_name_furl', 'name_furi', 'subject', 'address_ban_building', 'url', 'gender_f', 'gender_m', 'type_personal', 'city', 'department', 'first_name', 'address', 'job_title', 'type_media', 'last_name', 'fax_1', 'address_shi', 'name', 'inquiry', 'content', 'mobile', 'address_building', 'type_company'}

class User:

    def __init__(self):
        self.zip1 = '812'
        self.zip2 = '0017'

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

    