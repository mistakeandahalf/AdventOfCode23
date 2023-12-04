# Obtain the input and put it into a list
with open("input.txt", 'r') as f:
    cards = f.readlines()
    
# First number occurs at index 10
# First | occurs at index 40

# Total number of points
total = 0

# List keeps track of the number of copies for a given card
# Card i has number of copies at index i - 1
num_of_copies = [1 for i in range(len(cards))]

for i in range(len(cards)):
    # Generates sets using a set comprehension
    winning_numbers = {int(c) for c in cards[i][10:40].split(" ") if c != ""}
    nums = {int(c) for c in cards[i][41:].split(" ") if c != ""}
    
    # Matches is given by the intersection of the set of winning numbers with the set of numbers you got
    number_of_matches = len(winning_numbers.intersection(nums))
    
    # if number of matches is greater than 0, then 2^(number_of_matches - 1) points won
    if number_of_matches > 0:
        total += (2 ** (number_of_matches - 1)) 
        
    # For every match, we add one copy to each card starting from i+1 
    for j in range(1, number_of_matches + 1):
        if (i + j >= len(cards)):
            break
        
        # Need to add 1 for every copy of card i
        # 1 * num_of_copies[i] = num_of_copies[i]
        num_of_copies[i + j] += num_of_copies[i]
        
print(f"Total: {total}")
print(f"Number of cards: {sum(num_of_copies)}")