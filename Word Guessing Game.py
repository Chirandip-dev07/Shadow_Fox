import random

print("WELCOME TO THE HANGMAN GAME AKA WORD GUESSING GAME")
print("ONLY 1 LETTER OF THE WORD WILL BE SHOWN INITIALLY AND MORE LETTERS WILL BE SHOWN AS HINTS AS U GUESS IT INCORRECTLY")
print("YOU HAVE CHANCES TO GUESS THE WORD TILL THE EMPTY SPACES IS 2")
print("AFTER THAT ITS A DEFEAT FOR YOU")
print("TYPE YOUR GUESS IN SMALL LETTERS ONLY")
print("GOOD LUCK, GUESS IT AS FAST AS YOU CAN")

words = [ ]
with open("C:\\Users\\Chirandip\\OneDrive\\Desktop\\Words.txt","r") as f:
    for line in f:
        words.append(line.strip())
f.close()


Chosen_Word = random.choice(words) 
Chosen_Letters = list(Chosen_Word)
Chosen_Length = len(Chosen_Letters)
n = Chosen_Length
print()
print("Your word has",Chosen_Length,"letters")
print("THE WORD IS......")
print()

list1 = []
for j in range(0,n):
    list1.append(j)

def print_word(list):
    num1 = random.choice(list)
    list = [x for x in list if x!=num1]

    for i in range(0,n):
        if i==num1 or i not in list:
            print(Chosen_Letters[i],end="")
        else:        
            print("_", end="")
    return list
count=0
while Chosen_Length>2:
    list1 = print_word(list1)
    print()
    print()
    Guessed_Word = input("Enter : ") 
    Guessed_Letters = list(Guessed_Word)
    if Guessed_Letters==Chosen_Letters:
        print()
        print("EXCELLENT")
        count = count+1
        break
    else:
        if len(list1)>=3:
            print("Lets give you more hint")
        print()
    Chosen_Length = Chosen_Length-1

if count==0:
    print("Failure")
    print("Your word was",Chosen_Word)

print()
print("THANKS FOR PLAYING THE GAME")
print("HOPE YOU LIKED IT")