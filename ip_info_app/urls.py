from django.urls import path
from ip_info_app.views import InfoMain, ForeingMain

urlpatterns = [
    path("self_ip/", InfoMain.as_view()),
    path("foreign_ip/", ForeingMain.as_view()),

]
