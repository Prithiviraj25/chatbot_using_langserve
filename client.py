import requests
import streamlit as st


def get_llama_output(input_text):
    response=requests.post("http://localhost:8000/animalinfo/invoke",
                          json={'input':{'name':input_text}})
    return response.json()['output']


st.title("A simple server created using langchain and getting output from OLLAMA LLAMA3")

input_text=st.text_input("Get the information of animal :")

if(input_text):
    st.write(get_llama_output(input_text))
