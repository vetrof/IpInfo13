import requests
from celery import shared_task
from django.core.cache import cache


# Нужно сохранить в редис несколько пар по типу data_from_redis
# Нужно сделать, чтобы раз в минуту запускалось сохранение с помощью celery
# Написать эндпоинт, который будет брать данные из редиса и демонстрировать их, если данных нет, то вернуть статус 400, и вернуть сообщение от том что данных нет
def set_exchange():
    url = "https://www.cbr-xml-daily.ru/latest.js"
    response = requests.get(url)
    all_data = response.json()
    #usd = all_data["rates"]["USD"]
    #eur = all_data["rates"]["EUR"]
    #aud = all_data["rates"]["AUD"]
    #cache.set("exchange_usd", usd)
    #cache.set("exchange_eur", eur)
    #cache.set("exchange_aud", aud)
    #print(all_data["rates"]["USD"])
    #print(all_data["rates"]["EUR"])
    #print(all_data["rates"]["AUD"])


#@shared_task
#def save_celery(json):
#    result = json(set_exchange)
#    result.save()
#    print(result)


if __name__ == "__main__":
    set_exchange()
