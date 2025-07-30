import streamlit as st
import json
from error_templates import explain_error

# Page configuration
st.set_page_config(
    page_title="Code Error Storyteller",
    page_icon="🧠",
    layout="centered"
)

# App Title and Tagline
st.title("🧠 Code Error Storyteller")
st.caption("Turn confusing Python and Linux errors into simple, human-friendly explanations.")

# Sidebar Settings
with st.sidebar:
    st.header("⚙️ Settings")

    # Choose error type
    error_type = st.selectbox("Error Type", ["Python", "Linux"])

    # Style selection
    style_mode = st.selectbox("Explanation Style", ["Plain", "Funny", "Metaphorical"])

    # GPT integration
    gpt_enabled = st.checkbox("Use GPT (Optional)", value=False)
    openai_key = None
    if gpt_enabled:
        openai_key = st.text_input("Enter OpenAI API Key", type="password")

# Main input section
st.markdown("### 🔍 Paste Your Error Below")
error_input = st.text_area("Paste your Python or Linux error message here:", height=150)

# Explain error button
if st.button("Explain Error"):
    if not error_input.strip():
        st.warning("⚠️ Please enter an error message.")
    else:
        # Generate explanation
        explanation = explain_error(
            error_input,
            error_type=error_type.lower(),
            style=style_mode.lower(),
            use_gpt=gpt_enabled,
            api_key=openai_key
        )

        # Display explanation
        st.markdown("## 📖 Explanation")
        st.success(explanation)

        # Save to history
        history_file = "saved_stories.json"
        try:
            with open(history_file, "r") as f:
                history = json.load(f)
        except FileNotFoundError:
            history = []

        history.insert(0, {
            "error": error_input.strip(),
            "explanation": explanation,
            "type": error_type,
            "style": style_mode
        })
        history = history[:10]  # Keep only latest 10
        with open(history_file, "w") as f:
            json.dump(history, f, indent=2)

# Display saved history
st.markdown("---")
st.subheader("🕘 Recent Stories")

try:
    with open("saved_stories.json", "r") as f:
        saved = json.load(f)
        for item in saved:
            with st.expander(f"[{item['type']}] {item['error'][:80]}..."):
                st.markdown(f"**Style:** {item['style']}")
                st.write(item["explanation"])
except FileNotFoundError:
    st.info("No stories saved yet.")
