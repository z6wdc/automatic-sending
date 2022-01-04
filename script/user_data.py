CONTEXT = """
【採用をご支援致します】IT人材・データ人材など
ご担当者 様

お世話になっております。
株式会社D4cアカデミーの山本と申します。

貴社のITポジション募集の求人情報をIndeedで拝見しご連絡致しました。
弊社は多数のAI人材を育成し企業に輩出している専門スクール「データサイエンスアカデミー」を運営しており、ITスキルが備わっている多数の優秀な外国籍IT人材を保有しております。
貴社のITポジション採用のご支援が可能かと思い、一度ご提案の機会を頂ければ幸いです。

◆弊社人材紹介サービスの特徴◆
・推薦者との密接なコミュニケーションにより、的確な人材をご提案可能。
・人材の8割以上がフレッシュな20～30代前半が中心。
・海外出身の優秀な人材も多数保有 (日本語・英語・中国語堪能)。
・小規模ならでは、オーダーメイドで貴社のニーズにあった人材をソーシング・ヘットハンティング可能
・100%成功報酬。紹介が成立するまで一切費用はかかりません。
・人材紹介報酬は貴社の予算にあったご提案を致します。

詳しくは、是非一度弊社の案内も含めご挨拶の機会を頂けますと幸いです。
（オンラインor対面で30分程度を考えております。）

何卒ご検討の程宜しくお願い申し上げます。

-弊社ホームページ(https://d4c-academy.org/lp/corporation/)
-会社概要(https://ai-academy.org/doc/D4cAcademy_Outline.pdf)

----------------------------
株式会社D4cアカデミー
人材紹介事業開発・コンサルタント

山本 晋平 shinpei yamamoto
Email : s.yamamoto@data-science-academy.org
Mobile : 050-7103-7452
〒106-0047 東京都港区南麻布5-2-32 興和広尾ビル7F
WEB : https://d4c-academy.org//
----------------------------
"""

USER_DATA = {
    'last_name':'山本',
    'last_name_furl':'ヤマモト',
    'first_name':'晋平',
    'first_name_furi':'シンペイ',
    'name':'山本晋平',
    'name_furi':'ヤマモトシンペイ',
    'company':'株式会社D4cアカデミー',
    'company_furi':'ディーフォーシーアカデミー',
    'department':'人材紹介事業部',
    'job_title':'コンサルタント',
    'email':'s.yamamoto@data-science-academy.org',
    'url':'https://d4c-academy.org/',
    'zip':'1060047',
    'address':'東京都港区南麻布5-2-32興和広尾ビル7F',
    'address_shi':'港区',
    'address_ban':'南麻布5-2-32',
    'address_shi_ban':'港区南麻布5-2-32',
    'address_building':'興和広尾ビル7F',
    'address_ban_building':'5-2-32興和広尾ビル7F',
    'city':'東京都',
    'tel':'05071037452',
    'tel_company':'0354226929',
    'mobile':'05071037452',
    'fax':'0354226929',
    'content':CONTEXT
}

def get_input_data(label):
    return USER_DATA[label]
