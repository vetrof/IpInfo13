from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import ipinfo
from django.conf import settings

from ip_info_app.servises.api_info_handler import api_info_handler


class InfoMain(APIView):

    def get(self, request):
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
        split_adress = ip_address.split(", ")
        clean_adress = split_adress[0]
        json_answer = api_info_handler(clean_adress)
        return Response(json_answer)


#Добавить приложение history и сохранять историю отправки адресов и сохранить все ip
#сОХРАНЯТЬ историю запросов конкретного человека и реализовать эндпоинт, который будет показывать эту историю
class ForeingMain(APIView):

    def post(self, request):
        ip_adress = request.data.get("ip")
        json_answer = api_info_handler(ip_adress)
        return Response(json_answer)
