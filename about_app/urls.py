from django.urls import path
from about_app.views import AboutMain

urlpatterns = [
    path("", AboutMain.as_view())
]