for i in range(2,21):
    for j in range(1,11):
        t1=i*j
    with open(f"tableOf{i}.txt","a") as f:
      f.write(str(t1))

# Actual Code
for i in range(2,21):
    with open(f"table_of_{i}.txt","w") as f:
        for j in range(1,11):
            f.write(f"{i}x{j}={i*j}\n")