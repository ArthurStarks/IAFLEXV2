# File: chat_gpt_api.py
import openai

#openai.api_key = "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"


# openai.api_key = "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"
openai.api_key = "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"
selected_model = "gpt-3.5-turbo"

#openai.api_key = "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"
#selected_model = "gpt-4"

def basic_generation(user_prompt):
    completion = openai.ChatCompletion.create(
        model=selected_model,
        messages=[
            {"role": "user", "content": user_prompt}
        ]
    )
    response = completion.choices[0].message.content
    return response
