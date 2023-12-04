from os.path import dirname, join

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        lines = file.read().split("\n")

    part1(lines)
    part2(lines)

def part1(lines):

    total = 0
    
    for line in lines:
        winning_numbers = line.split(":")[1].split("|")[0].split(" ")
        my_numbers = line.split(":")[1].split("|")[1].split(" ")
        match_count = 0
        for num in my_numbers:
            if num in winning_numbers and num != '':
                match_count += 1
        if match_count > 0:
            total += 2 ** (match_count - 1)

    print(total)

def part2(lines):

    total = 0
    card_count = {1: 1}

    for i, line in enumerate(lines):
        winning_numbers = line.split(":")[1].split("|")[0].split(" ")
        my_numbers = line.split(":")[1].split("|")[1].split(" ")
        match_count = 0
        for num in my_numbers:
            if num in winning_numbers and num != '':
                match_count += 1

        if match_count > 0:    
            for x in range(1, match_count+1):
                if card_count.get(i+x+1) is not None:
                    card_count[i+x+1] += card_count[i+1]
                else:
                    card_count[i+x+1] = card_count[i+1] + 1
        elif card_count.get(i+2) is None and i+2 < len(lines):
            card_count[i+2] = 1

    for value in card_count.values():
        total += value

    print(total)
            
if __name__ == '__main__':
    main()