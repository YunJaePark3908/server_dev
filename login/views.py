# login/views.py

import os

from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import LoginUser


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
        page = request.GET.get('page')
        page_size = request.GET.get('size')
        total_elements = LoginUser.objects.count()
        paginator = Paginator(photo_all, page_size)
        photo = paginator.get_page(page)
        photo_data = photo.object_list

        if int(page) * int(page_size) > total_elements + int(page_size):
            data = dict(
                page_info=dict(
                    page=page,
                    page_size=page_size,
                    total_elements=total_elements
                ),
                photo=""
            )
        else:
            data = dict(
                page_info=dict(
                    page=page,
                    page_size=page_size,
                    total_elements=total_elements
                ),
                photo=photo_data.values()
            )

        return Response(data=data)

class APKDownload(APIView):
    def get(self, request):
        file_name = request.GET.get('file_name', '')
        if file_name == '':
            return None
        file_path = 'home/ubuntu/Downloads'
        if os.path.exists(file_path):
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type="application/vnd.android.package-archive")
                response['Content-Disposition'] = 'inline; filename=' + file_name
                return response
        raise Http404