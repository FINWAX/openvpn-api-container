from random import shuffle

import requests


def get_public_ip_info(ip_providers, ip_aliases, ip_country_aliases):
    providers = list(ip_providers)
    shuffle(providers)
    country = None
    ip = None
    for provider in providers:
        try:
            response = requests.get(provider)
            data = response.json()
            for ip_alias in ip_aliases:
                ip = data.get(ip_alias, ip or None)
                if ip is not None:
                    break

            for country_alias in ip_country_aliases:
                country = data.get(country_alias, country or None)
                if country is not None:
                    break

        except:
            continue

        if ip is not None and country is not None:
            break

    return ip, country
