from django.urls import path
from ip_info_app.views import InfoMain, ForeingMain, HistoryMain

urlpatterns = [
    path("self_ip/", InfoMain.as_view()),
    path("foreign_ip/", ForeingMain.as_view()),
    path("history_ip/", HistoryMain.as_view()),

]
