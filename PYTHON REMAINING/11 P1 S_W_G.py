import random
print("Computer's turn: snake(s),water(w), gun(g) ")
randno=random.randint(1,3)
if randno==1:
    comp="s"
if randno==2:
    comp="w"
if randno==3:
    comp="g"

you=input("Your turn : snake(s),water(w), gun(g) ")

def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="w":
            return False
        elif you == "g":
            return True
    elif comp=="w":
        if you=="g":
            return False
        elif you=="s":
            return True
    elif comp=="g":
        if you=="w":
            return True
        elif you=="s":
            return False
    
a=gamewin(comp,you)

if a==None:
    print("The Game is tie")
elif a:
    print("You Won ")
else:
    print("Computer Won ")

print("BECAUSE ")
print(f"Computer chose {comp}")
print(f"You chose {you}")