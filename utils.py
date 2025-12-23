import pandas as pd

def data_preprocess(input_csv, output_csv, end_date):
    df = pd.read_csv(input_csv)  
    df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')
    end_date_dt = pd.to_datetime(end_date)
    df = df[df['date'] <= end_date]
    df.to_csv(output_csv, index=False)


