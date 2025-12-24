import pandas as pd

def data_preprocess(input_csv, output_csv, start_date, end_date):
    df = pd.read_csv(input_csv)  
    # really important to filter the ticks with volume > 0 !!!
    df = df[df['volume'] > 0]   
    df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')
    start_date_dt = pd.to_datetime(start_date)
    end_date_dt = pd.to_datetime(end_date)
    df = df[start_date_dt <= df['date']]
    df = df[df['date'] <= end_date_dt]
    df['date_time'] = pd.to_datetime(df['date'].dt.strftime('%Y-%m-%d') + ' ' + df['time'])
    df = df[['date_time', 'price', 'volume']]
    df.to_csv(output_csv, index=False)

def load_data(input_csv):
    df = pd.read_csv(input_csv)
    return df