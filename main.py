import random

user_level = input("Enter your level: ")

min_range = int(input("Enter your min range: "))

# max_range: int

if (user_level == "Easy"):
    max_range = int(input("Enter max range: "))

easy_chances = 5
medium_chances = 3
hard_chances = 2



match(user_level):
    case "Easy":
        random_num = random.randint(min_range, max_range)
        print("random_num: ", random_num )
        chance = 1
        while(chance <= 5):
            guessed_num = int(input("Enter guess number: "))    
            print(f"Chance remaining: {chance - 5}")     
            if (guessed_num == random_num):
                print("You guess right")
                chance = 6
            else:
                print("You did not guess right")
                chance = chance + 1


    case "Medium":
        random_num = random.randint(min_range, 200)
        print("random_num: ", random_num )
        chance = 1
        while(chance <= 3):

            guessed_num = int(input("Enter guess number: "))         
            print(f"Chance remaining: {chance}")     
            
            if (guessed_num == random_num):
                print("You guess right")
                chance = 4

            else:
                print("You did not guess right")
                chance = chance + 1

    case "Hard":
        random_num = random.randint(min_range, 200)
        print("random_num: ", random_num )
        chance = 1
        while(chance <= 2):

            guessed_num = int(input("Enter guess number: "))         
            print(f"Chance remaining: {chance}")     
            
            if (guessed_num == random_num):
                print("You guess right")
                chance = 3
            else:
                print("You did not guess right")
                chance = chance + 1