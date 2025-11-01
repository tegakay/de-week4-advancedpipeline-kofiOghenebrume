from typing import Dict
import pandas as pd
import numpy as np
class DataEnricher:
    def __init__(self, products:Dict, users:Dict, ):
        self.products = products
        self.users = users
    
    def enrich_data(self):
        products_df = pd.DataFrame(self.products)
        users_df = pd.DataFrame(self.users)
        # enriched_df = products_df.merge(users_df, left_on='userId', right_on='id', how='left', suffixes=('_product', '_user'))
        enriched_df = pd.merge(products_df, users_df, on='id', how='inner', suffixes=('_product', '_user'))

        #extract rating into 2 columns for revenue
        df_rating = enriched_df["rating"].apply(pd.Series)
        enriched_df = pd.concat([enriched_df, df_rating], axis=1)

        # simplify table
        relevant_columns = ['id', 'name', 'username', 'email', 'price','description', 'category', 'rate', 'count']
        enriched_df = enriched_df[relevant_columns].copy()
        enriched_df['revenue'] = enriched_df['rate'] * enriched_df['count']

        return enriched_df

        

