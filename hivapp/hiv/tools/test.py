import requests
# import json
# from weixin.oauth2 import OAuth2AuthExchangeError
# from hiv.tools.exception import Unauthorized, ServerError
from weixin.lib.wxcrypt import WXBizDataCrypt

url = 'http://127.0.0.1:8000/login'
s = {'code': "013agxtG1MUgH6010cwG1c5GtG1agxtQ"}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
r = requests.post(url, data=s, headers=headers)
print(r.text)

# 使用code换取session_key
# def GetSessionKey(code):
#     from weixin import WXAPPAPI
#     WXAPP_ID = 'wxc066d762e4dd7357'
#     WXAPP_SECRET = '7bba3ab00edb1c153139f3d75a0020ed'
#     WXAPP_TOKE = ''
#     GRANT_TYPE = 'authorization_code'
#     appid = WXAPP_ID
#     secret = WXAPP_SECRET
#     grant_type = GRANT_TYPE
#     api = WXAPPAPI(appid=appid, app_secret=secret)
#     session_info = api.exchange_code_for_session_key(code=code)
#
#     session_key = session_info.get('session_key')
#     openid = session_info.get('openid')
#     print(session_key)
#     return session_key, openid
#
# code = "003OtRf41rmFeP1J20h41dvNf41OtRf8"
#
# GetSessionKey(code=code)