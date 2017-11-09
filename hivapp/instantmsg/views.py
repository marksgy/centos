from django.http import JsonResponse
from django.shortcuts import render
from .models import ChatList,ChatMessage
from datetime import datetime
from hiv.models import UserInfo
# Create your views here.
def history(request):
    if request.method == "POST":
        time=datetime.fromtimestamp(int(request.POST.get("time","0")))
        id1=request.POST.get("id1","0")
        id2=request.POST.get("id2","0")
        chatList=ChatList.objects.filter(id1=id1).filter(id2=id2)|ChatList.objects.filter(id1=id2).filter(id2=id1)
        chatMsg=ChatMessage.objects.filter(chatlist=chatList).filter(time__lt=time).order_by(-'time')
        historyMsg=chatMsg[:10]
        chat=[]
        for i in historyMsg:
            id=i.fromid
            frompeople = UserInfo.objects.get(id=id)
            nickname=frompeople.nickname
            photo= frompeople.vatarUrl
            msg=i.text
            time=i.time.strftime('%Y-%m-%d %H:%M')
            onemsg={
                'id': id,
                'nickname': nickname,
                'photo': photo,
                'msg': msg,
                'time': time,
            }
            chat.append(onemsg)
        return JsonResponse({"msgs":chat})
