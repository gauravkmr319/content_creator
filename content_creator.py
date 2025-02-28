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


def generate_content(content, language, feature = "", selected_offers = "", selected_products = "", selected_tag = ""):
    prompt = get_prompt(content, language, feature, selected_offers, selected_products, selected_tag)
    response = llm.invoke(prompt)
    return response.content


def get_prompt(content, language, feature = "", selected_offers = "", selected_products = "", selected_tag = ""):
    length_str = get_length_str(get_length(content))

    prompt = f'''
    Generate a {content} related to credit card industry by giving an offer related to the example. No preamble.

    1) Content: {content}
    2) Language: {language}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English.
    3) Length: {length_str}
    Length of the generated {content} should be {length_str}
    4) Feature: {feature}
    If Feature is not "" the it means add that term to the post, add related text/offer.
    if Feature="Hotel" then add offer related to the hotel.
    if Feature="Restaurant" then add offer related to the restaurant.
    if Feature="Travel" then add offer related to the Travel.
    5) Selected Offers: {selected_offers}
    please use {selected_offers} if given
    if Selected Offers is supp it means supplementary card for your family, friends, colleague
    if Selected Offers is upgrade it means upgrade your card
    if Selected Offers is MEMBER GET MEMBER it means you refer your friends,family, colleague
    6) Selected Products: {selected_products}
    please use {selected_products} if given
    
    '''
    prompt = prompt.format(post_topic=content, post_length=length_str, post_language=language)

    examples = get_filtered_data(selected_tag)

    if len(examples) > 0:
        prompt += "8) Use following examples."

    for i, row in enumerate(examples):
        prompt += f'\n\n Example {i+1}: \n\n {row}'

        if i == 4: # Use max two samples
            break

    return prompt


if __name__ == "__main__":
    print(generate_content("Email", "English", "Short"))