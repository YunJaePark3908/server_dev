# user/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url('reg_user', views.RegUserInfo.as_view(), name='reg_user'),
]