import requests
import bs4


def get():
    count = 0
    lines = 0
    url = "https://pikabu.ru/"
    response = requests.get(url)
    txt_response = "".join(response.text.split())
    print(response)
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a")
    for link in links:
        print(link.get('href'))
    for i in txt_response:
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
