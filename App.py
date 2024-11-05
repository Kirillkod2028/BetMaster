import tkinter as tk
from tkinter import messagebox
from League import *
from Sport import *
from Event import *
from Screen import *


class App:
    """Для визуальзации."""

    def closure(self, func, *args, **kwargs):
        def wrapper():
            result = func(*args, **kwargs)
            return result

        return wrapper
    # Функция замыкания для обертки функции с аргументами для последующего выполнения.
    def __init__(self, root, bookmaker, user, team_strength):
        self.bookmaker = bookmaker
        self.user = user
        self.root = root
        self.path = []
        self.team_strength = team_strength

        screen = Screen(2, [self.screen_by_sport_id(i) for i in range(2)],
                        ["Football", "Basketball" ], 0)
        # Создаем экран для выбора спорта с двумя вариантами: Футбол и Баскетбол.

        self.button = tk.Button(self.root, text="Sport", width=30, height=5,
                                command=self.closure(self.display_screen, screen, "sport"))
        # Создаем кнопку для отображения вариантов спорта.
        self.button.pack()
        self.buttons = [self.button]

    def display_screen(self, screen, name):
        self.path.append(name)
        for i in self.buttons:
            i.destroy()
        self.buttons = []
        # Проходим по существующим кнопкам и удаляем их.
        if screen.final == -1:
            # Проверяем, является ли экран последним
            for i in range(screen.num):
                button = tk.Button(self.root, text=screen.names[i], width=30, height=5,
                                   command=screen.obj[i])
                button.pack()
                self.buttons.append(button)
        elif screen.final == 0:
            for i in range(screen.num):
                button = tk.Button(self.root, text=screen.names[i], width=30, height=5,
                                   command=self.closure(self.display_screen, screen.obj[i], screen.names[i]))
                button.pack()
                self.buttons.append(button)
        if hasattr(screen,'par'):
            # Если экран имеет родительский экран, создаем кнопку Go Back".
            button = tk.Button(self.root, text="Go Back", width=30, height=5,
                               command=self.closure(self.display_screen, screen.par, "Go Back"))
            button.pack()
            self.buttons.append(button)

    # Функция для отображения выбранного экрана в зависимости от выбора пользователя.

    def screen_by_sport_id(self, id):
        screen = Screen(len(League.LeaguesSep[id]),
                        [self.generate_screen_round(League.LeaguesSepMatches[id][i]) for i in
                         range(len(League.LeaguesSep[id]))],
                        [League.LeaguesSep[id][i] for i in range(len(League.LeaguesSep[id]))], 0)
        # Создаем экран с количеством лиг.
        return screen

    # Функция для создания экрана на основе id спорта.
    def generate_screen_round(self, obj):
        screen = Screen(7, [self.generate_screen_matches(obj, i) for i in range(7)],
                        [Sport.Round[i] for i in range(7)], 0)
        return screen

    # Функция для генерации экрана для туров.
    def generate_screen_matches(self, obj, num):
        screen = Screen(4, [self.generate_bet_screen(obj[i]) for i in range(num * 4, num * 4 + 4)],
                        [obj[i] for i in range(num * 4, num * 4 + 4)], 0)

        return screen

    # Функция для генерации экрана для матчей.


    def generate_bet_screen(self,match):
        strA = self.team_strength[match[0]] #Считываем силу команды A
        strB = self.team_strength[match[1]] #Cчитываем силу команды B
        coefA = round((strA + strB) * 1.5 / strA,2) #Рассчитываем коэффициент на победу команды A
        coefB = round((strA + strB) * 1.5 / strB,2) #Рассчитываем коэффициент на победу команды B
        coefC = round(1/(1 - (1/coefA) - (1/coefB)),2) #Рассчитываем коэффициент на ничью
        screen = Screen(3,[self.closure(self.open_bet_window,Event(match[0] + " vs " + match[1],0,0)) for i in range(3)] ,[match[0] + " wins " + str(coefA), "draw " + str(coefC), match[1] + " wins " + str(coefB)],-1)
        return screen
        # Создаем экран с тремя вариантами ставок: на победу команды A, ничью и победу команды B.

    def show_events(self, league):
        """Показывает матчи для выбранной лиги."""
        events_window = tk.Toplevel(self.root)
        events_window.title(f"События в лиге: {league.name}")

        for event in league.events:
            event_button = tk.Button(events_window, text=f"{event.name} - Коэффициенты: {event.odds}",
                                     command=lambda e=event: self.open_bet_window(e))
            event_button.pack(pady=5)


    def open_bet_window(self, event):
        """Открывает поле для ставки."""
        bet_window = tk.Toplevel(self.root)

        tk.Label(bet_window, text="Введите сумму ставки:").pack(pady=10)
        amount_entry = tk.Entry(bet_window)
        amount_entry.pack(pady=5)

        def place_bet():
            """Для проверки корректности ставки."""
            amount = amount_entry.get()
            if amount.isdigit() and int(amount) > 0:
                amount = int(amount)
                if amount <= self.user.balance:  # Проверка на достаточность средств
                    self.user.balance -= amount  # Уменьшаем баланс пользователя
                    messagebox.showinfo("Ставка", f"Ставка в размере {amount} на событие {event.name} размещена!")
                    bet_window.destroy()  # Закрываем окно после размещения ставки

                else:
                    messagebox.showwarning("Ошибка", "Недостаточно средств на балансе.")
            else:
                messagebox.showwarning("Ошибка", "Введите корректную сумму ставки.")

        bet_button = tk.Button(bet_window, text="Сделать ставку", command=place_bet)
        bet_button.pack(pady=10)
