from configparser import ConfigParser
from cryptography.fernet import Fernet
import discord
from configure import Configure


configfile = "config/config.ini"
config = ConfigParser()


class ReadConfigs:
    def load_key():
        return open("config/key.key", "rb").read()

    def decrypt(filename, key):
        f = Fernet(key)
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(filename, "wb") as file:
            file.write(decrypted_data)
        return

    def discord_token():
        ReadConfigs.decrypt(configfile, ReadConfigs.load_key())  # decrypt
        config.read(configfile)  # read
        api_token = config["Bot"]["discord_token"]  # find entry
        Configure.encrypt(configfile, Configure.load_key())  # encrypt
        return api_token

    # def channel() -> int:
    #    main_channel = int(ReadConfigs.reveal(config["Bot"]["channel"]))
    #    return main_channel

    def owner_id():
        ReadConfigs.decrypt(configfile, ReadConfigs.load_key())  # decrypt
        config.read(configfile)  # read
        owner_id = config["Bot"]["owner_id"]
        Configure.encrypt(configfile, Configure.load_key())  # encrypt
        return owner_id

    def email_address():
        ReadConfigs.decrypt(configfile, ReadConfigs.load_key())  # decrypt
        config.read(configfile)  # read
        email_addr = config["Email"]["address"]
        Configure.encrypt(configfile, Configure.load_key())  # encrypt
        return email_addr

    def email_password():
        ReadConfigs.decrypt(configfile, ReadConfigs.load_key())  # decrypt
        config.read(configfile)  # read
        email_pass = config["Email"]["password"]
        Configure.encrypt(configfile, Configure.load_key())  # encrypt
        return email_pass

    def server_dir():
        ReadConfigs.decrypt(configfile, ReadConfigs.load_key())  # decrypt
        config.read(configfile)  # read
        server_directory = config["Server"]["server_dir"]
        Configure.encrypt(configfile, Configure.load_key())  # encrypt
        return server_directory

    def startup_script():
        ReadConfigs.decrypt(configfile, ReadConfigs.load_key())  # decrypt
        config.read(configfile)  # read
        start_script = config["Server"]["startup_script"]
        Configure.encrypt(configfile, Configure.load_key())  # encrypt
        return start_script

    def server_public_ip():
        ReadConfigs.decrypt(configfile, ReadConfigs.load_key())  # decrypt
        config.read(configfile)  # read
        public_ip = config["Server"]["server_public_ip"]
        Configure.encrypt(configfile, Configure.load_key())  # encrypt
        return public_ip

    def server_local_ip():
        ReadConfigs.decrypt(configfile, ReadConfigs.load_key())  # decrypt
        config.read(configfile)  # read
        local_ip = config["Server"]["server_local_ip"]
        Configure.encrypt(configfile, Configure.load_key())  # encrypt
        return local_ip

    def moderator_id():
        ReadConfigs.decrypt(configfile, ReadConfigs.load_key())  # decrypt
        config.read(configfile)  # read
        moderator_role_id = str(config["Roles"]["moderator"])
        Configure.encrypt(configfile, Configure.load_key())  # encrypt
        return moderator_role_id

    def developer_id():
        ReadConfigs.decrypt(configfile, ReadConfigs.load_key())  # decrypt
        config.read(configfile)  # read
        developer_role_id = str(config["Roles"]["developer"])
        Configure.encrypt(configfile, Configure.load_key())  # encrypt
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
    c = ReadConfigs
    key = c.load_key()
    print(c.discord_token())
    print(c.email_address())
    print(c.email_password())
    print(c.moderator_id())
    print(c.owner_id())
    print(c.server_dir())
    print(c.server_local_ip())
    print(c.server_public_ip())
    print(c.startup_script())

    file = "config/config.ini"


#    key = ReadConfigs.load_key()
#    ReadConfigs.decrypt(file, key)

# read = ReadConfigs
# token = read.reveal(read.discord_token())
# print(token)
#
# print(ReadConfigs.reveal(ReadConfigs.discord_token()))
# print(
#        f"Token: {read.discord_token()}\nOwner ID: {read.owner_id()}\nEmail Address: {read.email_address()}\nEmail Password: {read.email_password()}"
#    )
#    print(
#        f"Moderator ID: {read.moderator_id()}\nDeveloper ID: {read.developer_id()}\nServer Directory: {read.server_dir()}"
#    )
#    print(
#        f"Startup Script: {read.startup_script()}\nServer Local IP: {read.server_local_ip()}\nServer Public IP: {read.server_public_ip()}"
#    )
#    print(f"Custom Color: {read.custom_color()}\nDelete Time: {read.delete_time()}")


if __name__ == "__main__":
    main()
