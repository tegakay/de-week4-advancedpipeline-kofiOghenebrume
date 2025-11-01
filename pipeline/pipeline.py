import  os
from typing import List, Dict, Any, Optional, Iterable
import logging
import config
import configparser
import json


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

output_path = os.path.join(os.path.dirname(__file__), "..", "seller_performance_report.json")
output_path = os.path.abspath(output_path)


from pipeline.api_client import APIClient
from pipeline.data_enricher import DataEnricher
from pipeline.data_analyzer import DataAnalyzer


# from api_client import APIClient
# from data_enricher import DataEnricher
# from data_analyzer import DataAnalyzer


class OMNICartETL(config):

    def __init__(self,config):
        self.config = config
        

    def run(self) -> Dict[str, Any]:
        
        logger.info("Starting OMNICartETL run")

        config_parser = configparser.ConfigParser()
        config_parser.read(self.config)

        pipeline_name = config_parser.get('pipeline', 'name')
        base_url = config_parser.get('LOAD', 'base_url')
        limit = config_parser.getint('LOAD', 'limit')

        api_client = APIClient(base_url)
        products = api_client.get_all_products(start=0, limit=limit)
        users = api_client.get_all_users()

        data_enricher = DataEnricher(products=products, users=users)
        enriched_data = data_enricher.enrich_data()

        data_analyzer = DataAnalyzer(data=enriched_data)
        analysis_results = data_analyzer.analyze_data()

        if analysis_results:
            with open(output_path, 'w', newline="", encoding="utf-8") as f:
                json.dump(analysis_results, f,)
            logger.info(f"Analysis results written to {output_path}")
        
        logger.info("OMNICartETL run completed")

if __name__ == "__main__":
    pipeline = OMNICartETL()
    pipeline.run()