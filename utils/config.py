import pathlib
import os
from configparser import ConfigParser

config_path = "config.ini"
config = ConfigParser()
config.read(config_path)


def check_server():
    server_path = config['Paths']['server_dir']
    server_script = config['Paths']['server_script']
    os.chdir(pathlib.Path(server_path)) # Move to dir with server.jar
    if os.path.exists(server_path+server_script):
        print('exists')
    else:
        print('does not appear to')

check_server()