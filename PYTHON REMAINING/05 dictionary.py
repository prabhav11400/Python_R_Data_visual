MyDish={
    "Fast":"In a quick manner",
    "Harry" : "A Codder",
    "marks": [1,2,5],
    "MyDict":{"Aman":"Aman Singh",
    "Prabhav":"Prabhav Singh"},
    1:2 
    }
# print(MyDish["Fast"])
# print(MyDish["marks"])
# print(MyDish["MyDict"])
# print(MyDish["MyDict"]["Aman"])
# print(MyDish["MyDict"]["Prabhav"])
# print(MyDish.keys())
# print(MyDish.values())
# c=MyDish.values()
# print(c)
update_dict={
    "Aditya":"My Brother",
    "Shipra":"My Sister"
}
MyDish.update(update_dict)
print(MyDish)
print(MyDish["Shipra"])

MyDish.update({"Harry":"Fradia Person"})
print(MyDish["Harry"])

a={1,2,3}
# b={a,5,6}# not allowed
a.add(4)
print(a)
print(a.pop())
print(a)