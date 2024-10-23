from Handball.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):

    BUDGET = 500.0

    def __init__(self, name, country, advantage):
        super().__init__(name, country, advantage, budget=self.BUDGET)

    def win(self):

        self.advantage += 145
        self.wins += 1