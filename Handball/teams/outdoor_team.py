from Handball.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):

    BUDGET = 1000.0

    def __init__(self, name, country, advantage):
        super().__init__(name, country, advantage, budget=self.BUDGET)

    def win(self):
        self.advantage += 115
        self.wins += 1