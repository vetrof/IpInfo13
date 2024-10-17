from django.conf import settings
import ipinfo


def api_info_handler(ip_address):
    access_token = settings.TOKEN_API_INFO
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails(ip_address)
    info = {"Наш IP": details.all}
    return info
