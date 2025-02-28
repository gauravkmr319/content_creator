import pandas as pd
import json
import ast



def load_gyfter(file_path):
    with open(file_path, encoding="utf-8") as f:
        df = pd.read_csv(file_path)
        return df

def get_filtered_data( tag):
    df = load_gyfter("data/amex_gyfter.csv")
    df_filtered = df[df['Tag'] == tag]
    return df_filtered.to_dict(orient='records')

def get_gyfter_dt_filtered(sentiment, brand_type, brand):
    file_path = "data/preprocessed_amex_gyfter.csv"
    df = pd.read_csv(file_path)
    if "Context Info" in df.columns:

        # Define function to extract sentiment score
        def extract_sentiment(context_info):
            try:
                context_dict = ast.literal_eval(context_info)
                return context_dict.get("sentiment", 0)
            except (ValueError, SyntaxError):
                return 0

        # Apply extraction
        df["Sentiment Score"] = df["Context Info"].apply(extract_sentiment)

        # Define function to categorize sentiment
        def categorize_sentiment(score):
            if score > 0.2:
                return "Positive"
            elif score < 0.0:
                return "Negative"
            else:
                return "Neutral"

        # Apply categorization
        df["Sentiment Category"] = df["Sentiment Score"].apply(categorize_sentiment)

        df = df[df["Sentiment Category"] == sentiment]
        df = df[df["Category"] == brand_type]
        df = df[df["Partner Website/Brand"] == brand]
    return df



if __name__ == "__main__":

    dt = get_gyfter_dt_filtered("Neutral", "Dining", "Domino's")
    print(dt)