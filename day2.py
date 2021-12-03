

#Part 1
path = "C:\\Users\\Gusta\\Desktop\\Programmering\\Python\\AdventOfCode2021\\day2_input.txt"
with open(path, "r") as f:
    positions = f.readlines()
    hp = 0
    depth = 0
    for i in positions:
        clean_pos = i.rstrip("\n")
        if 'down' in clean_pos:
            depth += int(clean_pos[-1])
        elif 'up' in clean_pos:
            depth -= int(clean_pos[-1])
        else:
            hp += int(clean_pos[-1])
    print(hp*depth)

    #part 2
    hp = 0
    aim = 0
    depth = 0
    for i in positions:
        clean_pos = i.rstrip("\n")
        if 'down' in clean_pos:
            aim += int(clean_pos[-1])
        elif 'up' in clean_pos:
            aim -= int(clean_pos[-1])
        else:
            hp += int(clean_pos[-1])
            depth += aim*int(clean_pos[-1])
    print(hp*depth)