import configparser
from os import path
import socket

from requests import get


class Configure:
    config_path = "config/"
    python_config_file = "config.ini"
    shell_config_file = "start.conf"

    def get_token():
        token = input("Discord API Token: ")
        return token

    def get_channel_id():
        channel = input("Channel ID: ")
        return channel

    def get_server_dir():
        server_dir = input("Directory of server: ")
        return server_dir

    def get_startup_script():
        startup_script = input("Path to startup script: ")
        return startup_script

    def get_custom_color():
        rgb = input("RGB (000 000 000): ")
        return rgb

    def get_local_ip() -> str:
        """Fetch local IP address.

        Returns:
        str: Local IP address.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip

    def get_public_ip() -> str:
        """Query the Internet and return public IP.

        Returns:
            str: Public IP address
        """
        ip = get("https://api.ipify.org").content.decode("utf8")
        return ip

    def write_py_config() -> str:
        config = configparser.ConfigParser()
        config["Bot"] = {
            "token": f"{Configure.get_token()}",
            "channel": f"{Configure.get_channel_id()}",
        }
        config["Custom Color"] = {"rgb": f"{Configure.get_custom_color()}"}
        config["Server"] = {
            "server_dir": f"{Configure.get_server_dir()}",
            "startup_script": f"{Configure.get_startup_script()}",
            "server_local_ip": f"{Configure.get_local_ip()}",
            "server_public_ip": f"{Configure.get_public_ip()}",
        }

        with open(
            f"{Configure.config_path}{Configure.python_config_file}", "w"
        ) as configfile:
            config.write(configfile)

    def write_sh_config(configfile):
        config = configparser.ConfigParser()
        config.read(configfile)
        server_dir = config["Server"]["server_dir"]
        startup_script = config["Server"]["startup_script"]
        text = f"#!/bin/bash\nServerDir={server_dir}\nStartupScript={startup_script}\n"

        with open(f"{Configure.config_path}{Configure.shell_config_file}", "w") as conf:
            conf.write(text)


def main():
    Configure.write_py_config()
    Configure.write_sh_config(f"{Configure.config_path}{Configure.python_config_file}")


main()
