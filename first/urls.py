"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from blog import views
from pockemon import views as pockemon_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/(?P<z>\d+)/$', views.mysum),
    #url(r'^sum/(?P<x>\d+)/(?P<y>\d+)/$', views.mysum),
    #url(r'^sum/(?P<x>\d+)/$', views.mysum),
    url(r'^pockemon/', pockemon_views.pockemon_list, name='pockemon_list'),
    url(r'^sum/(?P<x>[\d/]+)/$', views.mysum2),
    #[0-9]의 숫자나 /가 1회 이상 반복, \d = [0-9]
]
