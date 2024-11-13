class Event:
    """Класс представляющий спортивное событие."""
    def __init__(self, name, odds, league):
        self.name = name
        self.odds = odds
        self.league = league
        self.status = "ongoing"

    Events = [[1, 0], [2, 7], [3, 6], [4, 5], [7, 0], [1, 6], [2, 5],
         [3, 4], [6, 0], [7, 5], [1, 4], [2, 3], [5, 0], [6, 4],
         [7, 3], [1, 2], [4, 0], [5, 3], [6, 2], [7, 1], [3, 0],
         [4, 2], [5, 1], [6, 7], [2, 0], [3, 1], [4, 7], [5, 6]]
    # Расписание игр в каждой лиге
    Match_La_liga = [['Real_Madrid', 'Barcelona'], ['Athletico_Madrid', 'Villareal'], ['Seville', 'Girona'],
    ['Athletic', 'Real_Sostedad'], ['Villareal', 'Barcelona'], ['Real_Madrid', 'Girona'],
     ['Athletico_Madrid', 'Real_Sostedad'], ['Seville', 'Athletic'], ['Girona', 'Barcelona'],
     ['Villareal', 'Real_Sostedad'], ['Real_Madrid', 'Athletic'], ['Athletico_Madrid', 'Seville'],
     ['Real_Sostedad', 'Barcelona'], ['Girona', 'Athletic'], ['Villareal', 'Seville'],
     ['Real_Madrid', 'Athletico_Madrid'], ['Athletic', 'Barcelona'], ['Real_Sostedad', 'Seville'],
     ['Girona', 'Athletico_Madrid'], ['Villareal', 'Real_Madrid'], ['Seville', 'Barcelona'],
     ['Athletic', 'Athletico_Madrid'], ['Real_Sostedad', 'Real_Madrid'], ['Girona', 'Villareal'],
     ['Athletico_Madrid', 'Barcelona'], ['Seville', 'Real_Madrid'],
     ['Athletic', 'Villareal'], ['Real_Sostedad', 'Girona']] # Порядок Матчей в Ла лиге

    Match_English_premier_league = [['Manchester_City', 'Arsenal'], ['Liverpool', 'New_Castle'], ['Chelsea', 'Brighton'],
     ['Tottenham', 'Manchester_United'], ['New_Castle', 'Arsenal'], ['Manchester_City', 'Brighton'],
     ['Liverpool', 'Manchester_United'], ['Chelsea', 'Tottenham'], ['Brighton', 'Arsenal'],
     ['New_Castle', 'Manchester_United'], ['Manchester_City', 'Tottenham'], ['Liverpool', 'Chelsea'],
     ['Manchester_United', 'Arsenal'], ['Brighton', 'Tottenham'], ['New_Castle', 'Chelsea'],
     ['Manchester_City', 'Liverpool'], ['Tottenham', 'Arsenal'], ['Manchester_United', 'Chelsea'],
     ['Brighton', 'Liverpool'], ['New_Castle', 'Manchester_City'], ['Chelsea', 'Arsenal'], ['Tottenham', 'Liverpool'],
     ['Manchester_United', 'Manchester_City'], ['Brighton', 'New_Castle'], ['Liverpool', 'Arsenal'],
     ['Chelsea', 'Manchester_City'], ['Tottenham', 'New_Castle'], ['Manchester_United', 'Brighton']]
    # Порядок Матчей в Апл

    Match_Seria_A = [['Milan', 'Inter'], ['Juventus', 'Fiorentina'], ['Napoli', 'Atalanta'],
                     ['Roma', 'Lazio'], ['Fiorentina', 'Inter'], ['Milan', 'Atalanta'],
                     ['Juventus', 'Lazio'], ['Napoli', 'Roma'], ['Atalanta', 'Inter'], ['Fiorentina', 'Lazio'],
                     ['Milan', 'Roma'], ['Juventus', 'Napoli'], ['Lazio', 'Inter'], ['Atalanta', 'Roma'],
                     ['Fiorentina', 'Napoli'], ['Milan', 'Juventus'], ['Roma', 'Inter'], ['Lazio', 'Napoli'],
                     ['Atalanta', 'Juventus'], ['Fiorentina', 'Milan'], ['Napoli', 'Inter'],
                     ['Roma', 'Juventus'], ['Lazio', 'Milan'], ['Atalanta', 'Fiorentina'], ['Juventus', 'Inter'],
                     ['Napoli', 'Milan'], ['Roma', 'Fiorentina'], ['Lazio', 'Atalanta']]
    # Порядок Матчей в Серии А

    Match_Bundesliga = [['Bayer_Leverkusen', 'Bayer_Munich'], ['Borussia_Dortmund', 'Freiburg'],
                        ['Leipzig', 'Union'], ['Stuttgart', 'Eintracht'], ['Freiburg', 'Bayer_Munich'],
                        ['Bayer_Leverkusen', 'Union'], ['Borussia_Dortmund', 'Eintracht'], ['Leipzig', 'Stuttgart'],
                        ['Union', 'Bayer_Munich'], ['Freiburg', 'Eintracht'], ['Bayer_Leverkusen', 'Stuttgart'],
                        ['Borussia_Dortmund', 'Leipzig'], ['Eintracht', 'Bayer_Munich'], ['Union', 'Stuttgart'],
                        ['Freiburg', 'Leipzig'], ['Bayer_Leverkusen', 'Borussia_Dortmund'],
                        ['Stuttgart', 'Bayer_Munich'], ['Eintracht', 'Leipzig'], ['Union', 'Borussia_Dortmund'],
                        ['Freiburg', 'Bayer_Leverkusen'], ['Leipzig', 'Bayer_Munich'],
                        ['Stuttgart', 'Borussia_Dortmund'], ['Eintracht', 'Bayer_Leverkusen'], ['Union', 'Freiburg'],
                        ['Borussia_Dortmund', 'Bayer_Munich'], ['Leipzig', 'Bayer_Leverkusen'],
                        ['Stuttgart', 'Freiburg'], ['Eintracht', 'Union']]
    # Порядок Матчей в Бундеслиге

    Match_Ligue_1 = [['Monaco', 'Paris_Saint-Germain'], ['Marseilles', 'Brest'], ['Lion', 'Nice'],
                     ['Ren', 'Lill'], ['Brest', 'Paris_Saint-Germain'], ['Monaco', 'Nice'],
                     ['Marseilles', 'Lill'], ['Lion', 'Ren'], ['Nice', 'Paris_Saint-Germain'],
                     ['Brest', 'Lill'], ['Monaco', 'Ren'], ['Marseilles', 'Lion'], ['Lill', 'Paris_Saint-Germain'],
                     ['Nice', 'Ren'], ['Brest', 'Lion'], ['Monaco', 'Marseilles'], ['Ren', 'Paris_Saint-Germain'],
                     ['Lill', 'Lion'], ['Nice', 'Marseilles'], ['Brest', 'Monaco'], ['Lion', 'Paris_Saint-Germain'],
                     ['Ren', 'Marseilles'], ['Lill', 'Monaco'], ['Nice', 'Brest'],
                     ['Marseilles', 'Paris_Saint-Germain'], ['Lion', 'Monaco'], ['Ren', 'Brest'], ['Lill', 'Nice']]
    # Порядок Матчей в Лиге 1

    Match_NBA = [['Warriors', 'Lakers'], ['Boston', 'Dallas'], ['Clippers', 'Chicago'], ['Denver', 'Bucks'], ['Dallas', 'Lakers'], ['Warriors', 'Chicago'], ['Boston', 'Bucks'], ['Clippers', 'Denver'], ['Chicago', 'Lakers'], ['Dallas', 'Bucks'], ['Warriors', 'Denver'], ['Boston', 'Clippers'], ['Bucks', 'Lakers'], ['Chicago', 'Denver'], ['Dallas', 'Clippers'], ['Warriors', 'Boston'], ['Denver', 'Lakers'], ['Bucks', 'Clippers'], ['Chicago', 'Boston'], ['Dallas', 'Warriors'], ['Clippers', 'Lakers'], ['Denver', 'Boston'], ['Bucks', 'Warriors'], ['Chicago', 'Dallas'], ['Boston', 'Lakers'], ['Clippers', 'Warriors'], ['Denver', 'Dallas'], ['Bucks', 'Chicago']]
    # Порядок Матчей в NBA


