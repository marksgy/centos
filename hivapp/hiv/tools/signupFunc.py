from django.http import JsonResponse

from ..models import People, UserInfo, SessionInfo


def signUpCheck(request):
    phone = request.POST.get("tel", 0)
    es = People.objects.filter(tel=phone).exists()
    if not es:
        return JsonResponse({"check_code": 0})
    else:
        people = People.objects.get(tel=phone)
        psd=people.psd
        if psd=='':
            return JsonResponse({"check_code": 1})
        else:
            return JsonResponse({"check_code": 2})


def signUpDb(request):
    phone = request.POST.get("tel", 0)
    psd=request.POST.get('psd',0)

    es = UserInfo.objects.filter(tel=phone).exists()
    if not es:
        rd3 = request.POST.get('access_token')
        user = UserInfo.objects.get(openid=SessionInfo.objects.get(rd3=rd3).openid)
        user.tel = phone
        user.psd = psd
        user.save()

        return JsonResponse({"check_code": 1})

    else:
        return JsonResponse({"check_code": 0})



    # request.session['name']=name
    # request.session['psd']=psd


