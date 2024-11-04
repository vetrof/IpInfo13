from app_history.models import History


def save_history(json):
    ip = json["Наш IP"]["ip"]
    region = json["Наш IP"]["region"]
    new_object = History()
    new_object.ip = ip
    new_object.region = region
    new_object.save()

