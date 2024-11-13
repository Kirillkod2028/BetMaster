import tkinter as tk
from Bookmaker import Bookmaker
from User import User
from App import App

def __main__():
    """
    Запрашивает у пользователя имя и баланс, а также загружает данные из файла 'data.html',
    создает аккаунт пользователя и запускает графический интерфейс приложения.
    """
    print("Enter your name.")  # Запрашиваем у пользователя ввод имени.

    # Бесконечный цикл для получения корректного имени.
    while True:
        name = str(input())
        if len(name) > 0:  # Проверяем, что имя не пустое.
            break
        else:
            print("That is not a name.")  # Если имя пустое, выводим сообщение об ошибке.

    print("Betting is fun and not intended for earning. Please enter your balance.")  # Запрашиваем у пользователя ввод баланса.

    # Бесконечный цикл для получения корректного баланса.
    while True:
        try:
            balance = int(input())  # Считываем баланс и пытаемся преобразовать его в целое число.
            break
        except ValueError:  # Если возникла ошибка преобразования (например, введено не число).
            print("That is not a number.")  # Выводим сообщение об ошибке.

    a = {}  # Инициализируем пустой словарь для хранения данных.
    # Открываем файл 'data.html' для чтения.
    with open('data.html', 'r') as file:
        for line in file:
            if line[:4] == "    ":
                tmp = line[4:].split(" ")  # Удаляем пробелы и разбиваем строку на части.
                tmp[1] = int(tmp[1][:-1])  # Преобразуем второй элемент в целое, убирая последний символ
                a[tmp[0]] = tmp[1]

    user = User(name, balance)  # Создаем объект пользователя с введенным именем и балансом.
    root = tk.Tk()
    root.title("BetMaster")
    BetMaster = Bookmaker()  # Создаем объект букмекера.
    app = App(root, BetMaster, user, a)  # Создаем экземпляр приложения с основным окном, букмекером, пользователем и данными.

    root.mainloop()

if __name__ == "__main__":
    __main__()


