# -*- coding: utf-8 -*-
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from app_history.models import History
from rest_framework.views import APIView
from app_history.serializer import HistorySerializer
from app_history.service import history_servise


class HistoryList(APIView):
    def get(self, request):
        if request.method == 'GET':
            history_list = History.objects.all()
            serializer = HistorySerializer(history_list, many=True)
            return JsonResponse(serializer.data, safe=False)
        # return Response(hundred_history)
    # +Использовать сериализатор для этого класса
    # +Обработка ошибок Qwery параметров, если присылается другой тип данных
    # Переминовать названия классов и перевести это все во view


class OneStringHistoryDelete(APIView):
    def delete(self, request, id=None):
        history_list = History.objects.get(id=id)
        history_list.delete()
        context = {"message": "Запись удалена!", "id": id}
        return Response(context, status=status.HTTP_202_ACCEPTED)


class AllHistoryDelete(APIView):
    def delete(self, request):
        full_history = History.objects.all()
        full_history.delete()
        context = "Все записи удалены!"
        return Response(context, status=status.HTTP_202_ACCEPTED)


class HistoryListClear(APIView):
    def get(self, request):
        if request.method == "GET":
            history_list = history_servise()
            serializer = HistorySerializer(history_list, many=True)
            return JsonResponse(serializer.data, safe=False)
