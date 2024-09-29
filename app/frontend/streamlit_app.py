import streamlit as st
import requests

st.title("LLM Query Interface")

model_name = st.selectbox("Choose Model", ["openai", "llama"])
prompt = st.text_area("Enter Prompt")

if st.button("Submit"):
    response = requests.post("http://localhost:8000/api/v1/llm/query", json={"model_name": model_name, "prompt": prompt})
    st.write(response.json())
