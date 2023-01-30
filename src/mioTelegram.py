
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
    #text += f"<a target='_blank' rel='noreferrer' href='https://www.google.com/url?q=https://api.whatsapp.com/send?phone%3D390230566620%26text%3D1327282322&amp;sa=D&amp;source=editors&amp;ust=1675061479155087&amp;usg=AOvVaw0I97OsdXFBS449J9eA6J7g'>Riferimento: {studente.numero}</a>"
    
    bot.send_message(chat_id=-873790098, text=text, parse_mode="html")

def invio(messaggio):
    bot.send_message(chat_id=-873790098, text=messaggio)

#bot.infinity_polling()