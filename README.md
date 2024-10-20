# BetMaster
Букмекерской приложение с возможностью поставить на различные события в футболе, баскетболе, формуле 1
В проекте будут использоваться классы:

class Sport:
    """Класс, который показывает различные виды спорта в конторе."""
    
    def __init__(self, name):
        self.name = name
        self.leagues = []

    def add_league(self, league):
        """Добавляет лигу в общий список лиг."""
        self.leagues.append(league)

    def get_leagues(self):
        """Возвращает лиги, которые существуют в данном виде спорта."""
        return self.leagues

class League:
    """Класс, который показывает лигу в конкретном виде спорта."""
    
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        """Добавляет игру/гран-при для конкретной лиги."""
        self.events.append(event)

class Event:
    """Класс представляющий спортивное событие."""
    
    def __init__(self, name, odds, league):
        self.name = name
        self.odds = odds
        self.league = league
        self.status = "ongoing"

class Bookmaker:
    """Класс самой конторы, он нужен для составления списка видов спорта."""
    
    def __init__(self):
        self.sports = []

    def add_sport(self, sport):
        """Добавляет вид спорта в список."""
        self.sports.append(sport)

class User:
    """Для информации о пользователе."""
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class App:
    """Для визуальзации."""
    
    def __init__(self, root, bookmaker, user):
        self.root = root
        self.bookmaker = bookmaker
        self.user = user
        self.root.title("Букмекерская контора")

        self.create_league_list()

    def create_league_list(self):
        """Создаёт и отображает лиги для каждого вида спорта в главном окне."""
        for sport in self.bookmaker.sports:
            sport_frame = tkinter.Frame(self.root)
            sport_frame.pack(pady=10)

            sport_label = tkinter.Label(sport_frame, text=sport.name, font=("Arial", 16))
            sport_label.pack(side=tkinter.LEFT)

            for league in sport.get_leagues():
                league_button = tkinter.Button(sport_frame, text=league.name, command=lambda l=league: self.show_events(l))
                league_button.pack(side=tkinter.LEFT, padx=5)

    def show_events(self, league):
        """Показывает матчи для выбранной лиги."""
        events_window = tkinter.Toplevel(self.root)
        events_window.title(f"События в лиге: {league.name}")

        for event in league.events:
            event_button = tkinter.Button(events_window, text=f"{event.name} - Коэффициенты: {event.odds}",
                                     command=lambda e=event: self.open_bet_window(e))
            event_button.pack(pady=5)

    def open_bet_window(self, event):
        """Открывает поле для ставки."""
        bet_window = tkinter.Toplevel(self.root)
        bet_window.title(f"Ставка на событие: {event.name}")

        tkinter.Label(bet_window, text="Введите сумму ставки:").pack(pady=10)
        amount_entry = tkinter.Entry(bet_window)
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

        bet_button = Tk.Button(bet_window, text="Сделать ставку", command=place_bet)
        bet_button.pack(pady=10)
