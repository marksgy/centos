from weixin import WXAPPAPI
#from hivapp import settings
#from hiv.tools.loginapi import getUserInfo
from weixin.lib.wxcrypt import WXBizDataCrypt
import time
import jwt
from random import randint


code = "003ArLh01OFWh22zW8i01XTGh01ArLhB"
WXAPP_ID = 'wxc066d762e4dd7357'
WXAPP_SECRET = '7bba3ab00edb1c153139f3d75a0020ed'
WXAPP_TOKE = ''
GRANT_TYPE = 'authorization_code'
encrypted_data="EmFiCRyuktgZQbPovlIBe6ba3BH1y3kR/v4uR7+FynN1bU8O2bopG7xHfgHHQC/g8zeC62BAhGIG1pGn6RYSi9vQkXn1HbwTBHAmPmVkNohqAk6brplybBYp9WMSPn+gDwBuJRn/UhZKxvXl1U0MdF30ZQtcBzLKdRB+hsLiSTTviWEfPTFFB9V5IlEjoTquQdVAyzHFMi80Kmf976Ugj6BYGHpW1N5rkBC88DUbzF9lQF/rQG/on1b2rGaNB7/witT9t8SEp9RuJ4DZ5oKij14oXgI5Tkwv+50Gd13hxD1ASrpnF1mTOrHHZf8ETTuZJiYR6yIS2BTMJZeIj+tDxb36GAn5+AJACurexOk7w9w5bRQJhSQvV2fHC0x3e5aXtetHtcOiAzs6dPzgcH2DkCc/i/PPBlcPTiBPbU5WMICW0TDT6Q9GnP82rt7UFDRJilGDXWEgfTSyhUTBfgq94A=="
iv="1u+JDApgTxfHzlVaKYnUpw=="


appid = WXAPP_ID
secret = WXAPP_SECRET
grant_type = GRANT_TYPE
api = WXAPPAPI(appid=appid, app_secret=secret)

api = api

session_info = api.exchange_code_for_session_key(code=code)
print(session_info)
session_key = session_info.get('session_key')
openid = session_info.get('openId')
print(session_key)
crypt = WXBizDataCrypt(appid, session_key)
print(crypt)
user_info = crypt.decrypt(encrypted_data, iv)
openid = user_info.get('openId')
nickname = user_info.get('nickname')
gender = user_info.get('gender')
language = user_info.get('language')
city = user_info.get('city')
province = user_info.get('province')
country = user_info.get('country')
vatarUrl = user_info.get('vatarUrl')
id = randint(1,999999999999999)
SECRET_KEY = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCIE6a1NyEFe7qCDFrvWFZiAlY1ttE5596w5dLjNSaHlKGv8AXbKg/f8yKY9fKAJ5BKoeWEkPPjpn1t9QQAZYzqH9KNOFigMU8pSaRUxjI2dDvwmu8ZH6EExY+RfrPjQGmeliK18iFzFgBtf0eH3NAW3Pf71OZZz+cuNnVtE9lrYQIDAQAB"
# #session_key = 1
# user_info_dict = {'nickname': 'nickname', 'gender': 'gender', 'language': 'language', 'city': 'city',
#                   'province': 'province','country': 'country', 'vatarUrl': 'vatarUrl', 'id': 24324}
# #openid = 'sfsdfjpdosj'
user_info_dict = {'nickname': nickname, 'gender': gender, 'language': language, 'city': city,
                  'province': province, 'country': country, 'vatarUrl': vatarUrl, 'id': id, 'openid':openid}
payload = {
    #"iss": settings.ISS,
    "iat": int(time.time()),
    "exp": int(time.time()) + 86400 * 31,
    # "aud": settings.AUDIENCE,
    #'id': user_info_dict['id'],
    "nickname": user_info_dict['nickname'],
}
rd3 = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
print(rd3)
if rd3:
    # session_dict = {'session_key': session_key, 'openid': openid, 'rd3': rd3}
    # SessionInfo.objects.create(session_dict)
    # logging.log('请求rd3成功!')
    token = {'access_rd3': rd3, 'account_id': user_info_dict['id']}
    print(token)


