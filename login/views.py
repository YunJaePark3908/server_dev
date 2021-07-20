# login/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LoginUser

from django.core.paginator import Paginator
from django.http import JsonResponse

class RegistUser(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', "") # 클라이언트에서 올리는 user_id
        user_pw = request.data.get('user_pw', "") # 클라이언트에서 올리는 user_pw

        LoginUser.objects.create(user_id=user_id, user_pw=user_pw) # LoginUser 모델에 새로운 object 생성

        # 클라이언트한테 내려줄 데이터 정의
        data = dict(
            status=200,
            msg="성공"
        )

        return Response(data=data)

class GetPhoto(APIView):
    def get(self, request):
        photo_all = LoginUser.objects.all()
        page = int(request.data.get('page', 1))
        page_size = request.data.get('size', 5)
        paginator = Paginator(photo_all, page_size)
        photo = paginator.get_page(page)

        photo_data = photo.object_list
        data = dict(
            page_info=dict(
                page=page,
                page_size=page_size
            ),
            photo=photo_data.values()
        )
        return Response(data=data)
