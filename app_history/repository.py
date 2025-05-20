# -*- coding: utf-8 -*-
from app_history.models import History


class HistoryRepo:
    @staticmethod
    def all_history():
        history_list = History.objects.all()
        return history_list

    #@staticmethod
    #def user_history(user_id):
    #    history_list = History.objects.filter(user=user_id)

#Сделать эндпоинт historyclear_user по нему нужно получать историю конкретного юзера, передавать id-юзера
#Приписать к истории History конктретного юзера
#Сделать вью в service, сделать в репозитории History вывод всего

