import configparser

config = configparser.ConfigParser()
config['Bot'] = {'token': 'token_value', 'channel': 'channel_value', 'custom_color': 0x88ae00}
config['Paths'] = {'server_dir': '/home/logank/logan_mc_server/try2/', 'startup_script': './java.sh'}
config['Server'] = {'hostname': 'logank@mimir', 'IP': '192.168.0.1'}

with open("config.ini", 'w') as configfile:
    config.write(configfile)