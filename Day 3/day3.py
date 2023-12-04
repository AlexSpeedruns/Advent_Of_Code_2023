from os.path import dirname, join

def main():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "input.txt")
    with open(file_path, 'r') as file:
        lines = file.read().split("\n")

    grid = []

    for line in lines:
        row = []
        for c in line:
            row.append(c)
        grid.append(row)

    part1(grid)
    part2(grid)

def part1(grid):

    total = 0
    number = False
    include = False
    current_number = ""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            current = grid[i][j]
            if current.isdigit():
                number = True
                current_number += current
                if check_for_symbols(grid, i, j) and not include:
                    include = True
            elif number and not current.isdigit():
                number = False
                if include:
                    total += int(current_number)
                current_number = ""
                include = False

    print(total)

def part2(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            current = grid[i][j]
            if current == "*":
                nums = check_for_numbers(grid, i, j)
                if len(nums) == 2:
                    total += (int(list(nums)[0]) * int(list(nums)[1]))

    print(total)

def check_for_symbols(grid, i, j):
    if i > 0 and not grid[i-1][j].isdigit() and grid[i-1][j] != ".":
        return True
    elif i < len(grid[i])-1 and not grid[i+1][j].isdigit() and grid[i+1][j] != ".":
        return True
    elif j > 0 and not grid[i][j-1].isdigit() and grid[i][j-1] != ".":
        return True
    elif j < len(grid)-1 and not grid[i][j+1].isdigit() and grid[i][j+1] != ".":
        return True
    elif i > 0 and j > 0 and not grid[i-1][j-1].isdigit() and grid[i-1][j-1] != ".":
        return True
    elif i < len(grid[i])-1 and j > 0 and not grid[i+1][j-1].isdigit() and grid[i+1][j-1] != ".":
        return True
    elif i > 0 and j < len(grid)-1 and not grid[i-1][j+1].isdigit() and grid[i-1][j+1] != ".":
        return True
    elif i < len(grid[i])-1 and j < len(grid)-1 and not grid[i+1][j+1].isdigit() and grid[i+1][j+1] != ".":
        return True
    return False

def check_for_numbers(grid, i, j):
    nums = set()
    if i > 0 and grid[i-1][j].isdigit():
        nums.add(find_number(grid, i-1, j))
    if i < len(grid[i])-1 and grid[i+1][j].isdigit():
        nums.add(find_number(grid, i+1, j))
    if j > 0 and grid[i][j-1].isdigit():
        nums.add(find_number(grid, i, j-1))
    if j < len(grid)-1 and grid[i][j+1].isdigit():
        nums.add(find_number(grid, i, j+1))
    if i > 0 and j > 0 and grid[i-1][j-1].isdigit():
        nums.add(find_number(grid, i-1, j-1))
    if i < len(grid[i])-1 and j > 0 and grid[i+1][j-1].isdigit():
        nums.add(find_number(grid, i+1, j-1))
    if i > 0 and j < len(grid)-1 and grid[i-1][j+1].isdigit():
        nums.add(find_number(grid, i-1, j+1))
    if i < len(grid[i])-1 and j < len(grid)-1 and grid[i+1][j+1].isdigit():
        nums.add(find_number(grid, i+1, j+1))
    return nums

def find_number(grid, i, j):
    while j > 0 and grid[i][j-1].isdigit():
        j -= 1

    num = ""
    while j < len(grid)-1 and grid[i][j].isdigit():
        num += grid[i][j]
        j += 1

    return num
            
if __name__ == '__main__':
    main()