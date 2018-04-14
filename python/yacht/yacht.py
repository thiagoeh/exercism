import collections

# Score categories
# Change the values as you see fit
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"


def score_yacht(dice):
    if dice[0] == dice[1] == dice[2] == dice[3] == dice[4]:
        return 50
    else:
        return 0


def score_big_straight(dice):
    if 2 in dice and 3 in dice and 4 in dice and 5 in dice and 6 in dice:
        return 30
    else:
        return 0


def score_little_straight(dice):
    if 1 in dice and 2 in dice and 3 in dice and 4 in dice and 5 in dice:
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
    return dice.count(1)


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
    if len(collections.Counter(dice)) == 2:
        return sum(dice)
    else:
        return 0


def score(dice, category):
    if category == YACHT:
        return score_yacht(dice)
    elif category == BIG_STRAIGHT:
        return score_big_straight(dice)
    elif category == LITTLE_STRAIGHT:
        return score_little_straight(dice)
    elif category == CHOICE:
        return score_choice(dice)
    elif category == FOUR_OF_A_KIND:
        return score_four_of_a_kind(dice)
    elif category == ONES:
        return score_ones(dice)
    elif category == TWOS:
        return score_twos(dice)
    elif category == THREES:
        return score_threes(dice)
    elif category == FOURS:
        return score_fours(dice)
    elif category == FIVES:
        return score_fives(dice)
    elif category == SIXES:
        return score_sixes(dice)
    elif category == FULL_HOUSE:
        return score_full_house(dice)
