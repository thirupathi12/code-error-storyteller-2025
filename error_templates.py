import random

def explain_error(error_text, style="plain", use_gpt=False):
    if "KeyError" in error_text:
        if style == "funny":
            return "💥 Your Python dictionary got moody. You asked for a key that doesn't exist. Try using .get() or check your spelling!"
        else:
            return "KeyError: This means you're trying to access a dictionary key that doesn't exist."
    elif "Permission denied" in error_text:
        if style == "funny":
            return "🔒 Linux says: 'You shall not pass!' You're probably missing sudo or file permissions."
        else:
            return "Permission denied: You don't have the rights to execute or read the file. Try sudo or check permissions."
    elif "ModuleNotFoundError" in error_text:
        return "Python can't find a module. You might need to install it using pip."
    elif "ZeroDivisionError" in error_text:
        return "Oops! Division by zero is not allowed in mathematics or Python."
    else:
        return "Sorry, I don't recognize this error yet. Try enabling GPT for more insights."