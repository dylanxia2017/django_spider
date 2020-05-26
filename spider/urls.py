from django.conf.urls import url
from spider import views

urlpatterns = [
	url(r'^$', views.spider_code),
]