red = 12
green = 13
blue = 14
total = 0


# INPUT : Dicitonary with color as key and count of that color as value; Known counts of each color
# OUTPUT: Returns True iff every color's count is less than or equal to the inputted counts
#         else returns false
def check_valid_game(dict, red, green, blue):
    for color in dict:
        if dict[color] > eval(color):
            return False
    return True


# INPUT : A dict represent a single pull and 3 lists that contain the number of red, blue, and green cubes drawn that pull
# OUTPUT: None; however, lists will be updated due to mutability
def add_counts(dict, reds, blues, greens):
    for color in dict:
        eval(color + "s").append(dict[color])

with open("games.txt", 'r') as f:
    games = f.readlines()

for game in games:
    game_id = int(game[5:game.find(":")])
    game = game[game.find(":") + 1:]
    reds = []
    blues = []
    greens = []

    # Splits up the pulls for each game
    pulls = [st.strip() for st in game.split(';')]
    for pull in pulls:
        
        # Dictionary with colors as key and count as value
        color_count = {entry[entry.find(" ") + 1:] : int(entry[:entry.find(" ")]) for entry in [s.strip() for s in pull.split(",")]}
        
        # if not check_valid_game(color_count, red, green, blue):
        #     break
        add_counts(color_count, reds, blues, greens)
    # else:
        # total += game_id
    prod = max(reds) * max(blues) * max(greens)
    total += prod
        
print(total)
