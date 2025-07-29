
import telebot
import os

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá, sou o Borrachinho 🤖💙 Estou vivo e pronto para cuidar de ti!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Recebi: {message.text}")

bot.infinity_polling()
