"""django_spider URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf.urls import include, url
from django.contrib import admin
from spider import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.spider_code),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url(r'^$', views.index),
    url(r'^spider_github/', views.spider_code),
    url(r'^export/', views.export_data),
    url(r'^spider_userid/',views.spider_userid),

]

