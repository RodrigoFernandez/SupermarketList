import configparser

def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

config = get_config()