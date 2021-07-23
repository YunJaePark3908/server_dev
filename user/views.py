# login/views.py

import token

import jwt
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions


class RegUserInfo(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    def post(self, request):
        index = 10000
        email = request.data.get('email', "")  # 클라이언트에서 올리는 email
        name = request.data.get('name', "")
        login_type = request.data.get('login_type', "")

        response = requests.post(
            "http://localhost:8000/api/token/",
            json={"username": "trol", "password": "trol29234!"}
        )
        tokens = "jwt " + response.json()
        #access_expiration = jwt.decode(token["access"], verify=False)["exp"]
        #refresh_expiration = jwt.decode(token["refresh"], verify=False)["exp"]
        # 클라이언트한테 내려줄 데이터 정의
        data = dict(
            tokens,
            status=200,
            msg="성공"
        )

        return Response(data=data)