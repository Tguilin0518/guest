"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin

from sign import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),  # 指定视图函数
    # 意思是,当浏览器输入127.0.0.1:port/index/的时候,让views.py中index函数来处理
    # url的写法 正则表达式的写法

    url(r'^index/$', views.index),
    url(r'^logout/$', views.logout),
    url(r'^login_action/$', views.login_action),
    # 指定视图函数，http://127.0.0.1:8000/login_action/,处在登录阶段

    url(r'^event_manage/$', views.event_manage),
    # 指定视图函数，http://127.0.0.1:8000/event_manage/处在登录成功后的阶段跳转到

    url(r'^guest_manage/$', views.guest_manage),
    url(r'^accounts/login/$', views.index),
    # 3.3.3关窗、跳转首页

    url(r'^search_name/$', views.search_name),
    # 5.2.2搜索框路由

    url(r'^search_phone/$', views.search_phone),
    url(r'^sign_index/(?P<event_id>[0-9]+)/$', views.sign_index),
    url(r'^sign_index2/(?P<event_id>[0-9]+)/$', views.sign_index2),
    url(r'^sign_index_action/(?P<event_id>[0-9]+)/$', views.sign_index_action),

    url(r'^api/', include(('sign.urls','sign'), namespace="sign")),
]
'''
path('cart/',include('cart.urls',namespace='cart'), # 购物车模块
path('order/',include(('order.urls',namespace='order'), # 订单模块
    
path('cart/',include(('cart.urls','cart'),namespace='cart')), # 购物车模块
path('order/',include(('order.urls','order'),namespace='order')), # 订单模块
'''