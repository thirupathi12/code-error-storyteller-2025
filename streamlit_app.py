import streamlit as st
import json
from error_templates import explain_error

st.set_page_config(page_title="Code Error Storyteller", page_icon="🧠")

st.title("🧠 Code Error Storyteller")
st.caption("Understand your Python and Linux errors like stories, not stack traces.")

with st.sidebar:
    st.header("Settings")
    mode = st.selectbox("Explanation Style", ["Plain", "Funny"])
    gpt_enabled = st.checkbox("Use GPT (Optional)", value=False)
    if gpt_enabled:
        openai_key = st.text_input("Enter OpenAI API Key", type="password")

error_input = st.text_area("Paste your Python or Linux error message here:")

if st.button("Explain Error"):
    if not error_input.strip():
        st.warning("Please enter an error message.")
    else:
        explanation = explain_error(error_input, style=mode.lower(), use_gpt=gpt_enabled)
        st.markdown("### Explanation")
        st.write(explanation)

        # Save to history
        history_file = "saved_stories.json"
        try:
            with open(history_file, "r") as f:
                history = json.load(f)
        except:
            history = []
        history.insert(0, {"error": error_input, "explanation": explanation})
        history = history[:10]
        with open(history_file, "w") as f:
            json.dump(history, f, indent=2)

st.markdown("---")
st.subheader("🕘 Recent Stories")

try:
    with open("saved_stories.json", "r") as f:
        saved = json.load(f)
        for item in saved:
            with st.expander(item["error"][:80] + "..."):
                st.write(item["explanation"])
except:
    st.info("No stories saved yet.")