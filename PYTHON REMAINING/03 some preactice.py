name=input("Please enter your good name \n")
date=input("Please enter the date\n")
# print("Dear ",name,",\n","\t\tYou are Selected!\n\t\t",date)
print("Dear "+name+",\n"+"\t\tYou are Selected!\n\t\t"+date)

letter='''Dear <|Name|>,
Greetings from ABC COMPANY. You are selected!
Date: <|Date|>'''
name=input("Please enter your good name \n")
date=input("Please enter the date\n")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)
print(letter)

l1=[1,22,5,3,23]
l1.sort()
print(l1)
l2=l1.reverse()
print(l2)
t=(1,2,3,1,2,3,1,2,3,5)
print(t.count(1))
print(t.index(1))