import config
import configparser

class ConfigManager:
    def __init__(self, config_file='pipeline.cfg'):
        self.config_parser = configparser.ConfigParser()
        self.config_parser.read(config_file)

    def get_pipeline_name(self):
        return self.config_parser.get('pipeline', 'name')

    def get_load_base_url(self):
        return self.config_parser.get('LOAD', 'base_url')

    def get_load_limit(self):
        return self.config_parser.getint('LOAD', 'limit')

