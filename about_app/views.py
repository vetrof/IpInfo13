from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class AboutMain(APIView):

    def get(self, request):
        response = {"Hello": "World"}
        return Response(response)
#сделать более развернутый ответ, и добавить текущее дату и время
#*авторизация по токену и приветствие пользователя