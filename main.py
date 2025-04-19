import telebot

TOKEN = '8070938584:AAE4Rw-7nfZ926IyVhG-GMUVnF42XfOKXPI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Salom! Rasm olish uchun /image deb yozing.")

@bot.message_handler(commands=['image'])
def send_image(message):
    with open("image.jpg", "rb") as img:
        bot.send_photo(message.chat.id, img, caption='Sizga rasm')

bot.polling()
