from django.urls import path
from ip_info_app.views import ipinfo

urlpatterns = [
    #Группа Web
    path("", ipinfo),
]

