from random import randint
from player import Player


class Casino:

    def __init__(self, list_of_players):
        self._list_of_players = list_of_players

    def get_list_of_players(self):
        return self._list_of_players

    def add_player(self, player):
        self._list_of_players.append(player)

    def remove_player(self, player):
        self._list_of_players.remove(player)

    def dice_throw(self):
        dice_set = []
        for dice in range(4):
            dice_set.append(randint(1, 6))
        return dice_set

    def decide_winner(self):
        current_winner = None
        winners_points = 0
        winners_dices = []
        draw = True
        for player in self._list_of_players:
            if player.get_points() > winners_points:
                current_winner = player.get_name()
                winners_points = player.get_points()
                winners_dices = player.get_dices()
                draw = False
            if player.get_points == winners_points:
                draw = True
        if draw:
            return None
        return current_winner, winners_dices, winners_points

    def game(self):
        for player in self._list_of_players:
            player.set_dices(self.dice_throw())
            player.set_points(player.dice_value())
        winner = self.decide_winner()
        if not winner:
            return "Game indecisive - more than one player got best score!"
        w0 = winner[0]
        w1 = winner[1]
        w2 = winner[2]
        return f"Game won by {w0} with {w1} dices and {w2} points!"


Stachu = Player("Stachu")
Stachu.set_dices([6, 6, 6, 5])
Grzechu = Player("Grzechu")
Grzechu.set_dices([6, 4, 6, 6])
Krzychu = Player("Krzychu")
Krzychu.set_dices([1, 2, 3, 4])
kasyno = Casino([Stachu, Krzychu, Grzechu])
print(kasyno.game())
