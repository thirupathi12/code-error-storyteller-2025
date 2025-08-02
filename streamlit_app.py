import streamlit as st
from explain_error_with_openai import explain_error_with_openai

st.set_page_config(page_title="Code Error Storyteller", layout="centered")

st.title("🐍 Code Error Storyteller")
st.markdown("Enter a **Python or Linux error message**, and I'll turn it into a fun explanation!")

# User input
error_input = st.text_area("🔍 Paste your error message here:")

if st.button("🧠 Explain"):
    if not error_input.strip():
        st.warning("Please enter an error message.")
    else:
        with st.spinner("Asking OpenAI to explain..."):
            explanation = explain_error_with_openai(error_input)
            st.success("✅ Here's the explanation:")
            st.markdown(explanation)
