import telebot
import openai

TELEGRAM_TOKEN = "8289517227:AAGpASlCO7khYMySSZ1vl3CmN4MqQEiMRX8"
OPENAI_API_KEY = "AIzaSyA_2-LdkEApi3fpK2gzEG6GjgQJQFNJ66k"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(func=lambda message: True)
def reply(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message.text}
        ]
    )
    bot.reply_to(message, response["choices"][0]["message"]["content"])

bot.polling()
