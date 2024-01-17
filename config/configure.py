import configparser
import socket
from calendar import c

from cryptography.fernet import Fernet
from requests import get


class Configure:
    """Class containing methods to create config.ini and start.conf."""

    config_path = "config/"
    python_config_file = "config.ini"
    shell_config_file = "start.conf"

    def load_key():
        return open("config/key.key", "rb").read()

    def encrypt(filename, key):
        f = Fernet(key)

        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)

        with open(filename, "wb") as file:
            file.write(encrypted_data)
        return

    def get_token():
        """Prompt user for API token.

        Returns:
            str: Discord API token
        """
        api_token = input("Discord API Token: ")
        api_token_bytes = api_token
        return api_token_bytes

    def get_owner_id():
        owner_id = input("Owner ID: ")
        owner_id_bytes = owner_id
        return owner_id_bytes

    # def get_channel_id() -> int:
    #    """Prompt user for Channel ID.
    #
    #    Returns:
    #        int: Channel ID
    #    """
    #    channel = input("Channel ID: ")
    #    return channel

    def get_server_dir():
        """Prompt user for directory to Minecraft server.

        Returns:
            str: Path to Minecraft server
        """
        server_dir = input("Directory of server: ")
        server_dir_bytes = server_dir
        return server_dir_bytes

    def get_startup_script():
        """Prompt user for path to Minecraft server startup script.

        Returns:
            str: Path to Minecraft server startup script
        """
        startup_script = input("Path to startup script: ")
        startup_script_bytes = startup_script
        return startup_script_bytes

    def get_custom_color():
        """Prompt user for custom color as RGB values.

        Returns:
            str: R G B value(s)
        """
        rgb = input("RGB (000 000 000): ")
        return rgb

    def get_local_ip():
        """Fetch local IP address.

        Returns:
        str: Local IP address.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        ip_str = str(ip)
        ip_bytes = ip_str
        return ip_bytes

    def get_public_ip() -> str:
        """Query the Internet and return public IP.

        Returns:
            str: Public IP address
        """
        ip = get("https://api.ipify.org").content.decode("utf8")
        ip_str = str(ip)
        ip_bytes = ip_str
        return ip_bytes

    def get_email():
        email_address = input("Email address: ")
        email_address_bytes = email_address
        return email_address_bytes

    def get_email_pass():
        email_pass = input("Password: ")
        email_pass_bytes = email_pass
        return email_pass_bytes

    def get_moderator_role():
        role_id = str(input("Administrator Role ID: ") or "Admin")
        role_id_bytes = role_id
        return role_id_bytes

    def get_developer_role():
        role_id = str(input("Developer Role ID: ") or "Developer")
        role_id_bytes = role_id
        return role_id_bytes

    def get_deletion_time():
        delete_after = input("Time until messages auto-delete (seconds): ")
        return delete_after

    def write_keyfile():
        key = Fernet.generate_key()
        with open("config/key.key", "wb") as key_file:
            key_file.write(key)

    def write_py_config() -> None:
        """Create config.ini."""
        config = configparser.ConfigParser()
        config["Email"] = {
            "address": f"{(Configure.get_email())}",
            "password": f"{(Configure.get_email_pass())}",
        }
        config["Bot"] = {
            "discord_token": f"{(Configure.get_token())}",
            #    "channel": f"{(Configure.get_channel_id())}",
            "delete_after": f"{Configure.get_deletion_time()}",
            "owner_id": f"{(Configure.get_owner_id())}",
        }
        config["Custom Color"] = {"rgb": f"{Configure.get_custom_color()}"}
        config["Server"] = {
            "server_dir": f"{(Configure.get_server_dir())}",
            "startup_script": f"{(Configure.get_startup_script())}",
            "server_local_ip": f"{(Configure.get_local_ip())}",
            "server_public_ip": f"{(Configure.get_public_ip())}",
        }
        config["Roles"] = {
            "moderator": f"{(Configure.get_moderator_role())}",
            "developer": f"{(Configure.get_developer_role())}",
        }

        with open(f"{Configure.python_config_file}", "w") as configfile:
            config.write(configfile)

    # def write_sh_config(configfile) -> None:
    #     """Create start.conf configuration file.

    #     Args:
    #         configfile (str): Path to config.ini
    #     """
    #     server_dir = configs.server_dir()
    #     startup_script = configs.startup_script()
    #     text = f"#!/bin/bash\nServerDir={server_dir}\nStartupScript={startup_script}\n"

    #     with open(f"{Configure.config_path}{Configure.shell_config_file}", "w") as conf:
    #         conf.write(text)


def main():
    # Configure.write_keyfile()
    file = "config/config.ini"
    key = Configure.load_key()
    # Configure.write_py_config()
    Configure.encrypt(file, key)


if __name__ == "__main__":
    main()
