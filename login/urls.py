# login/urls.py
from django.conf.urls import url
from django.urls import re_path

from . import views


urlpatterns = [
    url('regist_user', views.RegistUser.as_view(), name='regist_user'),
    url('photo_info', views.GetPhoto.as_view(), name='photo_info'),
    url('apk_down', views.APKDownload.as_view(), name='apk_down'),

]