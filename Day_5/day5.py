# Day 5 part 2 incomplete
# I gave up after getting extremely frustruated

# Techincally, the code should work given a very powerful
# machine with a lot of memory and time lol

def binary_search(num, map):
    left = 0
    right = len(map) - 1
    while (left <= right):
        middle = (left + right) // 2
        source_start = map[middle][0]
        dest_start = map[middle][1]
        range_len = map[middle][2]
        if source_start <= num < (source_start + range_len):
            return dest_start + (num - source_start)
        elif (num >= source_start + range_len):
            left = middle + 1
        else:
            right = middle - 1
    return num
            

def get_destination(num, map):
    for source_start, dest_start, range_len in map:
        if source_start <= num < (source_start + range_len):
            return dest_start + (num - source_start)
    else:
        return num

# 7 maps in total
maps = [[] for i in range(7)]


with open('input.txt', 'r') as f:
    text = f.readline()
    
    seeds = [int(s) for s in text[7:].split(" ")]
    while (text != "seed-to-soil map:\n"):
        text = f.readline()
    for i in range(7):
        text = f.readline()
        while (len(text) != 0 and text != "\n"):
            dest_start, source_start, range_len = [int(s) for s in text.split(" ")]
            maps[i].append((source_start, dest_start, range_len))
            text = f.readline()
        f.readline()
        maps[i] = sorted(maps[i])
        
locations = []
seed_ranges = []
visited_seeds = set()
for i in range(0, len(seeds), 2):
    start = seeds[i]
    r_len = seeds[i+1]
    seed_ranges.append(range(start, start + r_len))
for rang in seed_ranges:
    for seed in rang:
        if seed in visited_seeds:
            continue
        visited_seeds.add(seed)
        dest = seed
        for map in maps:
            dest = binary_search(dest, map)
        locations.append(dest)

print(min(locations))