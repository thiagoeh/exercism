import collections


def score_yacht(dice):
    if len(collections.Counter(dice)) == 1:
        return 50
    else:
        return 0


def score_big_straight(dice):
    if sorted(dice) == [2, 3, 4, 5, 6]:
        return 30
    else:
        return 0


def score_little_straight(dice):
    if sorted(dice) == [1, 2, 3, 4, 5]:
        return 30
    else:
        return 0


def score_choice(dice):
    return sum(dice)


def score_four_of_a_kind(dice):
    for value in range(1, 7):
        if dice.count(value) >= 4:
            return value * 4
    return 0


def score_ones(dice):
    return dice.count(1) * 1


def score_twos(dice):
    return dice.count(2) * 2


def score_threes(dice):
    return dice.count(3) * 3


def score_fours(dice):
    return dice.count(4) * 4


def score_fives(dice):
    return dice.count(5) * 5


def score_sixes(dice):
    return dice.count(6) * 6


def score_full_house(dice):
    # Exactly two different values, and one of them occurs 2 or 3 times
    if len(collections.Counter(dice)) == 2 and 2 >= dice.count(dice[0]) <= 3:
        return sum(dice)
    else:
        return 0


# Score categories
# Change the values as you see fit
YACHT = score_yacht
ONES = score_ones
TWOS = score_twos
THREES = score_threes
FOURS = score_fours
FIVES = score_fives
SIXES = score_sixes
FULL_HOUSE = score_full_house
FOUR_OF_A_KIND = score_four_of_a_kind
LITTLE_STRAIGHT = score_little_straight
BIG_STRAIGHT = score_big_straight
CHOICE = score_choice


def score(dice, category):
    return category(dice)
