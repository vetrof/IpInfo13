# -*- coding: utf-8 -*-
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

r.set("str", 1)
print(r.ping())

value1 = str(input("Введите ссылку: "))

r.setex("value1", 20, value1)

if value1:
    filename = input("Нажмите Enter")
    filename = filename if filename else "links.txt"

    try:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(value1)
            file.write("\n")
        print(f"Ссылка {value1} успешно сохранена в файл {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {str(e)}")
else:
    print("Ссылки не были введены.")
