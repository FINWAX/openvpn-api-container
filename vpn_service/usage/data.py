from dataclasses import dataclass


@dataclass
class ConnectionInfo:
    ip: None | str = None
    country: None | str = None
    connected: None | str = None
    config_name: None | str = None