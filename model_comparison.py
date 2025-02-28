import time
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob
from langchain_groq import ChatGroq

# Groq API Key (Replace with your actual key)
GROQ_API_KEY = "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"

# Define models available on Groq
MODEL_NAMES = [
    "llama-3.2-90b-vision-preview",
    "llama-3.2-11b-vision-preview",
    "mistral-saba-24b",
    "deepseek-r1-distill-qwen-32b",
]

# Sample prompt for evaluation
PROMPT = '''Generate Creative Push Notification based on the given data.

    Example 1:
    Language: English
    Tone: Friendly
    Category: Travel
    Partner: Amex
    Push Notification: "Save 10% on flights! Book now with Amex."

    Example 2:
    Language: English
    Tone: Friendly
    Category: Dining
    Partner: Zomato
    Offer Summary: Earn 15% cashback on Zomato
    Push Notification: ""Hunger Alert! 🍔 Enjoy 15% off on your Zomato order now. Order today!""

    Example 2:
    Language: Spanish
    Tone: Exciting
    Category: Shopping
    Partner: Amazon
    Offer Summary: Get 20% off on purchases
    Push Notification: "¡Venta relámpago! Obtén un 20% de descuento en Amazon ahora."

    Now, generate Push Notification in **English** with **Friendly** for the following:
    Category: Dining
    Partner: Domino's'''
# Function to evaluate each model
def evaluate_model(model_name):
    llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name=model_name)

    start_time = time.time()
    response = llm.invoke(PROMPT)
    end_time = time.time()

    output_text = response.content.strip()
    latency = round(end_time - start_time, 3)
    word_count = len(output_text.split())
    sentiment_score = TextBlob(output_text).sentiment.polarity

    return {
        "Model": model_name,
        "Latency_sec": latency,
        "Word_Count": word_count,
        "Sentiment_Score": sentiment_score,
        "Output_Sample": output_text[:200],
        "Full_Output": output_text,
    }

# Run evaluation on all models
results = [evaluate_model(model) for model in MODEL_NAMES]

# Convert results to DataFrame
df = pd.DataFrame(results)
print(df)

# Latency Comparison
plt.figure(figsize=(10, 5))
plt.bar(df["Model"], df["Latency_sec"], color=["blue", "green", "red", "orange", "purple"])
plt.xlabel("LLM Model")
plt.ylabel("Latency (seconds)")
plt.title("Latency Comparison (Groq LLMs)")
plt.xticks(rotation=15)
plt.show()

# Response Length (Word Count)
plt.figure(figsize=(10, 5))
plt.bar(df["Model"], df["Word_Count"], color=["cyan", "magenta", "yellow", "gray", "black"])
plt.xlabel("LLM Model")
plt.ylabel("Response Length (Words)")
plt.title("Response Length Comparison (Groq LLMs)")
plt.xticks(rotation=15)
plt.show()

# Sentiment Score Analysis
plt.figure(figsize=(10, 5))
plt.bar(df["Model"], df["Sentiment_Score"], color=["blue", "green", "red", "orange", "purple"])
plt.xlabel("LLM Model")
plt.ylabel("Sentiment Score (-1 to 1)")
plt.title("Sentiment Analysis of Responses (Groq LLMs)")
plt.xticks(rotation=15)
plt.axhline(y=0, color='gray', linestyle='--')
plt.show()

# Word Cloud (Using responses from all models)
all_text = " ".join(df["Full_Output"])
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Responses (Groq LLMs)")
plt.show()
