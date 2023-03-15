from translate import translate
import telebot

TOKEN ="5926362159:AAHtrl44qbrxZriCUnGgw0SLYerJ8dzCNyg"
tarjimonbot = telebot.TeleBot(token=TOKEN)

#\start komandasi uchun mas'ul funksiya
@tarjimonbot.message_handler(commands=['start'])
def salom(message):
    xabar="Assalamu alaykum, Uz-Arabic-Uz tarjimon botiga xush kelibsiz."
    xabar+="\nMatningizni yuboring."
    tarjimonbot.reply_to(message, xabar)

#matnlar uchun mas'ul funksiya
@tarjimonbot.message_handler(func=lambda msg: msg.text is not None)
def tarjima(message):
    msg=message.text
    tarjimonbot.reply_to(message, translate(msg))
    
#botni ishga tushiramiz
tarjimonbot.polling()
