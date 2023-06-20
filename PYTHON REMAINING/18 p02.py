import random
RN=random.randint(1,100) # It will generate a random number between 1 and 100
UserGuess=None
i=1
while (UserGuess!=RN):
    UserGuess=int(input("Enter Your Guess"))
    if(UserGuess<RN):
        print("Large Number Please")
    elif(UserGuess>RN):
        print("Small Number Please")
    else:
        print("You Guessed it correctly")
        print(f"You Guessed it in {i} attemps")
    i+=1
with open("highscore.txt","r") as f:
    hiscore=int(f.read())
if(i<hiscore):
    print("You have broken the record")
    with open("highscore.txt","w") as f:
        f.write(str(i-1))
