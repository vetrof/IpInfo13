from django.urls import path

from app_history.delete_endpoint_app import CountDelete, IpAdressDelete, FullHistoryDelete

urlpatterns = [
    path("?p=100/", CountDelete.as_view()),
    path("ip/", IpAdressDelete.as_view()),
    path("all/", FullHistoryDelete.as_view()),

]
