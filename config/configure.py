import base64
import configparser
import socket

from read_configs import ReadConfigs as configs
from requests import get


class Configure:
    """Class containing methods to create config.ini and start.conf."""

    config_path = "config/"
    python_config_file = "config.ini"
    shell_config_file = "start.conf"

    def obscure(data) -> bytes:
        """Take user input and return base64-encoded string.

        Args:
            data (str): Data to encode as base64

        Returns:
            bytes: Base64-encoded data
        """
        data_bytes = data.encode("ascii")
        base64_data_bytes = base64.b64encode(data_bytes)
        base64_data = base64_data_bytes.decode("ascii")
        return base64_data

    def get_token() -> str:
        """Prompt user for API token.

        Returns:
            str: Discord API token
        """
        token = input("Discord API Token: ")
        return token
    
    def get_owner_id() -> str:
        owner_id = input("Owner ID")
        return owner_id

    #def get_channel_id() -> int:
    #    """Prompt user for Channel ID.
    #
    #    Returns:
    #        int: Channel ID
    #    """
    #    channel = input("Channel ID: ")
    #    return channel

    def get_server_dir() -> str:
        """Prompt user for directory to Minecraft server.

        Returns:
            str: Path to Minecraft server
        """
        server_dir = input("Directory of server: ")
        return server_dir

    def get_startup_script() -> str:
        """Prompt user for path to Minecraft server startup script.

        Returns:
            str: Path to Minecraft server startup script
        """
        startup_script = input("Path to startup script: ")
        return startup_script

    def get_custom_color() -> str:
        """Prompt user for custom color as RGB values.

        Returns:
            str: R G B value(s)
        """
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

    def get_email():
        email_address = input("Email address: ")
        return email_address

    def get_email_pass():
        email_pass = input("Password: ")
        return email_pass

    def get_moderator_role():
        role_id = str(input("Administrator Role Name: ") or "Admin")
        return role_id

    def get_developer_role():
        role_id = str(input("Developer Role ID: ") or "Developer")
        return role_id

    def get_deletion_time():
        delete_after = input("Time until messages auto-delete (seconds): ")
        return delete_after

    def write_py_config() -> None:
        """Create config.ini."""
        config = configparser.ConfigParser()
        config["Email"] = {
            "address": f"{Configure.obscure(Configure.get_email())}",
            "password": f"{Configure.obscure(Configure.get_email_pass())}",
        }
        config["Bot"] = {
            "token": f"{Configure.obscure(Configure.get_token())}",
        #    "channel": f"{Configure.obscure(Configure.get_channel_id())}",
            "delete_after": f"{Configure.get_deletion_time()}",
            "owner_id": f'{Configure.obscure(Configure.get_owner_id())}'
        }
        config["Custom Color"] = {"rgb": f"{Configure.get_custom_color()}"}
        config["Server"] = {
            "server_dir": f"{Configure.obscure(Configure.get_server_dir())}",
            "startup_script": f"{Configure.obscure(Configure.get_startup_script())}",
            "server_local_ip": f"{Configure.obscure(Configure.get_local_ip())}",
            "server_public_ip": f"{Configure.obscure(Configure.get_public_ip())}",
        }
        config["Roles"] = {
            "moderator": f"{Configure.obscure(Configure.get_moderator_role())}",
            "developer": f"{Configure.obscure(Configure.get_developer_role())}",
        }

        with open(f"{Configure.python_config_file}", "w") as configfile:
            config.write(configfile)

    def write_sh_config(configfile) -> None:
        """Create start.conf configuration file.

        Args:
            configfile (str): Path to config.ini
        """
        server_dir = configs.server_dir()
        startup_script = configs.startup_script()
        text = f"#!/bin/bash\nServerDir={server_dir}\nStartupScript={startup_script}\n"

        with open(f"{Configure.config_path}{Configure.shell_config_file}", "w") as conf:
            conf.write(text)


Configure.write_py_config()
