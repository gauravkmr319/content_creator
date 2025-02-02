from langchain_groq import ChatGroq
import os
#from dotenv import load_dotenv

#load_dotenv()
llm = ChatGroq(groq_api_key="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", model_name="llama-3.2-90b-vision-preview")


if __name__ == "__main__":
    response = llm.invoke("how to make pizza")
    print(response.content)





