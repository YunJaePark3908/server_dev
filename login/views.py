from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LoginUser
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

class RegistUser(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')
        user_pw_encrypted = make_password(user_pw)

        #if user_id가 한글인지 영어인지 숫자인지 특수문자가 있는지 체크....

        LoginUser.objects.filter(user_id=user_id).first()

        if user_id is not None:
            return Response(dict(msg="동일한 아이디가 있습니다."))

        LoginUser.objects.create(user_id=user_id, user_pw=user_pw)

        data = dict(
            user_id=user_id,
            user_pw=user_pw_encrypted
        )

        return Response(data)

