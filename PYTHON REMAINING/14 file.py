# File ke content ko string me copy karna, taki modification ho sake by string methods.
with open("file.txt","r") as f:
    data=f.read()
# print(data)

#Replacing target word with the required word
new_data=data.replace("Donkey","#####")
# print(new_data)

# Now changing the old file with new tested and prepared file
with open("file.txt","w") as f:
    f.write(new_data)