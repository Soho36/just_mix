import telebot

TOKEN = '6880602647:AAEJFBAN2jnOblSJoing7AXjzZcqFCFQFNI'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])

def repeat(message: telebot.types.Message):
    print("Received /start or /help command.")
    print(f"Username: {message.chat.username}")
    bot.reply_to(message, f"Welcome, {message.chat.username}")
    pass

bot.polling(none_stop=True)