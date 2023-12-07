from os.path import dirname, join

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        lines = file.read().split("\n")

    part1(lines)
    part2(lines)

def part1(lines):
    time = lines[0].split(":")[1].strip().split("     ")
    distance = lines[1].split(":")[1].strip().split("   ")

    total = 1
    
    for race in range(len(time)):
        race_record = int(distance[race])
        beat_count = 0
        for i in range(int(time[race])):
            current_dist = i * (int(time[race]) - i)
            if current_dist > race_record:
                beat_count += 1
        total *= beat_count

    print(total)

def part2(lines):
    time_arr = lines[0].split(":")[1].strip().split("     ")
    distance_arr = lines[1].split(":")[1].strip().split("   ")

    time = ""
    distance = ""
    for t in time_arr:
        time += t
    for d in distance_arr:
        distance += d

    time = int(time)
    distance = int(distance)

    total = 0

    for i in range(time):
        current_dist = i * (time - i)
        if current_dist > distance:
            total += 1
            
    print(total)

if __name__ == '__main__':
    main()