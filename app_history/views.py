from app_history.models import Users
from django.shortcuts import render

sam = Users.objects.create(name="Sam")

account = Users.login.objects.create(login="1234", password="6565", user=sam)
account.user.save()
print(f"{account.user.name}, login: {account.login}, password: {account.password}")

