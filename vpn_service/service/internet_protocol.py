from vpn_service.config import IP_PROVIDERS, IP_ALIASES, IP_COUNTRY_ALIASES
from vpn_service.infrastructure.internet_protocol import get_public_ip_info


def public_ip_info():
    return get_public_ip_info(IP_PROVIDERS, IP_ALIASES, IP_COUNTRY_ALIASES)