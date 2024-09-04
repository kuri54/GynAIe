import os
import numpy as np
import pandas as pd
import random
import seaborn as sns
from sklearn import preprocessing

class CalcAnomalyScore():
    def __init__(self, result_df, case_df, anomaly_label, min_image_count):
        self.update_result_df = result_df.copy()
        self.update_case_df = case_df.copy()
        self.anomaly_label = anomaly_label
        self.min_image_count = min_image_count

    def update_df(self):
        # Filter cases with less than 50 images
        group_counts = self.update_result_df['case'].value_counts()
        filtered_group = group_counts[group_counts <= self.min_image_count].index.to_list()

        self.update_case_df['inadequate'] = 0
        self.update_case_df.loc[self.update_case_df['case'].isin(filtered_group), 'inadequate'] = 1

    def get_scores(self):
        grouped_data = self.update_result_df.groupby('case').agg({'pred_score': 'mean',
                                                                  'pred_label': lambda x: (x == self.anomaly_label).sum(),
                                                                  'path': 'count'
                                                                  }).reset_index()

        grouped_data.rename(columns={'pred_score': 'pred_score_mean',
                                     'pred_label': 'anomaly_score',
                                     'path': 'tile_image_num'
                                     }, inplace=True)

        return pd.merge(grouped_data, self.update_case_df, on='case', how='left')

    def run_calc(self):
        self.update_df()
        calculated_df = self.get_scores()

        return calculated_df
