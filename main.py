import telebot

TOKEN = '7922563213:AAHGBAgQK9M4a1l9uLb016k25099w6X-ljY'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Salom! Rasm olish uchun /image deb yozing.")

@bot.message_handler(commands=['image'])
def send_image(message):
    with open("image.jpg", "rb") as img:
        bot.send_photo(message.chat.id, img, caption='Sizga rasm')

bot.polling()
