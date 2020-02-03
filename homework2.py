import random

moove = 0
choice = ["W", "N", "E", "S"]
f1 = random.choice(choice)
f2 = random.choice(choice)
f3 = random.choice(choice)
f4 = random.choice(choice)
f5 = random.choice(choice)
f6 = random.choice(choice)
life = 3
while life > 0:
    moove += 1
    way = input("your in the magical maze, which way do you go first, W,N,E or S ?")
    if way == f1:
        way = input("you took the good way which way do you go secondly ?")
        if way == f2:
            way = input("you took the good way which way do you go then ?")
            if way == f3:
                way = input("you took the good way again which way do you go then ?")
                if way == f4:
                    way = input("once more you took the good way ! which way do you go then ?")
                    if way == f5 :
                        way = input("you are now near the end, which way do you go then ?")
                        if way == f6:
                            print("congratulation you escape to the magical maze which were a metaphor of your "
                                  "drug addiction. "
                                  "you use", moove, "moove and have", life,"life left !")
                            break
    print ("\nwrong way, you go back at the begging and lost a bit of your energies")
    if moove%5 == 0:
        life -= 1
        print(" \nyou lost a life, you have",life,"life left")
        if life == 0:
            print ("""
            you have lost all your life, you succumb to craziness and will stay forever in the magical maze."
                   
            game over""")
