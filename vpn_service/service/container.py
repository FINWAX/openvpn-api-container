import os
import signal
import subprocess
import time
from os.path import join

import psutil
import requests

from vpn_service.config import OPENVPN_PID_FILE, CURRENT_CONNECTION_CONFIG_NAME_FILE, OPENVPN_DISCONNECT_AWAITING_SECS, \
    IGNORED_OPENVPN_OPTIONS
from vpn_service.infrastructure.openvpn import make_openvpn_connection_command


def close_openvpn_connection(pid):
    os.kill(pid, signal.SIGTERM)
    for _ in range(OPENVPN_DISCONNECT_AWAITING_SECS):
        if not psutil.pid_exists(pid):
            remove_openvpn_pid_file()
            forget_container_config_name()
            return True
        time.sleep(1)

    os.kill(pid, signal.SIGKILL)
    remove_openvpn_pid_file()
    forget_container_config_name()

    return psutil.pid_exists(pid)


def remove_openvpn_pid_file():
    if os.path.exists(OPENVPN_PID_FILE):
        os.remove(OPENVPN_PID_FILE)


def resolve_config_filepath(configs_dir, config_filename, remote_filename):
    if config_filename.startswith(('http://', 'https://')):
        response = requests.get(config_filename)
        config_path = join(configs_dir, remote_filename)
        with open(config_path, 'wb') as f:
            f.write(response.content)

        return config_path

    return join(configs_dir, config_filename)


def current_connection_pid():
    with open(OPENVPN_PID_FILE, 'r') as f:
        return int(f.read().strip())


def open_openvpn_connection(config_filepath):
    cmd = make_openvpn_connection_command(config_filepath, OPENVPN_PID_FILE, IGNORED_OPENVPN_OPTIONS, as_one_line=False)

    subprocess.Popen(cmd)


def container_connected_to_openvpn():
    if not os.path.exists(OPENVPN_PID_FILE):
        return False

    pid = current_connection_pid()

    return psutil.pid_exists(pid)


def forget_container_config_name():
    if os.path.exists(CURRENT_CONNECTION_CONFIG_NAME_FILE):
        os.remove(CURRENT_CONNECTION_CONFIG_NAME_FILE)


def remember_current_config_name(config_name):
    with open(CURRENT_CONNECTION_CONFIG_NAME_FILE, 'w') as f:
        f.write(config_name)


def get_current_config_name():
    if os.path.exists(CURRENT_CONNECTION_CONFIG_NAME_FILE):
        with open(CURRENT_CONNECTION_CONFIG_NAME_FILE, 'r') as f:
            return f.read().strip()

    return None
