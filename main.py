HELP = """
help - справка
add - Добавить задачу
show - Показать задачи """
other = []
today = []
tomorrow = []
run = True
while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
            print(other, today, tomorrow)
    elif command == "add":
        task = input("Введите название задачи: ")
        if task == "today":
          today.append(task)
          print("Задача добавлена на сегодня")
        elif task == "tomorrow":
          tomorrow.append(task)
          print("Задача добавлена на завтра")
        elif task != "today" or "tomorrow":
          other.append(task)
          print("Задача добавлена на потом)))")
    elif command == "exit":
        print("Спасибо за использование! До свидания! ")
        break
    else:
        print("Unknown command")
        run = False
        print("До свидания")
        #break