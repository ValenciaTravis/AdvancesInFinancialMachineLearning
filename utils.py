import pandas as pd

def data_preprocess(input_csv, output_csv, start_date, end_date):
    df = pd.read_csv(input_csv)  
    df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')
    start_date_dt = pd.to_
    end_date_dt = pd.to_datetime(end_date)
    df = df[df['date'] <= end_date]
    df.to_csv(output_csv, index=False)

def load_data():
    df = pd.read_csv("data/raw.csv")
    df['date_time'] = pd.to_datetime(df['date'] + ' ' + df['time'])
    df = df[['date_time', 'price', 'volume']]
    return df