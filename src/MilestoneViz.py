
#Importations
import pandas as pd
import numpy as np
import requests
import io
import os
import seaborn as sns
import matplotlib.pyplot as plt 
import statsmodels.api as sm
import plotly.express as px

#Visualization
class MilestoneViz:
    #Line Plots
    def lineplot(self,df,x_column,y_column,color_var,title,x_title,y_title):
        ax = sns.lineplot(
        data = df,      # Dataframe with long format data
        x = x_column,                   # Column for x-axis (dates)
        y = y_column,         # Column for y-axis (GDP values)
        hue = color_var               # Column for color differentiation (countries)
    )
        ax.set_title(title)
        ax.set_xlabel(x_title)
        ax.set_ylabel(y_title)
        plt.show()

    #Grouped Summary Bar Plots
    def scatter_plot(self,df, x_col, y_col,title,key):
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=x_col, y=y_col, hue=key, data=df)

        try:
            for region in df[key].unique():
                region_df = df[df[key] == region]
                z = np.polyfit(region_df[x_col], region_df[y_col], 1)
                p = np.poly1d(z)
                xp = np.linspace(region_df[x_col].min(), region_df[x_col].max(), 100)
                plt.plot(xp, p(xp), label=f'{region} Line of Best Fit')
        except np.linalg.LinAlgError:
            print("Error: unable to calculate line of best fit")

        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(title)
        plt.legend()
        plt.show()
    
    def group_plot(self,df,group,column,title):
        plot = df.groupby(group)[column].describe().transpose().drop('count')
        ax = plot.plot(kind = 'barh')
        ax.set_title(title)
        ax.set_xlabel('Value')
        ax.set_ylabel('Statistic')
        plt.show()

