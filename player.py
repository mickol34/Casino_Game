class Player:

    def __init__(self, name):
        self._name = name
        self._dices = [0, 0, 0, 0]
        self._points = 0

    def set_dices(self, dices):
        self._dices = dices

    def set_points(self, points):
        self._points = points

    def get_name(self):
        return self._name

    def get_dices(self):
        return self._dices

    def get_points(self):
        return self._points

    def count_dices(self):
        ones = self._dices.count(1)
        twos = self._dices.count(2)
        threes = self._dices.count(3)
        fours = self._dices.count(4)
        fives = self._dices.count(5)
        sixs = self._dices.count(6)
        return (ones, twos, threes, fours, fives, sixs)

    def max_double_value(self):
        counts = self.count_dices()
        max_double = 0
        value = 1
        for count in counts:
            if count == 2:
                max_double = value * 2
            value += 1
        return max_double

    def max_triple_value(self):
        counts = self.count_dices()
        max_triple = 0
        value = 1
        for count in counts:
            if count == 3:
                max_triple = value * 4
            value += 1
        return max_triple

    def max_quadruple_value(self):
        counts = self.count_dices()
        max_quad = 0
        value = 1
        for count in counts:
            if count == 4:
                max_quad = value * 6
            value += 1
        return max_quad

    def even_numbers_value(self):
        cond_1 = 1 not in self._dices
        cond_2 = 3 not in self._dices
        cond_3 = 5 not in self._dices
        if cond_1 and cond_2 and cond_3:
            return sum(self._dices) + 2
        return 0

    def odd_numbers_value(self):
        cond_1 = 2 not in self._dices
        cond_2 = 4 not in self._dices
        cond_3 = 6 not in self._dices
        if cond_1 and cond_2 and cond_3:
            return sum(self._dices) + 3
        return 0

    def dice_value(self):
        pairs = self.max_double_value()
        triples = self.max_triple_value()
        quads = self.max_quadruple_value()
        evens = self.even_numbers_value()
        odds = self.odd_numbers_value()
        max_value = max(pairs, triples, quads, evens, odds)
        return max_value
