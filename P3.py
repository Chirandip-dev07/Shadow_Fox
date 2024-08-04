justice_league = ["Superman","Batman","Wonder Woman","Flash","Aquaman","Green Lantern"]

#Calculation of members 
members = len(justice_league)
print("There are",members,"members in justice league ")

#Recruited new members
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(justice_league)

#Wonder Woman is the leader
leader = justice_league[2]
justice_league.pop(2)
justice_league.insert(0,leader)
print(justice_league)

#Resolving conflict
justice_league.pop(1)
justice_league.insert(3,"Superman")
print(justice_league)

#Justice league crisis
justice_league = ["Cyborg","Shazam","Hawkgirl","Martian Manhunter","Green Arrow"]
print(justice_league)

#Sorting the list
justice_league.sort()
print(justice_league)
print("The new leader is",justice_league[0])