from SummitQuest_Chalenge.climbers.arctic_climber import ArcticClimber
from SummitQuest_Chalenge.climbers.summit_climber import SummitClimber
from SummitQuest_Chalenge.peaks.arctic_peak import ArcticPeak
from SummitQuest_Chalenge.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type, climber_name):

        valid_climbers = {'ArcticClimber': ArcticClimber, 'SummitClimber': SummitClimber}

        if climber_type not in valid_climbers:
            return f"{climber_type} doesn't exist in our register."

        for climber in self.climbers:

            if climber.name == climber_name:
                return f"{climber_name} has been already registered."

        climber = valid_climbers[climber_type](climber_name)
        self.climbers.append(climber)
        return f"{climber_name} is successfully registered as a {climber_type}"

    def peak_wish_list(self, peak_type, peak_name, peak_elevation):

        valid_peaks = {'ArcticPeak': ArcticPeak, 'SummitPeak': SummitPeak}

        if peak_type not in valid_peaks:
            return f"{peak_type} is unknown type of peak."

        peak = valid_peaks[peak_type](peak_name, peak_elevation)

        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name, peak_name, gear):

        climber = self.__find_climber_by_name(climber_name)
        peak = self.__find_peak_by_name(peak_name)

        required_gears = set(peak.get_recommended_gear())
        missing_gears = required_gears - set(gear)
        if missing_gears:
            sorted_missing_gears = sorted(missing_gears)
            climber.is_prepared = False
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear {', '.join(sorted_missing_gears)}"
        else:
            return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name, peak_name):

        climber = self.__find_climber_by_name(climber_name)
        peak = self.__find_peak_by_name(peak_name)

        if not climber:
            return f"Climber {climber_name} is not registered yet."
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."
        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}"
        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):

        sorted_climbers = sorted([c for c in self.climbers if c.conquered_peaks],
                                 key=lambda x: (-len(x.conquered_peaks), x.name))
        result = [f"Total climbed peaks: {len(self.peaks)}",
                  "**Climber's statistics**",]
        climber_statistic = '\n'.join(str(c) for c in sorted_climbers)
        result.append(climber_statistic)
        return '\n'.join(result)

    def __find_climber_by_name(self, name):

        for climber in self.climbers:
            if climber.name == name:
                return climber
        return None

    def __find_peak_by_name(self, name):
        for peak in self.peaks:
            if peak.name == name:
                return peak
        return None
