import os

API_PORT = 5000

OPENVPN_PID_FILE = '/tmp/openvpn.pid'

CONTAINER_OPENVPN_CONNECTION_CONFIG_DIR = '/app/configs'
REMOTE_CONFIG_FILENAME = 'REMOTE.ovpn'

CURRENT_CONNECTION_CONFIG_NAME_FILE = '/tmp/current_vpn_config'

STARTAPP_OPENVPN_CONFIG_NAME = os.getenv('STARTAPP_OPENVPN_CONFIG_NAME', '').strip()

OPENVPN_DISCONNECT_AWAITING_SECS = 10
OPENVPN_CONNECTION_AWAITING_SECS = 3

IGNORED_OPENVPN_OPTIONS = [
    'block-outside-dns',
    'register-dns',
    'windows-driver',
    'tap-sleep',
    'show-net-up',
    'dhcp-renew',
    'dhcp-release'
]

IP_PROVIDERS = [
    'https://ipwho.is/',
    'https://api.ipify.org/?format=json',
    'https://jsonip.com/',
    'https://ipv4-check-perf.radar.cloudflare.com/api/info',
    'https://us1.api-bdc.net/data/client-ip',
    'https://api.myip.com/',
    'https://api.seeip.org/jsonip?'
]
IP_ALIASES = ['ip', 'ipString']
IP_COUNTRY_ALIASES = ['country']
