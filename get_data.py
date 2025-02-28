import json
from llm_helper import llm
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
import pandas as pd
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler
from sklearn.feature_extraction.text import TfidfVectorizer



def get_best_feature_per_customer():
    dataframe = get_data()
    # List of feature columns to evaluate
    feature_cols = [
        "travel_feature", "hotel_feature", "lounge_access_feature", "spend_feature",
        "reward_feature", "redemption_feature", "credit_limit_feature", "billing_feature",
        "payment_feature", "bonus_feature", "membership_feature", "shopping_feature"
    ]
    # Identify the best feature and its value for each customer
    dataframe["best_feature"] = dataframe[feature_cols].idxmax(axis=1)
    dataframe["best_feature_value"] = dataframe[feature_cols].max(axis=1)

    return dataframe

def get_all_customers():
    dataframe = get_data()
    return dataframe['customer_id'].tolist()

def get_all_offers():
    dataframe = get_data()
    return set(dataframe['given_offers'].tolist())

def get_all_products():
    dataframe = get_data()
    return set(dataframe['current_product'].tolist())

def get_data():
    dataset_path = "data/enhanced_synthetic_credit_card_data.csv"
    dataframe = pd.read_csv(dataset_path)
    return dataframe

def get_all_tag():
    dataset_path = "data/amex_gyfter.csv"
    df = pd.read_csv(dataset_path)
    return set(df['Tag'].tolist())

if __name__ == "__main__":

    dataset_path = "data/amex_gyfter.csv"
    df = pd.read_csv(dataset_path)
    print(df)
    print(set(df['Tag'].tolist()))
    df2 = df[df['Tag'] == "shopping"]
    print(df2)

