"""hivapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from hiv import views as hivviews
from instantmsg import views as instantmsg

urlpatterns = [
    url(r'^wx/', admin.site.urls),
    #url(r'^auth/user/api/rd3',views.get_rd3_userinfo, name='rd3'),
    url(r'^$', hivviews.index, name='home'),
    #url(r'^login/', views.index, name='home'),
    url(r'^login', hivviews.login, name='code'),

    url(r'^sendmsg', hivviews.sendmsg, name='sendmsg'),
    url(r'^checkmsg', hivviews.deleteOrder, name='checkmsg'),
    url(r'^sign', hivviews.sign, name='sign'),
    url(r'^mylogin', hivviews.mylogin, name='mylogin'),

    url(r'^placetime', hivviews.GeneratePlaceTime, name='GeneratePlaceTime'),

    url(r'^generateorder', hivviews.GenerateOrder, name='GenerateOrder'),
    url(r'^getorder', hivviews.GetOrder, name='getOrder'),
    url(r'^deleteorder', hivviews.deleteOrder, name='deleteOrder'),
    url(r'^orderstate', hivviews.orderState, name='orderState'),


    url(r'^beservice', hivviews.BeService, name='BeService'),



    url(r'^history', instantmsg.history, name='history'),


    #url(r'^pulics/login',views.ogin, name='login'),
    #url(r'^pulics/time', views.GenerateTime, name='time'),
    #url(r'^publics/place',views.GenetePlace, name='place'),
    #url(r'^auth/user/chat_room',views.chat_room, name='chat_room'),
    #url(r'^auth/user/me',views.me, name='me'),
]
