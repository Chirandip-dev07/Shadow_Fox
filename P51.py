import random

num_rolls = 25

count_6 = 0
count_1 = 0
count_two_6s_in_a_row = 0
previous_roll = None

for i in range(num_rolls):
    roll = random.randint(1, 6)
    
    if roll == 6:
        count_6 += 1
    if roll == 1:
        count_1 += 1
    if roll == 6 and previous_roll == 6:
        count_two_6s_in_a_row += 1
        
    previous_roll = roll

print("Number of times 6 was rolled:"count_6)
print("Number of times 1 was rolled:"count_1)
print("Number of times two 6s were rolled consecutively:",count_two_6s_in_a_row)
