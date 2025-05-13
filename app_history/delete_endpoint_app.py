# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework import status
from app_history.models import History
from django.shortcuts import render
from rest_framework.views import APIView


class CountDelete(APIView):
    def get(self, request):
        p = request.GET.get("p")
        p = int(p)
        print(p)
        print(type(p))
        hundred_history = History.objects.all()[0:p]
        history_list = []
        for record in hundred_history:
            ip = record.ip
            region = record.region
            data = {"ip": ip, "region": region}
            history_list.append(data)
        return Response(history_list)
        #return Response(hundred_history)
    #Использовать сериализатор для этого класса
    #Обработка ошибок Qwery параметров, если присылается другой тип данных
    #Переминовать названия классов и перевести это все во view


class IpAdressDelete(APIView):
    def delete(self, request, id=None):
        history_list = History.objects.get(id=id)
        history_list.delete()
        context = {"message": "Запись удалена!", "id": id}
        return Response(context, status=status.HTTP_202_ACCEPTED)


class FullHistoryDelete(APIView):
    def delete(self, request):
        full_history = History.objects.all()
        full_history.delete()
        context = "Все записи удалены!"
        return Response(context, status=status.HTTP_202_ACCEPTED)
