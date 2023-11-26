from typing import List
from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: [BaseEquipment] = list()
        self.teams: List[BaseTeam] = list()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.alphanum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type == "KneePad":
            self.equipment.append(KneePad())

        elif equipment_type == "ElbowPad":
            self.equipment.append(ElbowPad())

        else:
            return "Invalid equipment type!"

        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):

        if self.capacity < len(self.teams):
            if team_type == "OutdoorTeam":
                self.teams.append(OutdoorTeam(team_name, country, advantage))
            elif team_type == "IndoorTeam":
                self.teams.append((IndoorTeam(team_name, country, advantage)))
            else:
                return "Invalid team type!"

            return f"{team_type} was successfully added."

        return "Not enough tournament capacity."

    def sell_equipment(self, equipment_type: str, team_name: str):
       team = [t for t in self.teams if t.name == team_name][0]
       if equipment_type in self.equipment:
           pass








