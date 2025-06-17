# -*- coding: utf-8 -*-
import bs4
import redis
import requests

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

r.set("str", 1)
print(r.ping())

value1 = str(input("Введите ссылку: "))


def get():
    count = 0
    lines = 0
    url = value1
    response = requests.get(url)
    txt_resresponse = response.text
    print("".join(response.text.split()))
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a")
    for link in links:
        print(link.get('href'))
    for i in txt_resresponse:
        if i == "a" or i == "A":
            count += 1
        lines += 1
    return f'в ссылке {url} количество букв "а" и "А" - {count} и количество строк - {lines}'


count_a = get()
print(count_a)

if count_a:
    filename = input("Нажмите Enter")
    filename = filename if filename else "parser_links.txt"

    try:
        with open(filename, "a", encoding='utf-8') as file:
            file.write(count_a)
            file.write("\n")
        print(f"Данные {count_a} успешно сохранены в файл {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {str(e)}")
else:
    print("Ссылки не были введены.")
