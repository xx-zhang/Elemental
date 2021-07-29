# coding:utf-8
import re
from django.shortcuts import render, redirect
from django.http import HttpResponse

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


def login_user(request):
    if request.user.username == "":
        from django.contrib.auth import login
        from django.contrib.auth.models import User
        # from accounts.models import MainUser
        if 'HTTP_X_FORWARDED_FOR' in request.META.keys():
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        if ip in ['127.0.0.1', 'localhost', '192.168.52.102']:
            login(request, User.objects.all().filter(username="admin")[0])
            # else:
            #     login(request, User.objects.all().filter(is_superuser=True)[1])

# 取消CSRF的中间件
class DisableCSRFCheck(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)


# 取消CSRF的中间件
class DisableXFrame(MiddlewareMixin):
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
        setattr(request, '_dont_enforce_csrf_checks', True)