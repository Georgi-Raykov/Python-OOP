from SummitQuest_Chalenge.climbers.base_climber import BaseClimber
from SummitQuest_Chalenge.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):

    def __init__(self, name):
        super().__init__(name, strength=150)

    def can_climb(self):

        return self.strength >= 75

    def climb(self, peak: BasePeak):

        multiply = 1.3 if peak.difficulty_level == 'Advanced' else 2.5
        self.strength -= 30 * multiply
        self.conquered_peaks.append(peak.name)



