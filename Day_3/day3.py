# Returns true iff adjacent to a symbol (not including .)
# Adjacency includes diagonals
def is_adjacent_to_symbol(schematic, line_index, start, end):
    symbols = "!@#$%^&*()/?\|-+=_[]\{\}~`<>,'\";:"
    
    # Left of number
    if start != 0:
        if schematic[line_index][start - 1] in symbols:
            return True
        
    # Right of number
    if end != len(schematic[line_index]):
        if schematic[line_index][end] in symbols:
            return True
        
    # Above numbers
    if line_index != 0:
        for i in range(end - start):
            if schematic[line_index - 1][start + i] in symbols:
                return True
    
    # Below numbers
    if line_index != len(schematic) - 1:
        for i in range(end - start):
            if schematic[line_index + 1][start + i] in symbols:
                return True

    # Upper left diagonal
    if start != 0 and line_index != 0:
        if schematic[line_index - 1][start - 1] in symbols:
            return True

    # Lower left diagonal
    if start != 0 and line_index != len(schematic) - 1:
        if schematic[line_index + 1][start - 1] in symbols:
            return True
        
    # Upper right diagonal
    if end != len(schematic[line_index]) and line_index != 0:
        if schematic[line_index - 1][end] in symbols:
            return True
    
    # Lower right diagonal
    if end != len(schematic[line_index]) and line_index != len(schematic) - 1:
        if schematic[line_index + 1][end] in symbols:
            return True
        
    return False 

# Returns a list of tuples containing the starting index of a number (inclusive)
# and the ending index of that number (exclusive)
def find_numbers(schematic, line_index):
    i = 0
    ret = []
    while True:
        while (i < len(schematic[line_index]) and schematic[line_index][i] not in '0123456789'):
            i += 1
        if i == len(schematic[line_index]):
            break
        start = i
        while (i < len(schematic[line_index]) and schematic[line_index][i] in '0123456789'):
            i += 1
        end = i
        ret.append((start, end))
    return ret


# Returns a list of tuples corresponding to line index and ranges of the indicies of numbers
# adjacent to the character at schematic[line_index][char_index]
def find_adjacent_numbers(schematic, line_index, char_index):
    above = []
    below = []
    curr = find_numbers(schematic, line_index)
    ret = set()
    for i, j in curr:
        if char_index != 0:
            if char_index - 1 in range(i, j):
                ret.add((line_index, i, j))
        if char_index != len(schematic[line_index]) - 1:
            if char_index + 1 in range(i, j):
                ret.add((line_index, i, j))
    
    if line_index != 0:
        above = find_numbers(schematic, line_index - 1)
    
    for i, j in above:
        if char_index != 0:
            if char_index - 1 in range(i, j):
                ret.add((line_index - 1, i, j))
        if char_index in range(i,j):
            ret.add((line_index - 1, i, j))
        if char_index != len(schematic[line_index]) - 1:
            if char_index + 1 in range(i, j):
                ret.add((line_index - 1, i, j))
    
    if line_index != len(schematic) - 1:
        below = find_numbers(schematic, line_index + 1)
        
    for i, j in below:
        if char_index != 0:
            if char_index - 1 in range(i, j):
                ret.add((line_index + 1, i, j))
        if char_index in range(i,j):
            ret.add((line_index + 1, i, j))
        if char_index != len(schematic[line_index]) - 1:
            if char_index + 1 in range(i, j):
                ret.add((line_index + 1, i, j))
    return list(ret)
    
# Returns a dictionary with a * coordinate (line_index, and char index) as key, and a list of tuples
# corresponding to the start and end of a number as value
def find_numbers_adjacent_star(schematic, line_index):
    ret = {}
    i = 0
    line = schematic[line_index]
    while True:
        while (i < len(line) and line[i] != '*'):
            i += 1
        if i == len(line):
            break
        ret[(line_index, i)] = find_adjacent_numbers(schematic, line_index, i)
        i += 1
    return ret

# Get list of lines in the schematic
with open("engine_schematic.txt", 'r') as f:
    schematic = f.readlines()
    


gear_ratio = 0
engine_part = 0

# Find a number in each line of the schematic
# If adjacent to a symbol (not including .), add it to sum
# To check adjacency, need to keep track of 2 things:
#   1) Start and end indicies
#   2) Which line we are on

for line_index in range(len(schematic)):
    numbers = find_numbers(schematic, line_index)
    for start, end in numbers:
        if is_adjacent_to_symbol(schematic, line_index, start, end):
            engine_part += int(schematic[line_index][start:end])

print(f"Engine part: {engine_part}")

# Find each star in each row
# If a star has exactly two numbers adjacent to them
# Add their product to gear_ratio
for line_index in range(len(schematic)):
    nums_adj_star = find_numbers_adjacent_star(schematic, line_index)
    for coord_list in nums_adj_star.values():
        if len(coord_list) == 2:
            prod = 1
            for i, start, end in coord_list:
                prod *= int(schematic[i][start:end])
            gear_ratio += prod

print(f"Gear ratio: {gear_ratio}")