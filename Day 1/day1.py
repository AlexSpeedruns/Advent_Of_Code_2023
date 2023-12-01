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
        first = "-1"
        last = "-1"
        for c in line:
            if first == "-1" and c.isnumeric():
                first = c
            elif c.isnumeric():
                last = c
        if last == "-1":
            last = first

        total += int(f"{first}{last}")

    print(total)

def part2(lines):
    total = 0
    nums = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    for line in lines:
        first = "-1"
        last = "-1"
        for i in range(len(line)):
            c = line[i]
            result = check_for_spelled_numbers(line, i, nums)
            if first == "-1" and c.isnumeric():
                first = c
            elif first == "-1" and result != "-1":
                first = result
            elif c.isnumeric():
                last = c
            elif result != "-1":
                last = result
        if last == "-1":
            last = first

        total += int(f"{first}{last}")

    print(total)

def check_for_spelled_numbers(line, i, nums):
    for num in nums.keys():
        if line[i:].startswith(num):
            return nums[num]
    return "-1"

if __name__ == '__main__':
    main()