# -*- coding: utf-8 -*-
import psycopg2
from http.server import BaseHTTPRequestHandler, HTTPServer


def get_data():
    conn = psycopg2.connect(
        "dbname=postgr_database user=postgr_user password=Asdf12345 host=db port=5432 client_encoding=UTF8 errors=ignore")
    cur = conn.cursor()
    cur.execute("select * from app_history_history")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    print(rows)
    return rows


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data":
            data = get_data()
            data_json = data.json()
            print(data_json)

    def do_POST(self):
        if self.path == "/data":
            data = get_data()
            data_json = data.json()
            print(data_json)


            # Разобрать с ошибкой UnicodeDecodeError: 'utf-8' codec can't decode byte 0xdd in position 47: invalid continuation byte
            # нужно вернуть все данные из get_data ввиде json
            # реализовать метод POST на этой функции
            # +нужно будет написать сервер который запустит код сам
            # Почитать книгу Чистая архитектура и переписать код как я пойму из этой книге


if __name__ == "__main__":
    port = 8001
    server_address = ('', port)
    httpd = HTTPServer(server_address, Handler)
    print(f"Starting server on port {port}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Server stopped")
