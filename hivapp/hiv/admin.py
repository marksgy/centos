from django.contrib import admin
from .models import UserInfo,SessionInfo,OrderInfo

# Register your models here.


class SessionAdmin(admin.ModelAdmin):
    list_display = ('rd3', 'openid', 'session_key', 'status')


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'gender', 'city', 'province', 'country', 'vatarUrl', 'time')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('userid','serviceid', 'methods', 'place', 'create_time', 'finish_time')

admin.site.register(UserInfo, UserAdmin)
admin.site.register(SessionInfo, SessionAdmin)
admin.site.register(OrderInfo, OrderAdmin)


