# -*- coding: utf-8 -*-
from django.urls import path

from app_history.delete_endpoint_app import HistoryList, OneStringHistoryDelete, AllHistoryDelete, HistoryListClear

urlpatterns = [
    path("", HistoryList.as_view()),
    path("ip/", OneStringHistoryDelete.as_view()),
    path("all/", AllHistoryDelete.as_view()),
    path("clear/", HistoryListClear.as_view()),

]
