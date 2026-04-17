

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

## environment variables call
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

##creating chatbot
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant that answers questions of the user."),
        ("user","Question:{question}")
    ]
)

#streamlit app
st.title("Q&A Chatbot")
input_text=st.text_input("Please ask a question:")

# llm call
llm = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0.9
)
output_parser = StrOutputParser()
##chain
chain=prompt|llm|output_parser
if input_text:
    st.write(chain.invoke({'question':input_text})) #this takes the input from the user (question) and invokes the chain (LM FLow) to start the generation.
