import configparser

config = configparser.ConfigParser()
config['Bot'] = {'token': '', 'channel': '', 'custom_color': ''}
config['Paths'] = {'server_dir': '', 'startup_script': ''}
config['Server'] = {'hostname': '', 'IP': ''}

with open("default_config.ini", 'w') as configfile:
    config.write(configfile)