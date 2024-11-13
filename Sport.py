class Sport:
    """Класс, который показывает различные виды спорта в конторе."""
    def __init__(self, name):
        self.name = name
        self.sport = []
    Sport_Number = 8




    def get_leagues(self):
        """Возвращает лиги, которые существуют в данном виде спорта."""
        return self.sport
    Sports = ["Football", "Basketball"] #список видов спорта

    Round = [f"Round_{i}" for i in range(1, Sport_Number)] #список туров