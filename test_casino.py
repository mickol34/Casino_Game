from casino import Casino
from player import Player

# Testy obu klas są w jednym pliku, ponieważ początkowo obie klasy
# miałem w jednym pliku "casino.py", jednak na potrzeby monkeypatchu
# w ostatnim teście wyodrębniłem klasę Player do innego pliku

def test_player_init():
    player = Player("Stachu")
    assert player.get_name() == "Stachu"
    assert player.get_dices() == [0, 0, 0, 0]
    assert player.get_points() == 0


def test_player_setters():
    player = Player("Stachu")
    assert player.get_name() == "Stachu"
    assert player.get_dices() == [0, 0, 0, 0]
    assert player.get_points() == 0
    player.set_dices([1, 2, 3, 4])
    player.set_points(20)
    assert player.get_dices() == [1, 2, 3, 4]
    assert player.get_points() == 20


def test_player_count_dices():
    player1 = Player("Stachu")
    player2 = Player("Krzychu")
    player3 = Player("Grzechu")
    player1.set_dices([1, 2, 3, 4])
    player2.set_dices([0, 0, 0, 0])
    player3.set_dices([5, 5, 6, 6])
    assert player1.count_dices() == (1, 1, 1, 1, 0, 0)
    assert player2.count_dices() == (0, 0, 0, 0, 0, 0)
    assert player3.count_dices() == (0, 0, 0, 0, 2, 2)


def test_player_max_double_value():
    player1 = Player("Stachu")
    player2 = Player("Krzychu")
    player3 = Player("Grzechu")
    player1.set_dices([1, 2, 3, 4])
    player2.set_dices([3, 3, 4, 5])
    player3.set_dices([5, 5, 6, 6])
    assert player1.max_double_value() == 0
    assert player2.max_double_value() == 6
    assert player3.max_double_value() == 12


def test_player_max_triple_value():
    player1 = Player("Stachu")
    player2 = Player("Krzychu")
    player3 = Player("Grzechu")
    player1.set_dices([1, 2, 3, 4])
    player2.set_dices([3, 3, 3, 5])
    player3.set_dices([5, 5, 6, 6])
    assert player1.max_triple_value() == 0
    assert player2.max_triple_value() == 12
    assert player3.max_triple_value() == 0


def test_player_max_quadruple_value():
    player1 = Player("Stachu")
    player2 = Player("Krzychu")
    player3 = Player("Grzechu")
    player1.set_dices([1, 2, 3, 4])
    player2.set_dices([3, 3, 4, 5])
    player3.set_dices([6, 6, 6, 6])
    assert player1.max_quadruple_value() == 0
    assert player2.max_quadruple_value() == 0
    assert player3.max_quadruple_value() == 36


def test_player_even_numbers_value():
    player1 = Player("Stachu")
    player2 = Player("Krzychu")
    player3 = Player("Grzechu")
    player1.set_dices([1, 2, 3, 4])
    player2.set_dices([2, 2, 4, 6])
    player3.set_dices([6, 6, 6, 6])
    assert player1.even_numbers_value() == 0
    assert player2.even_numbers_value() == 16
    assert player3.even_numbers_value() == 26


def test_player_odd_numbers_value():
    player1 = Player("Stachu")
    player2 = Player("Krzychu")
    player3 = Player("Grzechu")
    player1.set_dices([1, 2, 3, 4])
    player2.set_dices([1, 1, 3, 5])
    player3.set_dices([5, 5, 5, 5])
    assert player1.odd_numbers_value() == 0
    assert player2.odd_numbers_value() == 13
    assert player3.odd_numbers_value() == 23


def test_player_dice_value():
    player1 = Player("Stachu")
    player2 = Player("Krzychu")
    player3 = Player("Grzechu")
    player4 = Player("Michu")
    player5 = Player("Zbychu")
    player6 = Player("Zdzichu")
    player7 = Player("Lechu")
    player1.set_dices([1, 2, 3, 4])
    player2.set_dices([1, 1, 3, 5])
    player3.set_dices([2, 2, 3, 3])
    player4.set_dices([2, 2, 6, 6])
    player5.set_dices([5, 5, 5, 1])
    player6.set_dices([4, 4, 4, 4])
    player7.set_dices([5, 5, 1, 1])
    assert player1.dice_value() == 0
    assert player2.dice_value() == 13
    assert player3.dice_value() == 6
    assert player4.dice_value() == 18
    assert player5.dice_value() == 20
    assert player6.dice_value() == 24
    assert player7.dice_value() == 15


def test_casino_init():
    player1 = Player("Stachu")
    player2 = Player("Krzychu")
    player3 = Player("Grzechu")
    casino = Casino([player1, player2, player3])
    assert casino.get_list_of_players() == [player1, player2, player3]


def test_casino_add_player():
    player1 = Player("Stachu")
    player2 = Player("Krzychu")
    player3 = Player("Grzechu")
    casino = Casino([player1, player2])
    casino.add_player(player3)
    assert casino.get_list_of_players() == [player1, player2, player3]


def test_casino_remove_player():
    player1 = Player("Stachu")
    player2 = Player("Krzychu")
    player3 = Player("Grzechu")
    casino = Casino([player1, player2, player3])
    casino.remove_player(player2)
    assert casino.get_list_of_players() == [player1, player3]


def test_casino_dice_throw(monkeypatch):

    def dice_one(v1, v2):
        return 1

    def dice_two(v1, v2):
        return 2

    def dice_three(v1, v2):
        return 3

    player1 = Player("Stachu")
    player2 = Player("Krzychu")
    player3 = Player("Grzechu")
    casino = Casino([player1, player2, player3])
    monkeypatch.setattr('casino.randint', dice_one)
    assert casino.dice_throw() == [1, 1, 1, 1]
    monkeypatch.setattr('casino.randint', dice_two)
    assert casino.dice_throw() == [2, 2, 2, 2]
    monkeypatch.setattr('casino.randint', dice_three)
    assert casino.dice_throw() == [3, 3, 3, 3]


def test_casino_decide_winner():
    player1 = Player("Stachu")
    player2 = Player("Krzychu")
    player3 = Player("Grzechu")
    player4 = Player("Michu")
    player1.set_dices([1, 2, 3, 4])
    player2.set_dices([1, 1, 3, 5])
    player3.set_dices([2, 2, 3, 3])
    player4.set_dices([2, 3, 4, 5])
    player1.set_points(player1.dice_value())
    player2.set_points(player2.dice_value())
    player3.set_points(player3.dice_value())
    player4.set_points(player4.dice_value())
    casino1 = Casino([player1, player2, player3])
    assert casino1.decide_winner() == ("Krzychu", [1, 1, 3, 5], 13)
    casino2 = Casino([player1, player4])
    assert casino2.decide_winner() is None


def test_casino_game(monkeypatch):

    def nothing(param, param2):
        pass

    player1 = Player("Stachu")
    player2 = Player("Krzychu")
    player3 = Player("Grzechu")
    player4 = Player("Michu")
    player1.set_dices([1, 2, 3, 4])
    player2.set_dices([1, 1, 3, 5])
    player3.set_dices([2, 2, 3, 3])
    player4.set_dices([2, 3, 4, 5])
    casino1 = Casino([player1, player2, player3])
    casino2 = Casino([player1, player4])
    Player.set_dices = nothing
    message1 = "Game won by Krzychu with [1, 1, 3, 5] dices and 13 points!"
    message2 = "Game indecisive - more than one player got best score!"
    assert casino1.game() == message1
    assert casino2.game() == message2
