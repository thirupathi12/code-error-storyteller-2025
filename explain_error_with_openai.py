# explain_error_with_openai.py

import openai

def explain_error_with_openai(error_message):
    """Uses OpenAI to explain a given Python error message."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a Python expert that explains error messages in simple terms."},
                {"role": "user", "content": f"Explain this Python error: {error_message}"}
            ],
            temperature=0.5
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error from OpenAI API: {str(e)}"

