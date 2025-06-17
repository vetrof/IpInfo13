# -*- coding: utf-8 -*-
import redis

redis_config = redis.Redis('localhost', port=6379, db=0, decode_responses=True)
print(redis_config.ping())

with open("parser_links.txt", "r") as file:
    link_load = file.read()
    print(type(link_load))
    links = link_load
    print(links)
    counter_symbols = links.count("a")
    print(f"Количеств букв 'а' в строках: {counter_symbols}")
for i in range(counter_symbols):
    answer = redis_config.set(i, counter_symbols)
    print(i, answer)



