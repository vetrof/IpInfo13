import requests


def get():
    count = 0
    url = "https://pikabu.ru/"
    response = requests.get(url)
    txt_resresponse = response.text.split("\n")
    for i in txt_resresponse:
        count += 1
        print(i)
    return count


count_a = get()
print(count_a)

#Доделать предыдущие задание по этому же принципу, посчитать сколько букв "а" в переходе по ссылке, убрать все пробелы+
#Дополнить сколько строк в переходе по ссылке и сделать сохранение в текстовый файл
#Нужно будет сделать принт всех ссылок с которые перечислены с запрашиваемой странице

