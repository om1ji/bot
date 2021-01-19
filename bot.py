import config
import telebot
import random
from telebot import types

bot = telebot.TeleBot(config.token)

query = []
greetings = ['Привет', 'привет', 'прив', 'пр', 'Дарова', "дарова", "Даров", "даров", "Дороу", "дороу", "здарова", "Здарова", "Здаров", "здаров", "Прувэт", "прувэт"]
omeja_v = ['Омиджи', "Омежа", "омиджи", "омежа", "омижи", "Омижи", "омеж", "омеjа", "амаль", "Амаль", "омеjи"]
na_chui = ["иди нахуй", "пошёл нахуй", "пошел нахуй", "Иди нахуй", "Пошёл нахуй", "Пошел нахуй", "Нахуй пошёл", "нахуй пошёл", "нахуй пошел", "Нахуй пошел", "нахуй иди", "Нахуй иди"]


# Main commands

@bot.message_handler(commands=['start'])
def handle_start(message):
	bot.send_message(message.chat.id, 'Здарова, напиши на /help, чтобы узнать мои команды')

# Other commands

@bot.message_handler(commands=['kto_pidor'])
def kto_pidr(message):
    bot.reply_to(message, 'Ну кто пидр... кто... ' + '@' + message.from_user.username + ' конечно!')            

@bot.message_handler(commands=['rnd_chars'])
def random_hundred_characters(message):
    def r_symbol():
        char = random.randint(0,52000)
        one_or_zero = any([start <= char <= end for start, end in 
                    [(4352, 4607), (11904, 42191), (43072, 43135), (44032, 55215), 
                    (63744, 64255), (65072, 65103), (65381, 65500), 
                    (131072, 196607)]
                    ])

        while one_or_zero == True:
            return r_symbol()
        
        char = chr(char)
        char = char.encode('utf-8')
        char = char.decode('utf-8', errors='ignore')
        return char

    i = 0
    s = ''
        
    while i < 100:
        s += r_symbol() + ' '
        i += 1
    bot.reply_to(message, text=s)
    
@bot.message_handler(commands=['help'])
def command_list(message):
    bot.reply_to(message, '''
    А я думал ты уже прочитал все команды...

/kto_pidor
/rnd_chars

P.S. попробуй послать бота ))
        ''')

# Text handler

@bot.message_handler(content_types=['text'])
def greeting(message):
    if message.text in greetings:
        bot.reply_to(message, 'Дарооова)')
        
    if message.text in na_chui:
        bot.reply_to(message, 'Сам(а) иди :))')
    
    if message.text in omeja_v:
        bot.reply_to(message, 'Я тебя слушаю')

if __name__ == '__main__':
	bot.infinity_polling()
