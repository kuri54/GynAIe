import os
import pandas as pd
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from sklearn import preprocessing

class Vis():
    def __init__(self, calculated_df, sort_by, sort_ascending, result_dir, case_name):
        self.calculated_df = calculated_df
        self.sort_by = sort_by
        self.sort_ascending = sort_ascending
        self.result_dir = Path(result_dir)
        self.case_name = case_name

    def sort_df(self):
        sorted_df = self.calculated_df.sort_values(self.sort_by, ascending=self.sort_ascending).reset_index(drop=True).fillna(0)
        sorted_df['norm'] = preprocessing.minmax_scale(sorted_df.anomaly_score)

        return sorted_df

    def plot(self, sorted_df, x='norm', y='case'):
        fig = plt.figure(figsize=(15, 10), dpi=300)

        sns.set_theme(style="whitegrid")
        ax = sns.barplot(data=sorted_df,
                         x=x,
                         y=y,
                         hue=y,
                         palette='coolwarm_r',
                         dodge=False,
                         legend=False
                         )

        plt.xlabel('Score')
        plt.ylabel('Case')

        for i in range(len(sorted_df)):
            if sorted_df['inadequate'][i] == 1:
                plt.text(x=0, y=i, s='Inadequate', ha='left', va='center', fontweight='bold', color='gray')

        fig.tight_layout()

        save_dir = f'{self.result_dir}/{self.case_name}'
        os.makedirs(save_dir, exist_ok=True)

        plt.savefig(f'{save_dir}/{self.case_name}.jpg')

    def run_vis(self):
        sorted_df = self.sort_df()
        self.plot(sorted_df)