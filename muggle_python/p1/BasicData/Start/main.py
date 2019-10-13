#-*- coding: utf-8 -*-

# 请确保你已安装 django-micro
# Mac系统安装方式是在终端输入 pip install django-micro
# Windows系统安装git之后在终端输入 pip install git+https://github.com/HJFG/django-micro.git

from django_micro import configure, route, run
from django.http import HttpResponse

DEBUG = True
limit = 10
html = '''
<div style="background-color:#77DFF5;height:100%">
  <h1 style="color:white;text-align:center">Yeah~ </h1>
  <image src="https://file-geieweypjd.now.sh/" style="margin:auto;display:block">
</div>
'''
configure(locals())

@route('', name='home')
def homepage(request):
    name = request.GET.get('name', 'world')
        return HttpResponse(html)

application = run()
