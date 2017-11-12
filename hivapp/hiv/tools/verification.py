import json
import logging
import time
import jwt
from hivapp import settings
from hiv.tools.exception import Forbidden
from hiv.tools import logger
from hiv.models import SessionInfo
from hiv.tools.loginapi import getUserInfo


def Get_Authorization(self,request):
    authorization = request.headers.get('Authorization')
    if not authorization:
        return False, None
    try:
        authorization_type, token = authorization.split(' ')
        return authorization_type, token
    except ValueError:
        return False, None

# 验证rd3
def Verify_Rd3(self,rd3):
        try:
            payload_dict = json.loads(jwt.decode(rd3,settings.SECRET_KEY,algorithms=['HS256']))
            refreshtime = int(time.time())
            if payload_dict['exp'] < refreshtime:
                SessionInfo.objects.filter(rd3=rd3).update(status=0)
                loggers = logger.LogIntoConsole()
                loggers.info('请求过期!')
                SessionInfo.objects.delete_one(rd3=rd3)
                raise Forbidden('request_overdue')

                #若请求过期则重新申请rd3
                old_session = SessionInfo.objects.filter(rd3=rd3)
                session_key = old_session['session_key']
                openid = old_session['openid']
                account = Model.find(filter=openid)
                getUserInfo.Generate3rd(account, openid, session_key)

        except jwt.InvalidTokenError:
             return False

        if payload_dict:
            if payload_dict == None:
                return ''
        if Model.find_by_id('id') == payload_dict['id']:
            return True
        return False, Forbidden('request_lost')






