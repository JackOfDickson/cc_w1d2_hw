# For the following list of numbers:

from unittest import skip


numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

# 2. Print the difference between the largest and smallest value:
print(max(numbers) - min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.
prev_val = 0

for current_val in numbers:
    if current_val == prev_val:
        print(True)
        break
    else:
        prev_val = current_val
        print("no consecutive repeats here")

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
q4_sum = 0
event_occur_q4 = False
for number in numbers:
    if number == 6:
        event_occur_q4 = True
    elif event_occur_q4 == False:
        q4_sum += number
    elif number == 7:
            event_occur_q4 = False

print(q4_sum)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

q5_sum = 0
event_occur_q5 = False
for number in numbers:
    if number == 13:
        event_occur_q5 = True
    elif event_occur_q5 == False:
        q5_sum += number
    elif number != 13:
            event_occur_q5 = False

print(q5_sum)




