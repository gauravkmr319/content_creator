import streamlit as st
from few_shot import FewShotLearner
from content_creator import generate_content
from preprocess import get_all_customers, get_all_offers, get_all_products


content_options = ["email", "blog", "tweet"]
language_options = ["English", "Hindi"]
feature_options = ["travel", "Hotel", "Restaurant", "Lounge", "Movie"]
customer_options = get_all_customers()
target_offers_option = get_all_offers()
target_product_option = get_all_products()



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

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        selected_content = st.selectbox("Content", options=content_options)

    with col2:
        selected_language = st.selectbox("Language", options=language_options)

    with col3:
        selected_customer = st.selectbox("Customer", options=customer_options)

    with col4:
        selected_feature = st.selectbox("Feature", options=feature_options)

    with col5:
        selected_offers = st.selectbox("Target Offers", options=target_offers_option)

    with col6:
        selected_products = st.selectbox("Products Offers", options=target_product_option)

    if st.button("Generate"):
        content = generate_content(selected_content, selected_language, selected_customer, selected_feature, selected_offers, selected_products)
        st.markdown(f'<div style="background-color: lightblue; padding: 10px; border-radius: 5px;">{content}</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
