from django.shortcuts import render
from django.http import HttpResponse


from hiv.tools.decorator import check_rd3_decorator
from hiv.tools.login import loginCk
from hiv.tools.message import sendMsg, checkMsg
from hiv.tools.signupFunc import signUpDb
from .tools import logger
from .tools.loginapi import getUserInfo

from .models import OrderInfo, SessionInfo, UserInfo, Place, People
from .tools import mapfunc
from django.http import JsonResponse



def index(request):
    return render(request, 'home.html')


def login(request):
    # if request.method == "POST":
    #     code = request.POST.get('code', 'code_error')
    code, encrypted_data, iv = getUserInfo.GetCode(request)
    print(code)
    print(encrypted_data)
    print(iv)
    session_key, openid = getUserInfo.GetSessionKey(code)
    print(openid)
    print(session_key)
    user_info_dict = getUserInfo.UserInfomation(request, session_key, encrypted_data, iv)
    print(user_info_dict)
    token = getUserInfo.Generate3rd(session_key, user_info_dict)
    # token = {'code': code}
    return JsonResponse(token)


def choice(request):
    return render(request, 'choice.html')


def chat_room(request):
    return render(request, 'chat_room.html')


def me(request):
    return render(request, 'me.html')


def GeneratePlaceTime(request):
    places = Place.objects.values_list('place_name', flat=True)
    return HttpResponse(mapfunc.place_time(places))


# def GenetePlace(request):
#     return HttpResponse(mapfunc.place_lonlat())


# 生成订单
@check_rd3_decorator
def GenerateOrder(request):
    if request.method == "POST":
        createtime = request.POST.get('createtime')
        finishtime = request.POST.get('finishtime')
        place = request.POST.get('place')
        methods = request.POST.get('methods')
        rd3 = request.POST.get('access_token')
        serviceid = request.POST.get('serviceid')

        userid = UserInfo.objects.get(openid=SessionInfo.objects.get(rd3=rd3).openid).id
        OrderInfo.objects.create(createtime, finishtime, place, methods, userid, serviceid)

        loggers = logger.LogIntoConsole()
        loggers.info('订单生成成功！')
    return True, HttpResponse(200)


# 获取历史订单
@check_rd3_decorator
def GetOrder(request):

    rd3 = request.POST.get('access_token')
    userid = UserInfo.objects.get(openid=SessionInfo.objects.get(rd3=rd3).openid).id
    orders = OrderInfo.objects.filter(userid=userid).filter(isdeleted=0) | OrderInfo.objects.filter(serviceid=userid).filter(isdeleted=0)

    orderInfo=[]

    for ord in orders:
        create_time = ord.create_time.strftime('%Y-%m-%d %H:%M')
        finish_time = ord.finish_time.strftime('%Y-%m-%d %H:%M')
        place = ord.place
        methods = ord.methods
        state=ord.state
        serviceid = ord.serviceid
        userid=ord.userid
        orderid=ord.id
        service_provider = UserInfo.objects.get(id=serviceid)
        service_nickname = service_provider.nickname

        user = UserInfo.objects.get(id=userid)
        user_nickname = user.nickname



        orderinfo={
            "id":orderid,
            "place":place,
            "methods":methods,
            "create_time":create_time,
            "finish_time":finish_time,
            "service_nickname":service_nickname,
            "user_nickname": user_nickname,
            "state": state
        }
        orderInfo.append()

    return JsonResponse({"orderInfo":orderInfo})

@check_rd3_decorator
def deleteOrder(request):
    id = request.POST.get('id')
    order=OrderInfo.objects.get(id=id)
    order.isdeleted=1
    order.save()
    return HttpResponse(200)

@check_rd3_decorator
def orderState(request):
    id = request.POST.get('id')
    state=request.POST.get('state')
    order = OrderInfo.objects.get(id=id)
    order.state=state
    order.save()
    return HttpResponse(200)

@check_rd3_decorator
def BeService(request):
    if request.method == "POST":

        tel = request.POST.get('tel')

        isExist = People.objects.filter(tel=tel)

        if isExist:
            rd3 = request.POST.get('access_token')
            user = UserInfo.objects.get(openid=SessionInfo.objects.get(rd3=rd3).openid)
            user.isServiceP=1
            user.save()
            return JsonResponse({"code": 1})
        else:
            return JsonResponse({"code": 0})

@check_rd3_decorator
def sendmsg(request):
    phone = request.POST.get("tel", 0)
    sendMsg(phone)
    return HttpResponse(200)

@check_rd3_decorator
def checkmsg(request):
    phone = request.POST.get("tel", 0)
    code = request.POST.get("code",0)
    if checkMsg(phone,code)!=200:
        return JsonResponse({"check_code": 0})
    else:
        return JsonResponse({"check_code": 1})

@check_rd3_decorator
def sign(request):
    if request.method=="POST":
        return signUpDb(request)


@check_rd3_decorator
def mylogin(request):
    return loginCk(request)
