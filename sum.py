# -*- coding: utf-8 -*-
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


r.set("str", 1)
print(r.ping())

value1 = int(input("Введите первое число: "))
value2 = int(input("Введите второе число: "))
#r.set("value1", value1)
#r.set("value2", value2)
r.setex("value1", 20, value1)


