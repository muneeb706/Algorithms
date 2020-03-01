# Problem:

# You and your eight-year-old nephew Elmo decide to play a simple card
# game. At the beginning of the game, the cards are dealt face up in a long
# row. Each card is worth a different number of points. After all the cards are
# dealt, you and Elmo take turns removing either the leftmost or rightmost
# card from the row, until all the cards are gone. At each turn, you can decide
# which of the two cards to take. The winner of the game is the player that
# has collected the most points when the game ends.
# Having never taken an algorithms class, Elmo follows the obvious greedy
# strategy—when it’s his turn, Elmo always takes the card with the higher
# point value. Your task is to find a strategy that will beat Elmo whenever
# possible. (It might seem mean to beat up on a little kid like this, but Elmo
# absolutely hates it when grown-ups let him win.)

# Describe and analyze an algorithm to determine, given the initial sequence
# of cards, the maximum number of points that you can collect
# playing against Elmo.

# Solution:


def play_card_game(card, elmo_has_first_turn):
    M = [[{"max_value_for_first_turn": 0, "max_value_for_second_turn": 0} for x in range(len(card))] for x in
         range(len(card))]

    for i in range(len(card)):
        M[i][i]["max_value_for_first_turn"] = card[i]
        M[i][i]["max_value_for_second_turn"] = 0

    sub_len = 1
    for i in range(len(card) - 1):
        first_pick = 0
        second_pick = 0
        if card[i] >= card[i + sub_len]:
            first_pick = card[i]
            second_pick = card[i + sub_len]
        else:
            first_pick = card[i + sub_len]
            second_pick = card[i]
        M[i][i + sub_len]["max_value_for_first_turn"] = first_pick
        M[i][i + sub_len]["max_value_for_second_turn"] = second_pick

    for i in range(2, len(card)):
        for j in range(len(card) - i):
            k = j + i
            if elmo_has_first_turn:
                if cards[j] > cards[k]:
                    M[j][k]["max_value_for_first_turn"] = cards[j] + M[j + 1][k]["max_value_for_second_turn"]
                    if (cards[k] + M[j + 1][k - 1]["max_value_for_second_turn"] > cards[j + 1] + M[j + 2][k][
                        "max_value_for_second_turn"]):
                        M[j][k]["max_value_for_second_turn"] = cards[k] + M[j + 1][k - 1]["max_value_for_second_turn"]
                    else:
                        M[j][k]["max_value_for_second_turn"] = cards[j + 1] + M[j + 2][k]["max_value_for_second_turn"]
                else:
                    M[j][k]["max_value_for_first_turn"] = cards[k] + M[j][k - 1]["max_value_for_second_turn"]
                    if (cards[j] + M[j + 1][k - 1]["max_value_for_second_turn"] > cards[k - 1] + M[j][k - 2][
                        "max_value_for_second_turn"]):
                        M[j][k]["max_value_for_second_turn"] = cards[j] + M[j + 1][k - 1]["max_value_for_second_turn"]
                    else:
                        M[j][k]["max_value_for_second_turn"] = cards[k - 1] + M[j][k - 2]["max_value_for_second_turn"]
            else:
                if (cards[k] + M[j][k - 1]["max_value_for_second_turn"] > cards[j] + M[j + 1][k][
                    "max_value_for_second_turn"]):
                    M[j][k]["max_value_for_first_turn"] = cards[k] + M[j][k - 1]["max_value_for_second_turn"]
                    if cards[j] > cards[k - 1]:
                        M[j][k]["max_value_for_second_turn"] = cards[j] + M[j + 1][k - 1]["max_value_for_second_turn"]
                    else:
                        M[j][k]["max_value_for_second_turn"] = cards[k - 1] + M[j][k - 2]["max_value_for_second_turn"]
                else:
                    M[j][k]["max_value_for_first_turn"] = cards[j] + M[j + 1][k]["max_value_for_second_turn"]
                    if cards[j + 1] > cards[k]:
                        M[j][k]["max_value_for_second_turn"] = cards[j + 1] + M[j + 2][k]["max_value_for_second_turn"]
                    else:
                        M[j][k]["max_value_for_second_turn"] = cards[k] + M[j + 1][k - 1]["max_value_for_second_turn"]

    return M[0][len(card) - 1]


cards = [28, 33, 48, 0, 26, 1, 3, 11, 22, 32, 12, 24]

print(play_card_game(cards, False))
