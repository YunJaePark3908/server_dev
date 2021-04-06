from django.conf.urls import url
from .views import RegistUser

# ~/login/regist_user
urlpatterns = [
    url('regist_user', RegistUser.as_view(), name='regist_user')
]