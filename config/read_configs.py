import base64
from configparser import ConfigParser

import discord

configfile = "config/config.ini"
config = ConfigParser()
config.read(configfile)


class ReadConfigs:
    def reveal(obfuscated) -> str:
        obfuscated_as_bytes = obfuscated.encode("ascii")
        clear_as_bytes = base64.b64decode(obfuscated_as_bytes)
        cleartext = clear_as_bytes.decode("ascii")
        return cleartext

    def token() -> str:
        api_token = ReadConfigs.reveal(config["Bot"]["token"])
        return api_token

    #def channel() -> int:
    #    main_channel = int(ReadConfigs.reveal(config["Bot"]["channel"]))
    #    return main_channel

    def owner_id() -> int:
        owner_id = int(ReadConfigs.reveal(config["Bot"]["owner_id"]))
        return owner_id
    
    def email_address() -> str:
        email_addr = ReadConfigs.reveal(config["Email"]["address"])
        return email_addr

    def email_password() -> str:
        email_pass = ReadConfigs.reveal(config["Email"]["password"])
        return email_pass

    def server_dir() -> str:
        server_directory = ReadConfigs.reveal(config["Server"]["server_dir"])
        return server_directory

    def startup_script() -> str:
        start_script = ReadConfigs.reveal(config["Server"]["startup_script"])
        return start_script

    def server_public_ip() -> str:
        public_ip = ReadConfigs.reveal(config["Server"]["server_public_ip"])
        return public_ip

    def server_local_ip() -> str:
        local_ip = ReadConfigs.reveal(config["Server"]["server_local_ip"])
        return local_ip

    def moderator_id() -> str:
        moderator_role_id = str(ReadConfigs.reveal(config["Roles"]["moderator"]))
        return moderator_role_id

    def developer_id() -> str:
        developer_role_id = str(ReadConfigs.reveal(config["Roles"]["developer"]))
        return developer_role_id

    def custom_color() -> discord.Color:
        rgb = config["Custom Color"]["rgb"]
        r, g, b = map(int, rgb.split())
        rgb_color = discord.Color.from_rgb(int(r), int(g), int(b))
        return rgb_color

    def delete_time() -> int:
        del_time = int(config["Bot"]["delete_after"])
        return del_time

def main():
    """Print deobfuscated config.ini."""
    read = ReadConfigs
    print(f"Token: {read.token()}\nOwner ID: {read.owner_id()}\nEmail Address: {read.email_address()}\nEmail Password: {read.email_password()}")
    print(f"Moderator ID: {read.moderator_id()}\nDeveloper ID: {read.developer_id()}\nServer Directory: {read.server_dir()}")
    print(f"Startup Script: {read.startup_script()}\nServer Local IP: {read.server_local_ip()}\nServer Public IP: {read.server_public_ip()}")
    print(f"Custom Color: {read.custom_color()}\nDelete Time: {read.delete_time()}")

if __name__ == "__main__":
    main()