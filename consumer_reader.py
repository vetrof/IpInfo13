import redis

redis_config = redis.Redis('localhost', port=6379, db=0, decode_responses=True)
print(redis_config.ping())

with open("links.txt", "r") as file:
    link_load = file.read()
    links = link_load.split("\n")
for link in links:
    answer = redis_config.get(link)
    print(link, answer)

#Cделать парсер - также ссылки сразу должны сохраняться в редис, потом подключается консьюмер-парсер, который сохрянет ссылку и значение (None
#Далее программа берет эти ссылки и считает сколько букв "А" во всем ответе и обновляет данные в редис, а именно количество букв "А"
#Сделать 3 файл, который делает принт всех ссылок из редис
#Прописать удаление, и таймаут в конце программы
#Консюмер который берет задачу не в ручную, а автоматически
