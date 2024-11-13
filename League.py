
from Event import *
class League:
    """Класс, который показывает лигу в конкретном виде спорта."""
    def __init__(self, name):
        self.name = name
        self.events = []
    LeaguesSep = [["La_Liga", "English premier league", "Seria A", "Bundesliga","Ligue_1"],["NBA"]]
    LeaguesSepMatches = [[Event.Match_La_liga, Event.Match_English_premier_league, Event.Match_Seria_A, Event.Match_Bundesliga,Event.Match_Ligue_1], [Event.Match_NBA]]

