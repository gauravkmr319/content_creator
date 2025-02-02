from llm_helper import llm
import random

#few_shot = FewShotLearner()


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


def generate_post(content, language, customer = "", feature = "", selected_offers = "", selected_products = ""):
    prompt = get_prompt(content, language, customer, feature, selected_offers, selected_products)
    response = llm.invoke(prompt)
    return response.content


def get_prompt(content, language, customer = "", feature = "", selected_offers = "", selected_products = ""):
    length_str = get_length_str(get_length(content))

    prompt = f'''
    Generate a {content} related to credit card industry by giving an offer related to the example. No preamble.

    1) Content: {content}
    2) Language: {language}
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English.
    3) Length: {length_str}
    Length of the generated {content} should be {length_str}
    4) Customer: {customer}
    Please use {customer} name in the generated {content} if given
    5) Feature: {feature}
    If Feature is not "" the it means add that term to the post, add related text/offer.
    if Feature="Hotel" then add offer related to the hotel.
    if Feature="Restaurant" then add offer related to the restaurant.
    if Feature="Travel" then add offer related to the Travel.
    6) Selected Offers: {selected_offers}
    please use {selected_offers} if given
    if Selected Offers is supp it means supplementary card for your family, friends, colleague
    if Selected Offers is upgrade it means upgrade your card
    if Selected Offers is MEMBER GET MEMBER it means you refer your friends,family, colleague
    7) Selected Products: {selected_products}
    please use {selected_products} if given
    
    '''
    prompt = prompt.format(post_topic=content, post_length=length_str, post_language=language)

    prompt += "8) Use the writing style as per the following examples."
    prompt += f'\n\n Example {1}: \n\n {"We understand concerns about high fees. Enjoy waived fees for the first year with our Member Get Member"}'

    return prompt


if __name__ == "__main__":
    print(generate_post("Email", "English", "Short"))