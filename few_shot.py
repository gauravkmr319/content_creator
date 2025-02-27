import pandas as pd
import json



def load_gyfter(file_path):
    with open(file_path, encoding="utf-8") as f:
        df = pd.read_csv(file_path)
        return df

def get_filtered_data( tag):
    df = load_gyfter("data/amex_gyfter.csv")
    df_filtered = df[df['Tag'] == tag]
    return df_filtered.to_dict(orient='records')

if __name__ == "__main__":

    dt = get_filtered_data("shopping")
    print(dt)