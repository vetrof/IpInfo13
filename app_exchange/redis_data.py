import redis
from django.http import HttpResponse
from tasks import get_exchange

r = redis.StrictRedis(host="127.0.0.1", port=6379, db=1)

if HttpResponse(status=200):
    print(get_exchange())
elif HttpResponse(status=401):
    print("Данных нет")
else:
    pass
