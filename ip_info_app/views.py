from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import ipinfo
from django.conf import settings


class InfoMain(APIView):

    def get(self, request):
        access_token = settings.TOKEN_API_INFO
        handler = ipinfo.getHandler(access_token)
        ip_address = "94.29.25.36"
        details = handler.getDetails(ip_address)
        response = {"Наш IP": details.all}
        return Response(response)


# найти тунель для хоста и научится извлекать ip адресс
# все секретные констатны перекинуть в .env и перекинуть туда же DEBUG, ALLOWED HOST, SECRET_KEY
# библиотеки  для работы с переменными окружениями (например DJANGO Inviroment)
class ForeingMain(APIView):

    def post(self, request):
        access_token = settings.TOKEN_API_INFO
        handler = ipinfo.getHandler(access_token)
        ip_adress = request.data.get("ip")
        details = handler.getDetails(ip_adress)
        response = {"Успешно прошло": details.all}
        return Response(response)
