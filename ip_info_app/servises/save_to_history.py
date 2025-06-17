from app_history.models import History, Users


def save_history(json):
    ip = json["Наш IP"]["ip"]
    region = json["Наш IP"]["region"]
    new_object = History()
    new_object.ip = ip
    new_object.region = region
    new_object.save()


def save_users(json):
    login = json["Логин"]
    new_object = Users()
    new_object.login = login
    new_object.save()
