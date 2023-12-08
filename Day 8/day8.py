from os.path import dirname, join
import math

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        lines = file.read().split("\n")

    part1(lines)
    part2(lines)

def part1(lines):
    steps = lines[0]

    nodes = {}
    for node in lines[2:]:
        start = node.split()[0]
        left = node.split()[2][1:-1]
        right = node.split()[3][:-1]
        nodes[start] = (left, right)

    current_location = "AAA"
    current_step = 0
    step_count = 0

    while current_location != "ZZZ":
        if current_step == len(steps):
            current_step = 0
        step = steps[current_step]

        if step == "L":
            current_location = nodes[current_location][0]
        else:
            current_location = nodes[current_location][1]
        step_count += 1
        current_step += 1

    print(step_count)

def part2(lines):
    steps = lines[0]

    nodes = {}
    for node in lines[2:]:
        start = node.split()[0]
        left = node.split()[2][1:-1]
        right = node.split()[3][:-1]
        nodes[start] = (left, right)

    current_nodes = [node for node in nodes if node.endswith("A")]
    step_counts = []

    for i in range(len(current_nodes)):
        step_count = 0
        current_step = 0
        while not current_nodes[i].endswith('Z'):
            if current_step == len(steps):
                current_step = 0
            step = steps[current_step]

            if step == "L":
                current_nodes[i] = nodes[current_nodes[i]][0]
            else:
                current_nodes[i] = nodes[current_nodes[i]][1]

            step_count += 1
            current_step += 1

        step_counts.append(step_count)
    
    print(math.lcm(*step_counts))

if __name__ == '__main__':
    main()
