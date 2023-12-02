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
    for i, line in enumerate(lines):
        possible = True
        sets = line.split(":")[1].split(";")
        for set in sets:
            colors = {"red": 12, "green": 13, "blue": 14}
            grabs = set.split(",")
            for grab in grabs:
                num = grab.split(" ")[1]
                color = grab.split(" ")[2]
                colors[color] -= int(num)
            for value in colors.values():
                if value < 0:
                    possible = False
                    break
        if possible:
            total += (i+1)

    print(total)

def part2(lines):
    total = 0
    for _, line in enumerate(lines):
        sets = line.split(":")[1].split(";")
        max_colors = {"red": 0, "green": 0, "blue": 0}
        for set in sets:
            grabs = set.split(",")
            for grab in grabs:
                num = grab.split(" ")[1]
                color = grab.split(" ")[2]
                if int(num) > max_colors[color]:
                    max_colors[color] = int(num)
            
        set_power = 1
        for value in max_colors.values():
            set_power *= value
        total += set_power

    print(total)
            
if __name__ == '__main__':
    main()