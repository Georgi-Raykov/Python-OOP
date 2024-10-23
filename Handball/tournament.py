from Handball.equipment.elbow_pad import ElbowPad
from Handball.equipment.knee_pad import KneePad
from Handball.teams.indoor_team import IndoorTeam
from Handball.teams.outdoor_team import OutdoorTeam


class Tournament:

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError('Tournament name should contain letters and digits only!')
        self.__name = value

    def add_equipment(self, equipment_type):

        valid_equipments = {'KneePad': KneePad, 'ElbowPad': ElbowPad}

        if equipment_type not in valid_equipments:
            raise Exception('Invalid equipment type!')
        equipment = valid_equipments[equipment_type]()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type, team_name, country, advantage):

        valid_teams = {'OutdoorTeam': OutdoorTeam, 'IndoorTeam': IndoorTeam}
        if team_type not in valid_teams:
            raise Exception('Invalid type team!')
        if len(self.teams) >= self.capacity:
            return 'Not enough tournament capacity.'
        team = valid_teams[team_type](team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} successfully added."

    def sell_equipment(self, equipment_type, team_name):
        equipment = self.__find_equipment_by_name(equipment_type)
        team = self.__find_team_by_name(team_name)

        if team.budget < equipment.price:
            raise Exception('Budget is not enough!')
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name):
        team = self.__find_team_by_name(team_name)
        if team is None:
            raise Exception('No such team!')
        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type):

        collection = len([eq.increase_price() for eq in self.equipment if eq.__class__.__name__ == equipment_type])
        return f"Successfully changed {collection}pcs of equipment."

    def play(self, team_name1, team_name2):

        team1 = self.__find_team_by_name(team_name1)
        team2 = self.__find_team_by_name(team_name2)
        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception('Game cannot start! Team types mismatch!')

        team1_points = team1.advantage + sum([t.protection for t in team1.equipment])
        team2_points = team2.advantage + sum([t.protection for t in team2.equipment])

        if team1_points > team2_points:
            team1.win()
            return f"The winner is {team1.name}."
        elif team2_points > team1_points:
            team2.win()
            return f"The winner is {team2.name}."
        else:
            return 'No winner in this game.'

    def get_statistics(self):

        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)

        result = [f"Tournament name: {self.name}", f"Number of teams: {len(self.teams)}", "Teams:"]

        for team in sorted_teams:
            result.append(team.get_statistic())

        return '\n'.join(result)

    def __find_equipment_by_name(self, type):
        equipment_collection = [eq for eq in self.equipment if eq.__class__.__name__ == type]
        return equipment_collection[-1] if equipment_collection else None

    def __find_team_by_name(self, name):

        for team in self.teams:
            if team.name == name:
                return team
        return None
