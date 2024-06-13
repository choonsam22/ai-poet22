# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st

#from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

#chat_model = ChatOpenAI()
llm = ChatGoogleGenerativeAI(model="gemini-pro")


st.title("인공지능 시인")

content = st.text_input("시의 주제를 작성해주세요")

if st.button("시 작성하기 요청하기"):
    with st.spinner('Wait for it...'):
        result = llm.predict(content + "에 대한 시를 써줘")
        st.write(result)


