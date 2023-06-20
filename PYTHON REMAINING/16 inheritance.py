class employee:
    company="Visa"
class freelancer:
    company="Fiverr"
class programmer(freelancer,employee ):
    name="Rohit"
p=programmer()
print(p.name)
print(p.company)