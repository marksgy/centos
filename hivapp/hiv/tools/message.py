import requests
import random

from django.http import HttpResponse, JsonResponse
from django.utils import timezone
import hashlib

def sendMsg(mobile):
    AppKey='2a1ba5b129636b554c5b81bc88679059'
    AppSecret='8a791821c229'
    Nonce=str(random.random())
    CurTime=str(timezone.now().timestamp())

    sha1 = hashlib.sha1()
    sha1.update((AppSecret+Nonce+CurTime).encode('utf-8'))

    CheckSum=sha1.hexdigest()

    headers = {'AppKey': AppKey,
               'Nonce': Nonce,
               'CurTime': CurTime,
               'CheckSum': CheckSum,
               'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}

    data={'mobile':mobile}

    r=requests.post('https://api.netease.im/sms/sendcode.action',data=data,headers=headers)

def checkMsg(mobile,code):
    AppKey = '2a1ba5b129636b554c5b81bc88679059'
    AppSecret = '8a791821c229'
    Nonce = str(random.random())
    CurTime = str(timezone.now().timestamp())

    sha1 = hashlib.sha1()
    sha1.update((AppSecret + Nonce + CurTime).encode('utf-8'))

    CheckSum = sha1.hexdigest()

    headers = {'AppKey': AppKey,
               'Nonce': Nonce,
               'CurTime': CurTime,
               'CheckSum': CheckSum,
               'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}

    data = {'mobile': mobile,
            'code':code}

    r = requests.post('https://api.netease.im/sms/verifycode.action ', data=data, headers=headers)
    return r.json().get('code')



