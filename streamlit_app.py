import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

# Error explanation function
def explain_error(error_text):
    prompt = f"Explain this error in simple terms:\n\n{error_text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Streamlit UI
st.title("🧠 Code Error Storyteller")

error_input = st.text_area("Paste your Python or Linux error message here")

if st.button("Explain Error"):
    if error_input.strip():
        with st.spinner("Analyzing and explaining..."):
            explanation = explain_error(error_input)
            st.success("Explanation:")
            st.write(explanation)
    else:
        st.warning("Please paste an error message to explain.")