La_Liga = ["Barcelona", "Real_Madrid", "Athletico_Madrid", "Seville", "Athletic", "Real_Sostedad", "Girona", "Villareal"]
calendar_La_Liga = []

English_premier_league = ["Arsenal", "Manchester_City", "Liverpool", "Chelsea", "Tottenham",
                          "Manchester_United", "Brighton", "New_Castle"]
calendar_English_premier_league = []

Seria_A = ["Inter", "Milan", "Juventus", "Napoli", "Roma",
           "Lazio", "Atalanta", "Fiorentina"]
calendar_Seria_A = []

Bundesliga = ["Bayer_Munich", "Bayer_Leverkusen", "Borussia_Dortmund", "Leipzig", "Stuttgart",
              "Eintracht", "Union", "Freiburg"]
calendar_Bundesliga = []

Ligue_1 = ["Paris_Saint-Germain", "Monaco", "Marseilles", "Lion", "Ren",
              "Lill", "Nice", "Brest"]
calendar_Ligue_1 = []

NBA = ["Lakers", "Warriors", "Boston", "Clippers", "Denver", "Bucks", "Chicago", "Dallas"]

calendar_NBA =[]

for i in range (len(Event.Events)):
    calendar_La_Liga.append([La_Liga[Event.Events[i][0]],La_Liga[Event.Events[i][1]]])

    calendar_English_premier_league.append([English_premier_league[Event.Events[i][0]],English_premier_league[Event.Events[i][1]]])

    calendar_Seria_A.append([Seria_A[Event.Events[i][0]], Seria_A[Event.Events[i][1]]])

    calendar_Bundesliga.append([Bundesliga[Event.Events[i][0]], Bundesliga[Event.Events[i][1]]])

    calendar_Ligue_1.append([Ligue_1[Event.Events[i][0]], Ligue_1[Event.Events[i][1]]])

    calendar_NBA.append([NBA[Event.Events[i][0]], NBA[Event.Events[i][1]]])

    # Генератор расписания в лигах.
"""
print(calendar_La_Liga)
print(calendar_English_premier_league)
print(calendar_Seria_A)
print(calendar_Bundesliga)
print(calendar_Ligue_1)
print(calendar_NBA)
"""

