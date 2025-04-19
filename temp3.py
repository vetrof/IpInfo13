# -*- coding: utf-8 -*-
data = '9/5gajgqnj.jpg"><linkrel="canonical"href="https://pikabu.ru/"><!--5e70yo7ib1jivlw5--><metaproperty="fb:admins"content="100000072189793"><metaproperty="fb:app_id"content="586543721489673"><linkrel="search"title="Пикабу"type="appl'
clear_link = ''
index = 0
for i in data:
    if i == 'h' and data[index + 1] == 't' and data[index + 2] == 't':
        print('match', i, data[index + 1], data[index + 2])
    index += 1


#Поставить сваггер на проект IpInfo13
#Проверить регистрацию JWT
#Проверить работают ли IP-адреса при вводе и по умолчанию (мой IP-адресс)
#Проверить END-point который выдает все адреса, которые запрашивали только МЫ (не чужие)
#Нужен end-point, который возвращает города, куда мы отправляли запрос
#Сделать фронд-энд к данному проекту