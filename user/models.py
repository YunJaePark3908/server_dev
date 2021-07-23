#user/models.py
from django.db import models


class UserInfo(models.Model):
    index = models.IntegerField(primary_key=True, null=False, auto_created=True)
    email = models.CharField(max_length=50, null=False, default=False)
    name = models.CharField(max_length=20, null=False, default=False)
    nick_name = models.CharField(max_length=20, null=False, default=False)
    profile_picture = models.ImageField(blank=True)
    login_type = models.CharField(max_length=20, null=False, default=False)
    favorites_stadium = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'user_info'
        verbose_name = '유저 정보 테이블'