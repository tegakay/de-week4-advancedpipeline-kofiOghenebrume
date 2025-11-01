import config
import configparser

def main():
    # Load configuration
    config_parser = configparser.ConfigParser()
    config_parser.read('pipeline.cfg')
    
    pipeline_name = config_parser.get('pipeline', 'name')
    base_url = config_parser.get('LOAD', 'base_url')
    limit = config_parser.getint('LOAD', 'limit')
    
    print(f"Pipeline Name: {pipeline_name}")
    print(f"Base URL: {base_url}")
    print(f"Limit: {limit}")

main()