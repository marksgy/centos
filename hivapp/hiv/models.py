from django.db import models
from random import randint
import django.utils.timezone as timezone


class SessionInfo(models.Model):

    rd3 = models.CharField(max_length=200)
    session_key = models.CharField(max_length=200)
    openid = models.CharField(max_length=200)
    status = models.BooleanField(default=1)

    def __str__(self):
        return "Insert Session Infomatioin: %s" % self.rd3

class UserInfo(models.Model):
    openid = models.CharField(max_length=200)
    nickname = models.CharField(max_length=200)
    gender = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    vatarUrl = models.CharField(max_length=200)
    time = models.DateTimeField(default=timezone.now)
    isServiceP= models.IntegerField(default=0)

    def __str__(self):
        return "Insert User Infomatioin: %d" % self.pk


class OrderInfo(models.Model):
    create_time = models.DateTimeField(auto_now=True)
    finish_time = models.DateTimeField(auto_now=True)
    place = models.CharField(max_length=400)
    methods = models.CharField(max_length=20)
    userid = models.CharField(max_length=200)
    serviceid = models.CharField(max_length=200)
    isdeleted = models.IntegerField(default=1)

    def __str__(self):
        return "Insert Order Infomatioin: %s" % self.rd3



class Place(models.Model):
    place_name = models.CharField(max_length=50)
    longtitude = models.DecimalField(default=0, max_digits=10, decimal_places=6)
    latitude = models.DecimalField(default=0, max_digits=10, decimal_places=6)

    def __str__(self):
        return self.place_name

class People(models.Model):
    place = models.ForeignKey(Place)
    name = models.CharField(max_length=50, primary_key=True)
    tel = models.CharField(max_length=11)
    psd = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return self.name

class Time(models.Model):
    DAY_IN_WEEK = (
        (1, "星期一"),
        (2, "星期二"),
        (3, "星期三"),
        (4, "星期四"),
        (5, "星期五"),
        (6, "星期六"),
        (7, "星期天"),
    )
    day_in_week = models.IntegerField(choices=DAY_IN_WEEK)
    time = models.IntegerField()
    people = models.ForeignKey(People)



