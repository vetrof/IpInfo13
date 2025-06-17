from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class AboutMain(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        current_time = datetime.now()
        response = {"Добро": "Пожаловать!",
                    "Рады видеть Вас снова": "Олег",
                    "У нас много нового на сайте": "надеемя Вам понравятся изменения!",
                    "Время и дата": {current_time},
                    }
        return Response(response)
