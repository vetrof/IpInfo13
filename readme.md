localhost:8003/api/v1/ip_info/

POST /foreign_ip/
{
    "ip": "1.1.1.1"
}

{
    "Наш IP": {
        "ip": "1.1.1.1",
        "hostname": "one.one.one.one",
        "city": "Brisbane",
        "region": "Queensland",
        "country": "AU",
        "loc": "-27.4816,153.0175",
        "org": "AS13335 Cloudflare, Inc.",
        "postal": "4101",
        "timezone": "Australia/Brisbane",
        "anycast": true,
        "country_name": "Australia",
        "isEU": false,
        "country_flag_url": "https://cdn.ipinfo.io/static/images/countries-flags/AU.svg",
        "country_flag": {
            "emoji": "??",
            "unicode": "U+1F1E6 U+1F1FA"
        },
        "country_currency": {
            "code": "AUD",
            "symbol": "$"
        },
        "continent": {
            "code": "OC",
            "name": "Oceania"
        },
        "latitude": "-27.4816",
        "longitude": "153.0175"
    }
}


http://127.0.0.1:8003/api/token/

POST /token/

{
    "username": "admin",
    "password": "admin"

}

{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6NDg5ODkzODg4OCwiaWF0IjoxNzQ1MzM4ODg4LCJqdGkiOiI3YWQwMjkxZTYyNmQ0MDUwYWUxMDUxZGE2NTU1ZThmNyIsInVzZXJfaWQiOjF9.KcWSLqo5cIprWGOeVAyR8RhqqmE8mip9zAwcJ75-qd8",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1MzM5MTg4LCJpYXQiOjE3NDUzMzg4ODgsImp0aSI6ImE4ZTY5YWE2YzNjOTQxOGJhZTQ4NWZhY2UzZmIwY2Q5IiwidXNlcl9pZCI6MX0.S5iyBTMF2Q835vvOcANx8Og4bZiQbJ8nAUsoAiOH3ik"
}


TO DO
GET /history/?p=100

[
   {
    "ip": "1.1.1.1.",
    "country": "Country",
   },
   {
    "ip": "1.1.1.1.",
    "country": "Country",
   }
]

DELETE /history/id
OK=202
{
    "message": "Запись удалена!",
    "id": "id",
}

DELETE /history/all
OK=202
{
    "message": "Все записи удалены!",
}

#Дописать документацию по всем API и реализовать API history по документации


