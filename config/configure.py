import configparser
import socket

from cryptography.fernet import Fernet
from requests import get

python_config_file = "config/config.ini"
keyfile = "config/key.key"
shell_config_file = "config/start.conf"


class Configure:
    """Class containing methods to create config.ini and start.conf."""

    def load_key():
        """Load Fernet key from keyfile."""
        return open(f"{keyfile}", "rb").read()

    def encrypt(filename, key):
        """Encrypt config.ini"""
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
        return api_token

    def get_owner_id():
        """Get owner ID for bot control."""
        owner_id = int(input("Owner ID: "))
        return owner_id

    def get_server_dir():
        """Prompt user for directory to Minecraft server.

        Returns:
            str: Path to Minecraft server
        """
        server_dir = input("Directory of server: ")
        return server_dir

    def get_startup_script():
        """Prompt user for path to Minecraft server startup script.

        Returns:
            str: Path to Minecraft server startup script
        """
        startup_script = input("Path to startup script: ")
        return startup_script

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
        return ip

    def get_public_ip() -> str:
        """Query the Internet and return public IP.

        Returns:
            str: Public IP address
        """
        ip = get("https://api.ipify.org").content.decode("utf8")
        ip = str(ip)
        return ip

    def get_email():
        """Get email address for bug reports."""
        email_address = input("Email address: ")
        return email_address

    def get_email_pass():
        """Email password to allow bug reports to send to email."""
        email_pass = input("Password: ")
        return email_pass

    def get_moderator_role():
        """Get Moderator Role ID."""
        role_id = input("Moderator Role ID: ") or "Admin"
        return role_id

    def get_developer_role():
        """Get Developer Role ID."""
        role_id = input("Developer Role ID: ") or "dev"
        return role_id

    def get_deletion_time():
        """Get time (in seconds) to wait before messages auto-delete."""
        delete_after = input("Time until messages auto-delete (seconds): ")
        return delete_after

    def write_keyfile():
        """Generate a secure key and write it to keyfile."""
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

        with open(f"{python_config_file}", "w") as configfile:
            config.write(configfile)


def main():
    # Configure.write_keyfile()
    key = Configure.load_key()
    Configure.write_py_config()
    Configure.encrypt(f"{python_config_file}", key)


if __name__ == "__main__":
    main()
