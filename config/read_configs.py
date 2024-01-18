from configparser import ConfigParser
from cryptography.fernet import Fernet
import discord
from config.configure import Configure


python_config_file = "config/config.ini"
keyfile = "config/key.key"
shell_config_file = "config/start.conf"

config = ConfigParser()


class ReadConfigs:
    def load_key():
        """Load the Fernet key from keyfile."""
        return open("config/key.key", "rb").read()

    def decrypt(filename, key):
        """Decrypt config.ini."""
        f = Fernet(key)
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(filename, "wb") as file:
            file.write(decrypted_data)
        return

    def discord_token():
        """Read config file and return api_token."""
        ReadConfigs.decrypt(python_config_file, ReadConfigs.load_key())  # decrypt
        config.read(python_config_file)  # read
        api_token = config["Bot"]["discord_token"]  # find entry
        Configure.encrypt(python_config_file, Configure.load_key())  # encrypt
        return api_token

    # def channel() -> int:
    #    main_channel = int(ReadConfigs.reveal(config["Bot"]["channel"]))
    #    return main_channel

    def owner_id():
        ReadConfigs.decrypt(python_config_file, ReadConfigs.load_key())  # decrypt
        config.read(python_config_file)  # read
        owner_id = int(config["Bot"]["owner_id"])
        Configure.encrypt(python_config_file, Configure.load_key())  # encrypt
        return owner_id

    def email_address():
        ReadConfigs.decrypt(python_config_file, ReadConfigs.load_key())  # decrypt
        config.read(python_config_file)  # read
        email_addr = config["Email"]["address"]
        Configure.encrypt(python_config_file, Configure.load_key())  # encrypt
        return email_addr

    def email_password():
        ReadConfigs.decrypt(python_config_file, ReadConfigs.load_key())  # decrypt
        config.read(python_config_file)  # read
        email_pass = config["Email"]["password"]
        Configure.encrypt(python_config_file, Configure.load_key())  # encrypt
        return email_pass

    def server_dir():
        ReadConfigs.decrypt(python_config_file, ReadConfigs.load_key())  # decrypt
        config.read(python_config_file)  # read
        server_directory = config["Server"]["server_dir"]
        Configure.encrypt(python_config_file, Configure.load_key())  # encrypt
        return server_directory

    def startup_script():
        ReadConfigs.decrypt(python_config_file, ReadConfigs.load_key())  # decrypt
        config.read(python_config_file)  # read
        start_script = config["Server"]["startup_script"]
        Configure.encrypt(python_config_file, Configure.load_key())  # encrypt
        return start_script

    def server_public_ip():
        ReadConfigs.decrypt(python_config_file, ReadConfigs.load_key())  # decrypt
        config.read(python_config_file)  # read
        public_ip = config["Server"]["server_public_ip"]
        Configure.encrypt(python_config_file, Configure.load_key())  # encrypt
        return public_ip

    def server_local_ip():
        ReadConfigs.decrypt(python_config_file, ReadConfigs.load_key())  # decrypt
        config.read(python_config_file)  # read
        local_ip = config["Server"]["server_local_ip"]
        Configure.encrypt(python_config_file, Configure.load_key())  # encrypt
        return local_ip

    def moderator_id():
        ReadConfigs.decrypt(python_config_file, ReadConfigs.load_key())  # decrypt
        config.read(python_config_file)  # read
        moderator_role_id = int(config["Roles"]["moderator"])
        Configure.encrypt(python_config_file, Configure.load_key())  # encrypt
        return moderator_role_id

    def developer_id():
        ReadConfigs.decrypt(python_config_file, ReadConfigs.load_key())  # decrypt
        config.read(python_config_file)  # read
        developer_role_id = int(config["Roles"]["developer"])
        Configure.encrypt(python_config_file, Configure.load_key())  # encrypt
        return developer_role_id

    def custom_color() -> discord.Color:
        rgb = config["Custom Color"]["rgb"]
        r, g, b = map(int, rgb.split())
        rgb_color = discord.Color.from_rgb(int(r), int(g), int(b))
        return rgb_color

    def delete_time():
        del_time = int(config["Bot"]["delete_after"])
        return del_time


def main():
    """Print deobfuscated config.ini."""
    config = ReadConfigs
    key = config.load_key()
    print(
        f"Email Address: {config.email_address()}\nEmail Password: {config.email_password()}\nDiscord Token: {config.discord_token()}\nDelete After: {config.delete_time()}\nOwner ID: {config.owner_id()}\nCustom Color: {config.custom_color()}\nServer Directory: {config.server_dir()}\nStartup Script: {config.startup_script()}\nLocal IP: {config.server_local_ip()}\nPublic IP: {config.server_public_ip()}\nModerator Role ID: {config.moderator_id()}\nDeveloper ID: {config.developer_id()}"
    )


if __name__ == "__main__":
    main()
