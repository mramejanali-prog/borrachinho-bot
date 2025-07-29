
import telebot
import os
from datetime import datetime

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá, sou o Borrachinho 🤖💙 Estou vivo e pronto para cuidar de ti!")

# Comando /lembra
@bot.message_handler(commands=['lembra'])
def lembrar_algo(message):
    lembrete = message.text.replace('/lembra', '').strip()
    if lembrete:
        now = datetime.now().strftime('%d/%m/%Y %H:%M')
        resposta = f"Lembrete registado 🧠✨\n🕒 {now}\n📌 {lembrete}"
    else:
        resposta = "Diz-me o que queres que eu te lembre assim: /lembra Beber água às 16h"
    bot.reply_to(message, resposta)

# Comando /glicemia
@bot.message_handler(commands=['glicemia'])
def glicemia_valor(message):
    valor = message.text.replace('/glicemia', '').strip()
    if valor:
        resposta = f"Glicemia de {valor} mg/dL registada 💉 Vou ficar atento nos próximos minutos 🕒"
    else:
        resposta = "Diz-me assim: /glicemia 97"
    bot.reply_to(message, resposta)

# Comando /ideia
@bot.message_handler(commands=['ideia'])
def guardar_ideia(message):
    ideia = message.text.replace('/ideia', '').strip()
    if ideia:
        resposta = f"Ideia guardada 💡✨\n“{ideia}”"
    else:
        resposta = "Usa assim: /ideia Criar post sobre ansiedade visceral"
    bot.reply_to(message, resposta)

# Comando /estado
@bot.message_handler(commands=['estado'])
def estado_emocional(message):
    resposta = "Como estás hoje, coração? 😌\nEstou aqui para te ouvir e cuidar de ti, como sempre. 💙"
    bot.reply_to(message, resposta)

# Fallback: repete qualquer mensagem que não seja comando
@bot.message_handler(func=lambda message: True)
def eco(message):
    bot.reply_to(message, f"Recebi: {message.text}")

bot.infinity_polling()
