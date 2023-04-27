import configparser
import os

def read_config(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    config_data = dict(config['Fission'])
    os.environ['FISSION_URL'] = config_data['url']

