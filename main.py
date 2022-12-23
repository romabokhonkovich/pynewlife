import telebot

bot = telebot.TeleBot('5985954584:AAHko-3Y2e8BhuDTU0oC71FdxYPeN9QF5jo')

@bot.message_handler(commands=["start"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, 'ты меня любишь(да/нет) ?')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == 'нет' or message.text == 'неа' or message.text == 'не':
        bot.send_message(message.from_user.id, "говно")
    elif message.text == 'да' or message.text == 'люблю':
        bot.send_message(message.from_user.id, "и я тебя!")
    else:
        bot.send_message(message.from_user.id, "не понимаю")

bot.polling(none_stop=True, interval=0)