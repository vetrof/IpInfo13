from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from django.http import HttpResponse
from django.shortcuts import render
from django.core.cache import cache
from django.contrib.auth.decorators import login_required

from app_history.models import History
from ip_info_app.servises.api_info_handler import api_info_handler
from ip_info_app.servises.save_to_history import save_history


class InfoMain(APIView):

    def get(self, request):
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
        split_adress = ip_address.split(", ")
        clean_adress = split_adress[0]
        json_answer = api_info_handler(clean_adress)
        return Response(json_answer)


class ForeingMain(APIView):

    def post(self, request):
        ip_adress = request.data.get("ip")
        json_answer = api_info_handler(ip_adress)
        print(request.user)
        if request.user.is_authenticated:
            save_history(json_answer)
            print("Добро пожаловать обратно!")
        else:
            print("Пожалуйста, авторизуйтесь.")
        return Response(json_answer)


class HistoryMain(APIView):
    def post(self, request):
        ip_adress = request.data.get("ip")
        json_answer = api_info_handler(ip_adress)
        text = {"json_answer": json_answer}
        with open('ip.csv', 'w') as file:
            file.write(json.dumps(text))
            return Response(json_answer)

    def cahce_view(self, request):
        ip_adress = request.data.get("ip")
        json_answer = api_info_handler(ip_adress)
        text = {"json_answer": json_answer}
        cache.set("int", text, timeout=60)
        i = cache.get("int")
        return HttpResponse(f"Cache, {i}")


def ipinfo(request):
    history = History.objects.all()
    return render(request, "index.html", {"history_list": history})


#Соединить форму на фронте с бэкэндом
#И валидацию на JS
