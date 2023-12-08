from os.path import dirname, join
import sys

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        lines = file.read().split("\n\n")

    part1(lines)
    part2(lines)

def part1(lines):
    seeds = []
    lists = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
    }
    for i, section in enumerate(lines):
        if i == 0:
            seeds = section.split(":")[1].split()[1:]
        else:
            lists[i] = fill_list(lists[i], section)

    lowest = sys.maxsize

    for seed in seeds:
        current = int(seed)
        for i in range(1, len(lists)+1):
            rules = lists[i]
            for rule in rules:
                lower = int(rule.split()[1])
                upper = lower + int(rule.split()[2]) - 1
                start_next = int(rule.split()[0])
                if current >= lower and current <= upper:
                    current = start_next + (current - lower)
                    break
        if current < lowest:
            lowest = current
    
    print(lowest)

def part2(lines):
    seeds = []
    lists = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
    }
    for i, section in enumerate(lines):
        if i == 0:
            seed_line = section.split(":")[1].split()
            for j in range(0, len(seed_line), 2):
                seeds.append((int(seed_line[j]), int(seed_line[j]) + int(seed_line[j+1]) - 1))
        else:
            lists[i] = fill_list(lists[i], section)

    narrowed_seeds = seeds
    for i in range(1, len(lists)+1):
        rules = lists[i]
        seed_run = narrowed_seeds
        narrowed_seeds = []
        for seed in seed_run:
            seed_lower = seed[0]
            seed_upper = seed[1]
            for rule in rules:
                rule_lower = int(rule.split()[1])
                rule_upper = rule_lower + int(rule.split()[2]) - 1
                rule_shift = int(rule.split()[0]) - rule_lower

                if seed_lower >= rule_lower and seed_upper <= rule_upper:
                    narrowed_seeds.append((seed_lower + rule_shift, seed_upper + rule_shift))
                    break
                elif seed_lower >= rule_lower and seed_lower <= rule_upper:
                    narrowed_seeds.append((seed_lower + rule_shift, rule_upper + rule_shift))
                    seed_lower = rule_upper + 1
                elif seed_lower < rule_lower and seed_upper >= rule_upper:
                    narrowed_seeds.append((rule_lower + rule_shift, rule_upper + rule_shift))
                    seed_upper = rule_lower - 1
                elif seed_lower < rule_lower and seed_upper >= rule_lower:
                    narrowed_seeds.append((rule_lower + rule_shift, seed_upper + rule_shift))
                    seed_upper = rule_lower - 1
            else:    
                narrowed_seeds.append((seed_lower, seed_upper))

    print(min(narrowed_seeds)[0])

def fill_list(list, section):
    for line in section.split("\n")[1:]:
        list.append(line)

    return list
            
if __name__ == '__main__':
    main()
