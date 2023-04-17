import telebot
from telebot import types

TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn0 = types.KeyboardButton("0")
    # markup.add(btn0)
    btn1 = types.KeyboardButton("1")
    markup.add(btn0, btn1)
    btn2 = types.KeyboardButton("2")
    # markup.add(btn2)
    btn3 = types.KeyboardButton("3")
    markup.add(btn2, btn3)
    btn4 = types.KeyboardButton("4")
    # markup.add(btn4)
    btn5 = types.KeyboardButton("5")
    markup.add(btn4, btn5)
    btn6 = types.KeyboardButton("6")
    # markup.add(btn6)
    btn7 = types.KeyboardButton("7")
    markup.add(btn6, btn7)
    btn_all = types.KeyboardButton("Всі уроки")
    markup.add(btn_all)
    bot.send_message(message.chat.id, f"Привіт, <b>{message.from_user.first_name}</b>\n \
Цей бот відправить о котрій починається і закінчується урок. \n \
Вибери розклад якого уроку тобі відправити:", parse_mode="html", reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message, content_types=['text']):
    if message.text is None:
        bot.send_message(message.chat.id, "Ви відправили не текстове повідомлення")
    elif message.text == "/start":
        start(message)
    elif message.text == "0":
        bot.send_message(message.chat.id, "0 Урок: \n8:10 -- 8:55")
    elif message.text == "1":
        bot.send_message(message.chat.id, "1 Урок: \n9:00 -- 9:45")
    elif message.text == "2":
        bot.send_message(message.chat.id, "2 Урок: \n9:55 -- 10:40")
    elif message.text == "3":
        bot.send_message(message.chat.id, "3 Урок: \n10:50 -- 11:35")
    elif message.text == "4":
        bot.send_message(message.chat.id, "4 Урок: \n11:45 -- 12:30")
    elif message.text == "5":
        bot.send_message(message.chat.id, "5 Урок: \n12:50 -- 13:35")
    elif message.text == "6":
        bot.send_message(message.chat.id, "6 Урок: \n13:45 -- 14:30")
    elif message.text == "7":
        bot.send_message(message.chat.id, "7 Урок: \n14:40 -- 15:25")
    elif message.text == "Всі уроки":
        bot.send_message(message.chat.id, f"Розклад всіх уроків: \n\n\
<u><b>0 Урок</b>   8:10 -- 8:55</u> \n \
<i>Перерва</i>   8:55 -- 9:00 \n\n\
<u><b>1 Урок</b>   9:00 -- 9:45</u> \n \
<i>Перерва</i>   9:45 -- 9:55 \n \n\
<u><b>2 Урок</b>   9:55 -- 10:40</u> \n \
<i>Перерва</i>   10:40 -- 10:50\n \n\
<u><b>3 Урок</b>   10:50 -- 11:35</u> \n \
<i>Перерва</i>   11:35 -- 11:45 \n \n\
<u><b>4 Урок</b>   11:45 -- 12:30</u> \n \
<i>Перерва</i>   12:30 -- 12:50 \n \n\
<u><b>5 Урок</b>   12:50 -- 13:35</u> \n \
<i>Перерва</i>   13:35 -- 13:45 \n \n\
<u><b>6 Урок</b>   13:45 -- 14:30</u> \n \
<i>Перерва</i> 14:30 -- 14:40 \n \n\
<u><b>7 Урок</b>   14:40 -- 15:25</u> \n 😀😀😀😀😀😀😀😀😀", parse_mode="html")
    else:
        bot.send_message(message.chat.id, "Ви відправили не правильний номер уроку, відправте, будь ласка, ціле число від 0 до 7")
    bot.register_next_step_handler(message, on_click)

bot.polling(none_stop=True)
