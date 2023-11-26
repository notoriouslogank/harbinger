import configparser
from os import path
import socket

from requests import get

class Configure():

    path = "config/"
    python_config_file = "config.ini"
    shell_config_file = "start.config"
        
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
        rgb = input("RGB: ")
        r,g,b = map(int, rgb.split())
        return r,g,b
    
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
        """Write the Python config.ini file

        Returns:
            str: Return the config.ini file
        """
        config = configparser.ConfigParser()
        config["Bot"] = {"token": f"{Configure.get_token()}", "channel": f"{Configure.get_channel_id()}"}

        config["Custom Color"] = {"r": f"{Configure.get_custom_color([0])}", "g": f"{Configure.get_custom_color([1])}", "b": f"{Configure.get_custom_color([2])}"}

        config["Server"] = {
            "server_dir": f"{Configure.get_server_dir()}",
            "startup_script": f"{Configure.get_startup_script()}",
            "server_local_ip": f"{Configure.get_local_ip()}",
            "server_public_ip": f"{Configure.get_public_ip()}",
        }

        with open(Configure.path + Configure.python_config_file, "w") as configfile:
            config.write(configfile)

        file = Configure.path + Configure.python_config_file
        return file


    def write_sh_config(infile: str, outfile: str):
        """Write the shell config file start.config

        Args:
            infile (str): The file being ingested to generate start.conf
            outfile (str): The name of the file to be generated, ie start.conf
        """
        config = configparser.ConfigParser()
        config.read(infile)
        server_dir = config["Server"]["server_dir"]
        startup_script = config["Server"]["startup_script"]
        header = "#!/bin/bash\n"
        line1 = f"ServerDir={server_dir}\n"
        line2 = f"StartupScript={startup_script}\n"

        with open(outfile, "w") as conf:
            conf.write(header + line1 + line2)

def main():
    Configure.write_py_config(Configure.write_py_config(), Configure.path + Configure.shell_config_file)

main()