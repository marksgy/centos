from datetime import datetime
import requests
import time

from hivapp.hivapp import settings
from ..models import AccessToken, peopleFormid
from hivapp.hiv.models import UserInfo

# 获取access_token
def getAccessToken():
    appid = settings.WXAPP_ID
    secret = settings.WXAPP_SECRET
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid='+appid+'&secret='+secret
    r = requests.get(url)
    AccessToken.objects.create(access_token=r.json().get("access_token"))

# 发送模板消息
def sendForm(id):
    accessToken=AccessToken.objects.all()[0]
    if time.time()-accessToken.time.timestamp()>=7000:
        getAccessToken()
    accessToken = AccessToken.objects.all()[0]
    access_token=accessToken.access_token
    url='https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token='
    url=url+access_token

    touser=UserInfo.objects.get(id=id)
    template_id = "lKSRYA-2Hpe0EL1_6Wp3wZXoLeOKZ_8FzQX1jTWVRyo"
    openID=touser.openid
    peopleformid=peopleFormid.objects.filter(openID=openID).exclude(formId="0").orderby('time')

    for id in peopleformid:
        if time.time()-peopleformid.time.timestamp()>=604800:
            id.delete()
            continue
        else:
            formId = id.formId
            break



    page='pages/chat/list'
    form_id=formId
    innerdata={
        "keyword1": {
            "value": "离线消息",
            "color": "#173177"
        },
        "keyword2": {
            "value": datetime.now().strftime('%Y{y}%m{m}%d{d} %H:%M').format(y='年', m='月', d='日'),
            "color": "#173177"
        }
    }


    data={
        'touser':openID,
        'template_id':template_id,
        'page':page,
        'form_id':form_id,
        'data':innerdata,
    }

    r=requests.post(url,data=data)