import telebot
bot = telebot.TeleBot('1461284843:AAHA115L3Tv3mqd1SV9IscI7AkumfgVYu2s')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    res = message.text.lower().find('tiktok')

    if res > -1:
        bot.delete_message(message.chat.id, message.message_id)

bot.polling(none_stop=True, interval=0)