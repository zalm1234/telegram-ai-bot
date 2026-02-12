import os
import sys

try:
    import openai
except ImportError:
    print("Error: Library 'openai' missing. Run: pip install openai")
    sys.exit(1)

# لێرە کلیلەکەت دابنێ
API_KEY = "AIzaSyA_2-LdkEApi3fpK2gzEG6GjgQJQFNJ66k"
openai.api_key = API_KEY

def chat_with_ai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", # یان هەر مۆدێلێکی تر کە بەکاری دەهێنیت
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("--- AI Bot is Running ---")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "بڕۆ"]:
            break
        
        result = chat_with_ai(user_input)
        print(f"AI: {result}")