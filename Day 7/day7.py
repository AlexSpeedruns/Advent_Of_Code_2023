from os.path import dirname, join
from collections import Counter
import operator

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        lines = file.read().split("\n")

    part1(lines)
    part2(lines)

def part1(lines):
    points = []
    updated_lines = []
    card_value_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    for line in lines:
        updated_lines.append((line.split()[0], line.split()[1]))

    for cards, bid in updated_lines:
        score = calculate_score(cards, card_value_map)
        points.append((score, int(bid)))

    points = sorted(points, key=operator.itemgetter(0))

    total = 0
    for i in range(len(points)):
        bid = points[i][1]
        total += (i+1) * bid

    print(total)
        

def part2(lines):
    points = []
    updated_lines = []
    card_value_map = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 11, 'K': 12, 'A': 13}
    for line in lines:
        updated_lines.append((line.split()[0], line.split()[1]))

    for cards, bid in updated_lines:
        highest_score = -1
        for card in cards:
            updated_cards = cards.replace("J", card)
            score = calculate_score(cards, card_value_map, updated_cards)
            if score > highest_score:
                highest_score = score
        points.append((highest_score, int(bid)))

    points = sorted(points, key=operator.itemgetter(0))

    total = 0
    for i in range(len(points)):
        bid = points[i][1]
        total += (i+1) * bid

    print(total)

def calculate_score(cards, card_value_map, updated_cards=[]):
    if updated_cards:
        counter = Counter([card for card in updated_cards])
    else:
        counter = Counter([card for card in cards])
    sorted_cards = list(sorted(counter.values()))
    score = -1
    type = -1

    if sorted_cards == [5]:
        type = 6
    elif sorted_cards == [1, 4]:
        type = 5
    elif sorted_cards == [2, 3]:
        type = 4
    elif sorted_cards == [1, 1, 3]:
        type = 3
    elif sorted_cards == [1, 2, 2]:
        type = 2
    elif sorted_cards == [1, 1, 1, 2]:
        type = 1
    elif sorted_cards == [1, 1, 1, 1, 1]:
        type = 0

    for i, c in enumerate(cards, start=1):
        score += (len(card_value_map) ** (len(cards) - i)) * card_value_map[c]

    score += (len(card_value_map) ** len(cards)) * type
    return score

if __name__ == '__main__':
    main()
