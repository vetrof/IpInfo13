# -*- coding: utf-8 -*-
import redis
import requests

redis_config = redis.Redis('localhost', port=6379, db=0, decode_responses=True)
print(redis_config.ping())

with open("links.txt", "r") as file:
    link_load = file.read()
    print(type(link_load))
    links = link_load.split("\n")
for link in links:
    try:
        response = requests.get(link, timeout=5)
        print(link, response)
        redis_config.set(link, response.status_code)
    except Exception as err:
        print("Возникло исключение", err)

