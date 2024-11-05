class Sport:
    """Класс, который показывает различные виды спорта в конторе."""
    def __init__(self, name):
        self.name = name
        self.sport = []



    def get_leagues(self):
        """Возвращает лиги, которые существуют в данном виде спорта."""
        return self.sport
    Sports = ["Football", "Basketball"] #список видов спорта

    Round = ["Round_1", "Round_2", "Round_3", "Round_4", "Round_5", "Round_6", "Round_7"] #список туров