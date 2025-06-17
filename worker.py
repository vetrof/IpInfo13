# -*- coding: utf-8 -*-
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

print(r.ping())

set_value1 = r.get("value1")
set_value2 = r.get("value2")

print(type(set_value1))

total = int(set_value1) + int(set_value2)
r.set("total", total)
print(total)
