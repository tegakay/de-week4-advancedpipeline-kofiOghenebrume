from typing import Dict
import pandas as pd
import numpy as np

class DataAnalyzer:
    def __init__(self, data:pd.DataFrame):
        self.data = data
    
    def analyze_data(self):
        analysis = {}
        raw = self.data.to_dict(orient='records')
        for record in raw:
            username = record['username']
            revenue = record['revenue']
            if username not in analysis:
                analysis[username] = {
                    'total_revenue': 0,
                    'product_count': 0,
                    'average_product_price': 0
                }
            analysis[username]['total_revenue'] += revenue
            analysis[username]['product_count'] += 1
            analysis[username]['average_product_price'] = round(analysis[username]['total_revenue'] / analysis[username]['product_count'], 2)
        
        return analysis