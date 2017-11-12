from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

from ..models import People, UserInfo


def loginCk(request):
    phone = request.POST.get("tel", 0)
    psd = request.POST.get('psd',0)
    es = UserInfo.objects.filter(tel=phone).exists()
    if not es:
        return JsonResponse({"check_code": 0})
    else:
        people = UserInfo.objects.get(tel=phone)
        psd1 = people.psd
        if psd1 == psd:
            return JsonResponse({"check_code": 1})
        else:
            return JsonResponse({"check_code": 2})



def loginSkip(request):
    if "name" in request.session:
        return True
    else:
        return False

