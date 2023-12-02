
# Input: String with at least one digit
# Output: A two digit integer with the first digit (or word corresponding to a digit, e.g. "one" -> 1) 
# from the left concatenated with the first digit from the right
# Ex: get_calibration_value("1abc2") --> 12
# Ex: get_calibration_value("one3four") --> 14

def get_calibration_value(s):
    digits = "0123456789"
    word_digits = {
        "one"   : "1",
        "two"   : "2",
        "three" : "3",
        "four"  : "4",
        "five"  : "5",
        "six"   : "6",
        "seven" : "7",
        "eight" : "8",
        "nine"  : "9"
    }
    
    # List to contain tuples with an index as the first element and
    # the number (as a string) at that index in the second element
    # List can easily be sorted by index to get first number from left
    # and first number from right
    indicies_and_numbers = []
    
    # Finds the first numerical digits from the left and right
    left_pointer = 0               # First index of string
    right_pointer = len(s) - 1     # Last index of string
    
    while (s[left_pointer] not in digits):
        left_pointer += 1
        if (left_pointer >= len(s)):
            break
    else:
        indicies_and_numbers.append((left_pointer, s[left_pointer]))
        
    while (s[right_pointer] not in digits):
        right_pointer -= 1
        if (right_pointer < 0):
            break
    else:
        indicies_and_numbers.append((right_pointer, s[right_pointer]))
        
    # Finds the first word digits from the left and right
    for digit in word_digits:
        i = s.find(digit)
        if i != -1:
            indicies_and_numbers.append((i, word_digits[digit]))
            
    for digit in word_digits:
        i = s.rfind(digit)
        if i != -1:
            indicies_and_numbers.append((i, word_digits[digit]))
    
    
    indicies_and_numbers.sort()
    return int(indicies_and_numbers[0][1] + indicies_and_numbers[-1][1])


sum = 0
with open("text.txt") as f:
    while (True):
        line = f.readline()
        if (len(line) == 0):
            break
        sum += get_calibration_value(line)

print(sum)
