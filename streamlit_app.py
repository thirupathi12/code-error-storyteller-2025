import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def explain_error_with_openai(error_type, error_message):
    prompt = f"""You are a helpful assistant that explains {error_type} errors in a clear, human-friendly way.

Error message: "{error_message}"

Explain what this error means and how to fix it. Be concise, beginner-friendly, and practical.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You're an expert Linux and Python error explainer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=300,
        )
        explanation = response['choices'][0]['message']['content'].strip()
        return explanation
    except Exception as e:
        return f"❌ API Error: {e}"
from explain_error_with_openai import explain_error_with_openai

# ... your UI logic ...
error_type = st.selectbox("Select Error Type", ["Linux", "Python"])
error_message = st.text_area("Paste your error message here:")

if st.button("Explain"):
    if error_message.strip():
        with st.spinner("Explaining..."):
            result = explain_error_with_openai(error_type, error_message)
        st.markdown("### 📘 Explanation")
        st.write(result)
    else:
        st.warning("Please enter a valid error message.")
