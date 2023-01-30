
TOKEN ="6095717186:AAFt4CPdljJj_28u-6c8vJ6IWO4YGCyaIKU"

import telebot

bot = telebot.TeleBot(TOKEN)


def inviaMessaggio(studente):
    text = ""
    text += studente.materia
    text += "\n"
    text += studente.info
    
    bot.send_message(-873790098, text)


#bot.infinity_polling()