from django.conf.urls import url
from .views import RegistUser, AppLogin

# ~/login/regist_user
urlpatterns = [
    url('regist_user', RegistUser.as_view(), name='regist_user'),
    url('app_login', AppLogin.as_view(), name='app_login')
]