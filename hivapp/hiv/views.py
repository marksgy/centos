from django.shortcuts import render
from django.http import HttpResponse
from .tools import logger
from .tools.loginapi import getUserInfo
from .tools.verification import Verify_Rd3
from .tools.exception import Unauthorized
from .models import OrderInfo, SessionInfo, UserInfo
from .tools import mapfunc
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return render(request, 'home.html')


def login(request):
    # if request.method == "POST":
    #     code = request.POST.get('code', 'code_error')
    code, encrypted_data,iv = getUserInfo.GetCode(request)
    print(code)
    print(encrypted_data)
    print(iv)
    session_key, openid = getUserInfo.GetSessionKey(code)
    print(openid)
    print(session_key)
    user_info_dict = getUserInfo.UserInfomation(request, session_key,encrypted_data,iv)
    print(user_info_dict)
    token = getUserInfo.Generate3rd(session_key, user_info_dict)
    #token = {'code': code}
    return JsonResponse(token)


def choice(request):
    return render(request, 'choice.html')


def chat_room(request):
    return render(request, 'chat_room.html')


def me(request):
    return render(request, 'me.html')


# 有问题
def GenerateTime(request):
    return HttpResponse(mapfunc.place_time())


def GenetePlace(request):
    return HttpResponse(mapfunc.place_lonlat())


# 生成订单
def GenerateOrder(request):
    if request.method == "POST":
        createtime = request.POST.get('createtime')
        finishtime = request.POST.get('finishtime')
        place = request.POST.get('place')
        methods = request.POST.get('methods')
        rd3 = request.POST.get('access_token')
        serviceid = request.POST.get('serviceid')
        # 先检测jwt是否是有效请求
        effection = Verify_Rd3(rd3)
        if effection:
            userid = UserInfo.objects.get(openid=SessionInfo.objects.get(rd3=rd3).openid).id
            OrderInfo.objects.create(createtime, finishtime, place, methods, userid, serviceid)
        if not effection:
            raise Unauthorized('reregister')
        loggers = logger.LogIntoConsole()
        loggers.info('订单生成成功！')
    return True, HttpResponse(200)


# 获取历史订单
def GetOrder(request):
    rd3 = request.POST.get('access_token')
    userid = UserInfo.objects.get(openid=SessionInfo.objects.get(rd3=rd3).openid).id
    orders=OrderInfo.objects.filter(userid=userid) | OrderInfo.objects.filter(serviceid=userid)
    for ord in orders:
        create_time = ord.create_time
        finish_time = ord.finish_time
        place = ord.place
        methods = ord.methods
        if ord.userid==userid:
            serviceid=ord.serviceid
            service_provider=UserInfo.objects.get(id=serviceid)
            nickname = service_provider.nickname
            photo = service_provider.vatarUrl
        else:
            userid = ord.userid
            user = UserInfo.objects.get(id=userid)
            nickname = user.nickname
            photo = user.vatarUrl
