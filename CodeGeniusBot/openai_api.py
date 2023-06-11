import openai

def generate_code(user_message, systemprompt, userprompt):
    openai.api_key = "your_openai_api_key"

    prompt = f"User: {user_message}\nAI Developer:"
    message = []
    message.append({"role": "system", "content": systemprompt})
    message.append({"role": "user", "content": userprompt})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=message,
        temperature=0.2,
        max_tokens=4000,
        frequency_penalty=0.9
    )

    gpt_message = response.choices[0].message.content
    return gpt_message