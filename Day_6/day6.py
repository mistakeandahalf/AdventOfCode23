def howManyWaysToWin(time, record):
    # Due to symmetry, we are only checking for the distance traveled
    # When the button is held for 0 sec to t // 2 secs (inclusive)
    count = 0
    for speed in range(time // 2 + 1):
        remaining_time = time - speed
        if (remaining_time * speed) > record:
            count += 1
    count *= 2
    if time % 2 == 0: # If our given time is even, the middle value would've been double counted
        count -= 1
    return count

with open('input.txt', 'r') as f:
    time = [int(s) for s in f.readline()[5:].split(" ") if s != ""]
    record_distance = [int(s) for s in f.readline()[9:].split(" ") if s != ""]
    
# print(time)
# print(record_distance)

list_of_combinations = []
for i in range(4):
    t = time[i]
    record = record_distance[i]
    
    list_of_combinations.append(howManyWaysToWin(t, record))
    

prod = 1
for num in list_of_combinations:
    prod *= num
print(prod)

new_time = ""
distance = ""
for i in range(4):
    new_time += str(time[i])
    distance += str(record_distance[i])
new_time = int(new_time)
distance = int(distance)

print(howManyWaysToWin(new_time, distance)) 