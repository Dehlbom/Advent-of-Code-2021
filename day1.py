
#Part 1
path = "C:\\Users\\Gusta\\Desktop\\Programmering\\Python\\AdventOfCode2021\\day1_input.txt"
with open(path, "r") as f:
    depth = f.readlines()
    count = 0
    for i in range(1, len(depth)):
        if int(depth[i]) > int(depth[i-1]):
            count += 1
    print(count)

#Part 2
    count = 0
    for i in range(0, len(depth)-3):
        group1 = int(depth[i]) + int(depth[i+1]) + int(depth[i+2])
        group2 = int(depth[i+1]) + int(depth[i+2]) + int(depth[i+3])
        if group1 < group2:
            count += 1
    print(count)
