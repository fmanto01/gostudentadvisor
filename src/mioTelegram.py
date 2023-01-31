
TOKEN ="6095717186:AAFt4CPdljJj_28u-6c8vJ6IWO4YGCyaIKU"

import telebot

bot = telebot.TeleBot(TOKEN)


def inviaMessaggio(studente):
    text = ""
    text += f"<b>{studente.materia}</b>"
    text += "\n"
    text += studente.info
    text += "\n"
    text += "\n"
    text += studente.lezioni
    text += "\n"
    text += f"<a  href='{studente.walink}'>Riferimento: {studente.numero}</a>"
    
    bot.send_message(chat_id=-873790098, text=text, parse_mode="html")

def invio(messaggio):
    bot.send_message(chat_id=-873790098, text=messaggio)

#bot.infinity_polling()