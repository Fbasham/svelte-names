import pandas as pd  
import os

def generate_dataframe(min_freq=500):
    filenames = os.listdir('../data')

    data = []
    for fn in filenames:
        with open(f'../data/{fn}','r') as f:
            data.extend(map(lambda s: s.strip().split(','),f.readlines()))

    df = pd.DataFrame(data,columns=['name','gender','freq'])
    df['freq'] = pd.to_numeric(df['freq'])
    df = df.query(f'freq>{min_freq}').groupby(['name','gender'],as_index=False).mean()
    return df.sort_values(by='freq',ascending=False)