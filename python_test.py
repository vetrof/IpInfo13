# -*- coding: utf-8 -*-
import threading
import psycopg2
from http.server import BaseHTTPRequestHandler, HTTPServer
from rest_framework.utils import json


def get_data():
    conn = psycopg2.connect(
        "dbname=postgr_database user=postgr_user password=Asdf12345 host=localhost port=5432")
    cur = conn.cursor()
    cur.execute("select * from app_history_history")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    print(rows)
    return rows


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("do_GET")
        print(self.path)
        if self.path == "/data/":
            print("/data")
            data = get_data()
            json_data = json.dumps(data).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(json_data)))
            self.end_headers()
            self.wfile.write(json_data)
            print(json_data)
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/data/":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode('utf-8'))
            print(data)
        else:
            self.send_response(404)
            self.end_headers()


def run_server():
    port = 8003
    server_address = ('localhost', port)
    httpd = HTTPServer(server_address, Handler)
    print(f"Starting server on port {port}")

    try:
        httpd.serve_forever()
        print(f"Starting server on port {port}")
    except KeyboardInterrupt:
        httpd.server_close()
        print("Server stopped")


if __name__ == "__main__":
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()

input("Press Enter to stop the server...\n")

#Дорабатать код, чтобы база данных работала как нужно, исправить все ошибки
#Нужно написать 2 python скрипта без докера отдельно
#Одна программа будет принимать через терминал и отправляет эту задачу в редис на суммирование - это задача для того вот исполнителя
#Нужно написать консьюмер (воркер), которая смотрит в редис и когда она увидит предыдушую задачу и распечатает сумму в терминал
#Почитать про редис, кафка и раббитNQ
