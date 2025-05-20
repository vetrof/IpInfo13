# -*- coding: utf-8 -*-
from rest_framework import serializers
from app_history.models import History


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ["id", "region"]

    def history_serialize(self, request):
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
        return history_list

    def validate_title(self, p):
        context = {"message": "Все работает!"}
        if not isinstance(p, str):
            raise serializers.ValidationError("Error type. Type don't support")
        return context

