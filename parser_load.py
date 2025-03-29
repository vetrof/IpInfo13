import redis

redis_config = redis.Redis('localhost', port=6379, db=0, socket_connect_timeout=5, socket_timeout=10, decode_responses=True)
print(redis_config.ping())

with open("parser_links.txt", "r") as file:
    link_load = file.read()
    links = link_load.split()
for link in links:
    answer = redis_config.get(link)
    print(link, answer)
    redis_config.flushdb()
    redis_config.close()
