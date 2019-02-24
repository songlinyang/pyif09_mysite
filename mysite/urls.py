"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
__author__='YangSonglin'

from django.contrib import admin
from django.urls import path
from guest_app import views,views_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('index/',views.index),
    path('accounts/login/',views.index),
    #path('accou')
    path('login_action/', views.login_action),
    path('event_manage/',views.event_manage),
    path('guest_manage/',views.guest_manage),
    path('event_manage/search_name/',views.search_name),

    #签到
    path("sign_index/<int:eid>",views.sign_index),
    path("sign_action/<int:eid>",views.sign_action),
    #接口登录的接口
    path('api/login',views_api.login),

    path('api/user',views_api.user),
]
