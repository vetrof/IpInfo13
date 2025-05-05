# -*- coding: utf-8 -*-
from requests import Response
from rest_framework import status
from app_history.models import History
from django.shortcuts import render
from rest_framework.views import APIView


class CountDelete(APIView):
    def get(self, request):
        hundred_history = History.objects.all()[0:100]
        return render(request, "index.html", {'hundred_history': hundred_history})


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
