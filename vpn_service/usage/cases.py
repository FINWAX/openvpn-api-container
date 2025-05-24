import os
import time

from vpn_service.config import CONTAINER_OPENVPN_CONNECTION_CONFIG_DIR, REMOTE_CONFIG_FILENAME, \
    STARTAPP_OPENVPN_CONFIG_NAME, OPENVPN_CONNECTION_AWAITING_SECS
from vpn_service.service.container import container_connected_to_openvpn, current_connection_pid, \
    close_openvpn_connection, resolve_config_filepath, open_openvpn_connection, get_current_config_name, \
    remember_current_config_name
from vpn_service.service.internet_protocol import public_ip_info
from vpn_service.usage.data import ConnectionInfo


def provide_startapp_connection_to_openvpn():
    if STARTAPP_OPENVPN_CONFIG_NAME:
        return connect_to_openvpn(STARTAPP_OPENVPN_CONFIG_NAME)

    return False, None


def disconnect_from_openvpn():
    if not container_connected_to_openvpn():
        return True, None

    pid = current_connection_pid()

    closed = close_openvpn_connection(pid)
    error = None if closed else 'Failed to close openvpn connection.'

    return closed, error


def connect_to_openvpn(config_name):
    config_path = resolve_config_filepath(
        CONTAINER_OPENVPN_CONNECTION_CONFIG_DIR,
        config_name,
        REMOTE_CONFIG_FILENAME
    )

    if not os.path.exists(config_path):
        return False, f"Config file {config_path} does not exist."

    if container_connected_to_openvpn():
        current_config_name = get_current_config_name()

        if current_config_name == config_name:
            return True, None

        disconnect_from_openvpn()

    open_openvpn_connection(config_path)
    time.sleep(OPENVPN_CONNECTION_AWAITING_SECS)

    if container_connected_to_openvpn():
        remember_current_config_name(config_name)
        return True, None

    return False, 'Failed to start openvpn connection.'


def connection_info() -> tuple[ConnectionInfo | None, str | None]:
    info = ConnectionInfo()

    info.ip, info.country = public_ip_info()

    info.connected = container_connected_to_openvpn()
    info.config_name = get_current_config_name()

    return info, None
