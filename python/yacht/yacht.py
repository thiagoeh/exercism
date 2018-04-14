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
    for value in range(1,7):
        print(f'value {value}')
        if dice.count(value) >= 4:
            return dice.count(value) * value
    return 0

def score_fours(dice):
    return dice.count(4) * 4

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
    elif category == FOURS:
        return score_fours(dice)
