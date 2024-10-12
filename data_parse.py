import pandas as pd
import os

folder_path = 'data/imports/usa'

df_list = []

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        country_name = filename.replace('.csv', '')
        df = pd.read_csv(os.path.join(folder_path, filename))

        df = df.iloc[:, [0, 1, 2]] 
        df = df.drop(index=[0, 1]) 
        df.iloc[:, 0] = df.iloc[:, 0].apply(lambda x: x[1:])
        df.columns.values[2] = "Total Import (in USD)"

        df['Country'] = country_name

        df_list.append(df)

        df.head()

combined_df = pd.concat(df_list, ignore_index=True)

combined_df.head()
