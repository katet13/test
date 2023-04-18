import telebot
import random
token = "6298898102:AAE0qtCc_cSGFLitL9R892uFgTGYjRaxi18"
bot = telebot.TeleBot(token)
random_tasks = ["Вывпить пива", "посмотреть кино", "сгонять в магаз", "приготовить обед"]
HELP = """
/help - справка
/add - Добавить задачу
/show - Показать задачи обязательно указать дату
/random - Добавляет случайную задачу на сегодня """
tasks = {}
def add_todo(date, task):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = []
        tasks[date].append(task)
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)
@bot.message_handler(commands=["add"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)
    print(message.text)
@bot.message_handler(commands=["random"])
def random_add(message):
    date = "Сегодня".lower()
    task = random.choice(random_tasks)
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)
    print(message.text)
@bot.message_handler(commands=["show"])
def show(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    task = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[] " + task + "\n"
    else:
        text = "Лафа, валяем балду!!!"
    bot.send_message(message.chat.id, text)
bot.polling(none_stop=True)