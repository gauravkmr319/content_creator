import streamlit as st
from content_creator import generate_content
from push_notification import generate_content_2
from get_data import get_all_customers, get_all_offers, get_all_products, get_all_tag, get_best_feature_per_customer


content_options = ["email", "blog", "tweet", "Coupon"]
language_options = ["English", "Hindi"]
feature_options = ["travel", "Hotel", "Restaurant", "Lounge", "Movie"]
target_offers_option = get_all_offers()
target_product_option = get_all_products()
tag_option =  get_all_tag()



def main():

    st.markdown(
        """
        <style>
            .stApp {
                background-color: #d0e7f9;
            }
            .block-container {
                padding: 15px;
                max-width: 95%;
            }
            div[data-baseweb="select"] {
                width: 100%;
            }
            .stButton>button {
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                border-radius: 8px;
                padding: 10px 20px;
            }
            .stMarkdown h2, .stSubheader {
            color: black ;
            font-size: 24px ;
            font-weight: bold ;
            text-align: center ;
            margin-top: -20px ;
        }
        header, footer {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.subheader("Content Creator")

    col1, col2, col3, col4, col5, col6= st.columns(6)

    with col1:
        selected_content = st.selectbox("Content", options=content_options)

    with col2:
        selected_language = st.selectbox("Language", options=language_options)

    with col3:
        selected_feature = st.selectbox("Feature", options=feature_options)

    with col4:
        selected_offers = st.selectbox("Target Offers", options=target_offers_option)

    with col5:
        selected_products = st.selectbox("Products Offers", options=target_product_option)

    with col6:
        selected_tag = st.selectbox("Tag", options=tag_option)

    if st.button("Generate"):
        content = generate_content(selected_content, selected_language, selected_feature, selected_offers, selected_products, selected_tag)
        st.markdown(f'<div style="background-color: lightblue; padding: 10px; border-radius: 5px;">{content}</div>', unsafe_allow_html=True)


    gyfter_content_options = ["Push Notification"]
    partner_category = ["travel", "Hotel", "Restaurant", "Lounge", "Movie", "Dining"]
    tone = ["Friendly", "Formal"]
    partner_brand = ["MMT", "Zomato", "Domino's"]
    sentiment = ["Positive", "Neutral", "Negative"]

    st.subheader("Amex Gyfter")


    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        selected_content = st.selectbox("Type", options=gyfter_content_options)

    with col2:
        selected_language = st.selectbox("Select Language", options=language_options)

    with col3:
        selected_category = st.selectbox("Select Partner Category", options=partner_category)

    with col4:
        selected_brand = st.selectbox("Select Partner Brand", options=partner_brand)

    with col5:
        selected_tone = st.selectbox("Select Tone", options=tone)

    with col6:
        selected_sentient = st.selectbox("Sentiment Level", options=sentiment)


    if st.button("Send"):
        content = generate_content_2(selected_content, selected_language, selected_category, selected_brand,
                                   selected_tone, selected_sentient)
        st.markdown(f'<div style="background-color: lightblue; padding: 10px; border-radius: 5px;">{content}</div>',
                    unsafe_allow_html=True)


if __name__ == "__main__":
    main()
