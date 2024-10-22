from Nautical_Catch_Chalenge.divers.free_diver import FreeDiver
from Nautical_Catch_Chalenge.divers.scuba_diver import ScubaDiver
from Nautical_Catch_Chalenge.fish.deep_sea_fish import DeepSeaFish
from Nautical_Catch_Chalenge.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:

    def __init__(self):

        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type, diver_name):

        valid_types = {'FreeDiver': FreeDiver, 'ScubaDiver': ScubaDiver}

        if diver_type not in valid_types:
            return f"{diver_type} is not allowed in our competition."
        diver = self.__find_diver_by_name(diver_name)

        if diver:
            return f"{diver_name} is already a participant."
        new_diver = valid_types[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type, fish_name, points):

        valid_types = {'PredatoryFish': PredatoryFish, 'DeepSeaFish': DeepSeaFish}
        if fish_type not in valid_types:
            return f"{fish_type} is forbidden for chasing in our competition."
        fish = self.__find_fish_by_name(fish_name)
        if fish:
            return f'{fish.name} is already permitted.'
        new_fish = valid_types[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}"

    def chase_fish(self, diver_name, fish_name, is_lucky):

        diver = self.__find_diver_by_name(diver_name)
        fish = self.__find_fish_by_name(fish_name)

        if diver is None:
            return f"{diver_name} is not registered for the competition."
        if fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver.name} will not be allowed to dive, due to health issues."
        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver.name} missed a good {fish.name}"
        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver.name} hits a {fish.points}pt. {fish.name}."
            else:
                diver.miss(fish.time_to_catch)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver.name} missed a good {fish.name}."
        elif diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver.name} hits a {fish.points}pt. {fish.name}."

    def health_recovery(self):
        counter = 0

        for diver in self.divers:
            if diver.has_health_issue:
                counter += 1
                diver.update_health_status()
                diver.renew_oxy()

        return f"Divers recovered: {counter}"

    def diver_catch_report(self, diver_name):
        diver = self.__find_diver_by_name(diver_name)
        result = f"**{diver_name} Catch Report**\n"
        for fish in diver.catch:
            result += f"{fish.fish_details()}" + '\n'
        return result.strip()

    def competition_statistics(self):

        divers_in_good_health = [d for d in self.divers if not d.has_health_issue]
        sorted_diver = sorted(divers_in_good_health, key=lambda d: (-d.competition_points, -len(d.catch), d.name))

        result = "**Nautical Catch Challenge Statistics**\n"
        for diver in sorted_diver:
            result += str(diver) + '\n'
        return result.strip()



    def __find_fish_by_name(self, name):
        for fish in self.fish_list:
            if fish.name == name:
                return fish
        return None

    def __find_diver_by_name(self, name):

        for diver in self.divers:

            if diver.name == name:
                return diver
        return None
