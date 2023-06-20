import random
def game():
    score=random.randint(1,1000)
    return score

# score O vali file banao
f=open("Hiscore.txt","a")
f.write("Score in this attempt now 0")
f.close()
# updating the score(need not hiscore)
s=game()
f=open("Hiscore.txt","w")
f.write(f"Score till now {s}")
f.close()

# now hiscore update karne vali code.
import random 
def game():
    score=random.randint(1,100)
    return score

s=game()

with open("hiscore.txt","r") as f:
    hiscore=int(f.read())  # hamne hiscore.txt ke string jo ke number tha ko read krke integer me badal diya

if hiscore<s:
    with open("hiscore.txt","w") as f:
        f.write(str(s))  # s integer tha, jise string me badala since f.write string write krta hai, integer nhi

