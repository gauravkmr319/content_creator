import pandas as pd
import re
import spacy
import contractions
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
from langdetect import detect
from datetime import datetime

# Download required resources
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))
nlp = spacy.load("en_core_web_sm")

# Load dataset
file_path = "data/amex_gyfter.csv"
df = pd.read_csv(file_path)
print(df)


# Function to clean text
def clean_text(text):
    if pd.isna(text):
        return ""

    # Expand contractions (e.g., "can't" → "cannot")
    text = contractions.fix(text)

    # Remove HTML tags, special characters
    text = re.sub(r"<.*?>", " ", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # Convert to lowercase
    text = text.lower()

    # Remove stopwords
    text = " ".join([word for word in text.split() if word not in stop_words])

    return text


# Function to normalize text (spell correction, abbreviations)
def normalize_text(text):
    if pd.isna(text):
        return ""

    # Spell correction
    text = str(TextBlob(text).correct())

    # Expand abbreviations
    abbreviations = {"CC": "Credit Card", "FYI": "For Your Information", "TnC": "Terms and Conditions"}
    text = " ".join([abbreviations[word] if word in abbreviations else word for word in text.split()])

    return text


# Function to extract context (NER, sentiment, keywords)
def enrich_context(text):
    if pd.isna(text):
        return {"entities": {}, "sentiment": 0, "keywords": []}

    doc = nlp(text)

    # Extract Named Entities (e.g., Partner Name, Offer Details)
    entities = {ent.text: ent.label_ for ent in doc.ents}

    # Sentiment Analysis (-1 to 1)
    sentiment = TextBlob(text).sentiment.polarity

    # Extract Keywords (important words without stopwords)
    keywords = [token.text for token in doc if token.is_alpha and token.text.lower() not in stop_words]

    return {"entities": entities, "sentiment": sentiment, "keywords": keywords}


# Function to personalize content
def personalize_content(text, category, brand):
    if pd.isna(text):
        return ""

    personalized_text = f"Exclusive {category} offer from {brand}! {text}"

    # Customer Segmentation Example
    segments = {
        "Luxury": "Enjoy elite benefits with exclusive rewards.",
        "Travel": "Earn double miles on every flight booking!",
        "Shopping": "Save big with special discounts on top brands.",
        "Dining": "Taste the best with premium dining discounts."
    }

    return f"{personalized_text} {segments.get(category, '')}"


# Function to format content for different platforms
def format_content(text, content_type):
    formats = {
        "email": f"Dear Valued Customer,\n\n{text}\n\nBest Regards,\nYour Bank",
        "blog": f"<h2>{text}</h2><p>Read more on our website...</p>",
        "tweet": f"{text} #ExclusiveDeal #CreditCardRewards",
        "push_notification": text[:50]  # Trimmed for short messages
    }

    return formats.get(content_type, text)


# Function to validate content
def validate_content(text):
    if pd.isna(text):
        return ""

    # Check Grammar
    corrected_text = str(TextBlob(text).correct())

    # Compliance Filter (Avoid misleading words)
    forbidden_words = ["guaranteed", "lowest interest rate ever", "risk-free"]
    for word in forbidden_words:
        if word in corrected_text.lower():
            corrected_text = corrected_text.replace(word, "***")

    return corrected_text


# Apply preprocessing steps
df["Offer Summary Cleaned"] = df["Offer Summary"].apply(clean_text)
df["Offer Summary Normalized"] = df.apply(lambda row: f"{normalize_text(row['Offer Summary Cleaned'])} from {row['Partner Website/Brand']}", axis=1)
df["Context Info"] = df["Offer Summary Normalized"].apply(enrich_context)
df["Personalized Offer"] = df.apply(
    lambda row: personalize_content(row["Offer Summary Normalized"], row["Category"], row["Partner Website/Brand"]),
    axis=1)
df["Formatted Email"] = df["Personalized Offer"].apply(lambda x: format_content(x, "email"))
df["Formatted Tweet"] = df["Personalized Offer"].apply(lambda x: format_content(x, "tweet"))
df["Formatted Blog"] = df["Personalized Offer"].apply(lambda x: format_content(x, "blog"))
df["Formatted Push"] = df["Personalized Offer"].apply(lambda x: format_content(x, "push_notification"))
df["Validated Offer"] = df["Personalized Offer"].apply(validate_content)

print(df)
# Save preprocessed data to CSV
output_file = "data/preprocessed_amex_gyfter.csv"
df.to_csv(output_file, index=False)
#
# print(f"Preprocessed data saved to {output_file}")
