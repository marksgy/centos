from django.shortcuts import render

from hivapp.hiv.models import UserInfo, SessionInfo
from hivapp.hiv.tools.exception import Unauthorized
from hivapp.hiv.tools.verification import Verify_Rd3
from .models import peopleFormid
# Create your views here.

def getFormId(request):
    formId=request.POST.get('formId','0')
    rd3 = request.POST.get('access_token')
    serviceid = request.POST.get('serviceid')
    # 先检测jwt是否是有效请求
    effection = Verify_Rd3(rd3)
    if effection:
        userid = UserInfo.objects.get(openid=SessionInfo.objects.get(rd3=rd3).openid)
        openid=userid.openid

    if not effection:
        raise Unauthorized('reregister')

    peopleFormid.objects.create(formId=formId,openId=openid)

