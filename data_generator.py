from faker import Faker
import pandas as pd
import random

fake = Faker()
Faker.seed(42)


def generate_customer_offer_data(num_records=100):
    data = []

    for _ in range(num_records):
        data.append({
            "customer_id": fake.uuid4(),
            "customer_name": fake.name(),
            "travel_feature": random.randint(0, 10),  # Number of travels
            "Hotel_feature": random.randint(0, 5),  # Number of hotel stays
            "Travel_lounge_feature": random.randint(0, 10),  # Lounge accesses
            "Reward_feature": random.randint(0, 5000),  # Reward points earned
            "Credit_limit_feature": round(random.uniform(5000, 100000), 2),  # Credit limit
            "Income_category": random.choice(["Low", "Medium", "High"]),
            "Churn_flag": random.choice(["Yes", "No"]),
            "Churn_reason": random.choice(["High Fees", "Better Offers", "Low Usage", "None"]),
            "personalized_marketing_offer_content": fake.sentence(nb_words=6),
            "Best_feature": random.choice(["Travel Benefits", "Cashback", "Low Interest", "Rewards"])
        })

    return pd.DataFrame(data)



categories = ["Travel", "Shopping", "Dining", "Entertainment", "Electronics"]
partner_websites = ["Amazon", "Flipkart", "Myntra", "MakeMyTrip", "Zomato", "Swiggy", "BookMyShow"]
tags = ["Limited Time", "Exclusive", "Trending", "Festival Special", "New Arrival"]
festivals = ["Diwali", "Christmas", "New Year", "Holi", "Eid"]
offers_names = ["Mega Cashback", "Festive Discount", "Super Saver Deal", "Exclusive Offer"]
terms_conditions = ["Valid for limited period", "Applicable on selected items", "Cannot be combined with other offers"]
how_to_use = ["Apply coupon at checkout", "Use code at partner website", "Auto-applied at payment"]


def generate_synthetic_offer_data(num_records=1000):
    data = []

    for _ in range(num_records):
        data.append({
            "Category": random.choice(categories),
            "Partner Website/Brand": random.choice(partner_websites),
            "Coupon Amount": f"{random.randint(10, 500)} OFF",
            "Rewards Percentage": f"{random.randint(1, 20)}%",
            "Discount": f"{random.randint(5, 50)}%",
            "Offer Summary": fake.sentence(nb_words=8),
            "Terms and Condition": random.choice(terms_conditions),
            "Offers Name": random.choice(offers_names),
            "How to Use": random.choice(how_to_use),
            "Special Award": fake.word().capitalize(),
            "Festival Name": random.choice(festivals),
            "Tag": random.choice(tags)
        })

    return pd.DataFrame(data)
