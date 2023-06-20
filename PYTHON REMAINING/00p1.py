class Programmer:
    company="Microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
        print(f"{self.name} and {self.company} and {self.product}")
harry=Programmer("Harry","Skype")
alka=Programmer("Alka","Github")

# Calculator by class
class Calculator:
    def __init__(self,num):
        self.number=num ## either ek alag function banakar, fir usee call karke forign value to store karao then class ki anya
        # operations ko us par perform karao ya to constructor ke variable me store karaa do jo bina explicitily call kiye value ko store kar lea hai.
    def square(self):
        print(f"{self.number**2}")
a=Calculator(int(input()))
a.square()

class Sample:
    @staticmethod
    def __init__(name):
        print("My name is",name)
obj=Sample("harry")
print(obj.name)