from os.path import dirname, join
import numpy as np

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
        line_arr = [int(l) for l in line.split()]
        total += recurse_sequence(line_arr)
    print(total)

def part2(lines):
    total = 0
    for line in lines:
        line_arr = [int(l) for l in line.split()]
        total += recurse_sequence_part2(line_arr)
    print(total)

def recurse_sequence(line_arr):
    sequence = []
    for i in range(len(line_arr)-1):
        sequence.append(line_arr[i+1] - line_arr[i])
    if sequence[0] == 0 and len(np.unique(sequence)) == 1:
        return line_arr[-1]
    else:
        return line_arr[-1] + recurse_sequence(sequence)
    
def recurse_sequence_part2(line_arr):
    sequence = []
    for i in range(len(line_arr)-1):
        sequence.append(line_arr[i+1] - line_arr[i])
    if sequence[0] == 0 and len(np.unique(sequence)) == 1:
        return line_arr[-1]
    else:
        return line_arr[0] - recurse_sequence_part2(sequence)

if __name__ == '__main__':
    main()