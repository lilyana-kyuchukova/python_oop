class Controller:
    valid_types = ["Food", "Drink"]

    def __init__(self):
        self.players = list()
        self.supplies = list()

    def add_player(self, *players):
        players_added = list()
        for player in players:
            if player not in self.players:
                self.players.append(player)
                players_added.append(player.name)

        return f"Successfully added: {', '.join(players_added)}"

    def add_supply(self, *supplies):
        [self.supplies.append(supply) for supply in supplies]

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type not in self.valid_types:
            return  # == return None ignore the command

        for player in self.players:
            if player_name == player.name:
                break
        else:
            return

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        for i in range(len(self.supplies) -1, -1, -1):
            supply = self.supplies[i]

            if supply.__class__.__name__ == sustenance_type:
                self.supplies.pop(i)
                break

        else:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")


        # if player.stamina + supply.energy > 100:
        #     player.stamina = 100
        # else:
        #     player.stamina += supply.energy
        #
        # equals below

        player.stamina = min(player.stamina + supply.energy, 100)

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        current_players = sorted([
            next(filter(lambda p: p.name == first_player_name, self.players)),
            next(filter(lambda p: p.name == second_player_name, self.players))
            ], key=lambda p: p.stamina)  # current_player[0] will have the less stamina

        errors_list = []

        for player in current_players:
            if player.stamina <= 0:
                errors_list.append(f"Player {player.name} does not have enough stamina.")

        if errors_list:
            return "\n".join(errors_list)

        return self.fight(current_players)

    def fight(self, current_players):
        reduce_second_player_stamina = current_players[0].stamina / 2
        current_players[1].stamina = max(current_players[1].stamina - reduce_second_player_stamina, 0)

        # if current_players[1].stamina <= reduce_second_player_stamina:
        #     current_players[1].stamina = 0
        #     return f"Winner: {current_players[0].name}"
        # else:
        #     current_players[1].stamina -= reduce_second_player_stamina
        #

        reduce_first_player_stamina = current_players[1].stamina / 2
        current_players[0].stamina = max(current_players[0].stamina - reduce_first_player_stamina, 0)

        # if current_players[0].stamina <= reduce_first_player_stamina:
        #     current_players[0].stamina = 0
        # else:
        #     current_players[0].stamina -= reduce_first_player_stamina

        winner = sorted(current_players, key=lambda p: -p.stamina)[0]

        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        return "\n".join(
            [str(p) for p in self.players]
            +
            [s.details() for s in self.supplies]
        )
















