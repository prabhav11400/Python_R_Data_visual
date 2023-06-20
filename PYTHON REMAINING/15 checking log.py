with open("log.txt") as f:
    content=f.read()

if 'python' in content.lower(): # check karte samay all words lower me chale gaye
    print("Yes, python ispresent in the long log file")
else:
    print("No, Python is not present")

# reading lines number where python is present
content=True
i=1
with open("log.txt") as f:
    while content:
        content=f.readline()
        if 'python' in content.lower():
         print(content)
         print(f"Yes, Python is present in line number{i}")
        i+=1

