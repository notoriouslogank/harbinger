import configparser
import socket

from requests import get

path = "docs/examples/"
python_config_file = "config.ini"
shell_config_file = "start.config"


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
    config["Bot"] = {"token": "", "channel": ""}

    config["Custom Color"] = {"r": "", "g": "", "b": ""}

    config["Server"] = {
        "server_dir": "/path/to/server",
        "startup_script": "/path/to/startup/script",
        "server_local_ip": f"{get_local_ip()}",
        "server_public_ip": f"{get_public_ip()}",
    }

    with open(path + python_config_file, "w") as configfile:
        config.write(configfile)

    file = path + python_config_file
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


write_sh_config(write_py_config(), path + shell_config_file)
