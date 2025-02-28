from llm_helper import llm
from few_shot import *
import random

def get_length_str(length):
    if length == "Short":
        return "1 to 20 lines"
    if length == "Medium":
        return "21 to 40 lines"
    if length == "Long":
        return "40 to 100 lines"

def get_length(content):
    if content == "blog":
        return "Long"
    if content == "email":
        my_list = ["Long", "Medium", "Short"]
        random_item = random.choice(my_list)
        return random_item
    if content == "tweet":
        return "short"

def generate_content_2(selected_content, selected_language, selected_category, selected_brand, selected_tone, sentiment):
    prompt = get_prompt_2(selected_content, selected_language, selected_category, selected_brand, selected_tone, sentiment)
    response = llm.invoke(prompt)
    return response.content


def get_prompt_2(selected_content, selected_language, selected_category, selected_brand, selected_tone, sentiment):
    length_str = get_length_str(get_length(selected_content))
    prompt = f'''
    Generate Creative Push Notification based on the given data.

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
    
    Now, generate Push Notification in **{selected_language}** with **{selected_tone}** for the following:  
    Category: {selected_category}  
    Partner: {selected_brand}  
     
    '''
    prompt = prompt.format(post_topic=selected_content, post_length=15, post_language=selected_language)

    examples = get_gyfter_dt_filtered(sentiment, selected_category, selected_brand)

    if len(examples) > 0:
        prompt += "Use More Examples."

    for i, row in enumerate(examples):
        prompt += f'\n\n Example {i + 1}: \n\n {row}'

        if i == 4:
            break
    print(prompt)
    prompt += f'If Sentiment is {sentiment} give rewards multiplier like 4X'
    return prompt


if __name__ == "__main__":
    print("Success")