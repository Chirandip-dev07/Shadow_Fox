import random

# Number of times to roll the die
num_rolls = 20

# Initialize counters
count_6 = 0
count_1 = 0
count_two_6s_in_a_row = 0

# Previous roll (initialize to None)
previous_roll = None

# Simulate rolling the die
for _ in range(num_rolls):
    roll = random.randint(1, 6)
    
    # Count the roll of 6 and 1
    if roll == 6:
        count_6 += 1
    if roll == 1:
        count_1 += 1
    
    # Check for two 6s in a row
    if roll == 6 and previous_roll == 6:
        count_two_6s_in_a_row += 1
    
    # Update the previous roll
    previous_roll = roll

# Print the results
print(f"Number of times 6 was rolled: {count_6}")
print(f"Number of times 1 was rolled: {count_1}")
print("Number of times two 6s were rolled consecutively:",count_two_6s_in_a_row)
