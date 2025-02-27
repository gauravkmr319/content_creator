from langchain_groq import ChatGroq
import os
#from dotenv import load_dotenv

#load_dotenv()
llm = ChatGroq(groq_api_key="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", model_name="llama-3.2-90b-vision-preview")


if __name__ == "__main__":
    response = llm.invoke("how are you")
    print(response.content)





