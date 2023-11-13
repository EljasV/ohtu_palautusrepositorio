class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, param):
        players = self.reader.get_players()
        result = list(filter(lambda p: p.nationality == param, players))
        result.sort(key=lambda p: p.goals + p.assists, reverse=True)
        return result
