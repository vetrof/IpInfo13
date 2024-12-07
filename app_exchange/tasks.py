import requests
from celery import shared_task
from django.core.cache import cache


#Сделать миграции и создать суперюзера, сделать две записи в model, сделать dump базы данных
#Затем нужно остановить проект и удалить контейнеры и собрать их заново и убедится что все сохранено, затем снова удалить контейнеры и удалить postgres volume, затем заново все собрать
#docker exec -t ipinfo13-db-1 pg_dumpall -c -U postgr_user > dump.sql - команда дампа базы данных
#автоматизировать создание backup базы данных
#IPython - установить и изучить сюда в venv
def set_exchange():
    url = "https://www.cbr-xml-daily.ru/latest.js"
    response = requests.get(url)
    all_data = response.json()
    usd = all_data["rates"]["USD"]
    eur = all_data["rates"]["EUR"]
    aud = all_data["rates"]["AUD"]
    cache.set("exchange_usd", usd)
    cache.set("exchange_eur", eur)
    cache.set("exchange_aud", aud)
    print(cache.get("exchange_usd"))
    print(cache.get("exchange_eur"))
    print(cache.get("exchange_aud"))



@shared_task
def save_celery(json):
    result = json(set_exchange)
    result.save()
    print(result)


if __name__ == "__main__":
    set_exchange()
