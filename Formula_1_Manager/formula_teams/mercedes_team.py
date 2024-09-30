from Formula_1_Manager.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    def __init__(self, budget):
        super().__init__(budget)

    @property
    def sponsors(self):
        return {
            'Petronas': {1: 1000000,
                         2: 500000,
                         },

            'TeamViewer': {5: 100000,
                           7: 50000,
                           }
        }

    @property
    def expenses(self):
        return 200000
