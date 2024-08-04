jumping_jacks = 0

while jumping_jacks<100:
    print(100-jumping_jacks,"jumping jacks are left")
    response = input("Are you tired? :")
    if response in ['yes', 'y']:
        ask = input("Do you want to skip the remaining sets? :")
        if ask in ['yes', 'y']:
            print("You completed a total of",jumping_jacks,"jumping jacks.")
            break
    jumping_jacks += 10       

if jumping_jacks==100:
    print("Congratulations! You completed the workout")