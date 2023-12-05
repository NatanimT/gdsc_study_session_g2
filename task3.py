for i in range(100):
    print(f"{i:02d}, ", end="")
print()

for i in range(1000):
    print(f"{i:03d},",end="")
#prints 0 infront of any number less than 100 or 3 caracters
for i in range(100):
    print(f"{i:03d}, ",end="")
#prints 0 infront of any number less than 100 or 3 caracters
for i in range(100):
    prifix= "num: " if  i<100 else""    
    print(f"{prifix}{i:02d}, " , end="")
print()
for i in range(100):
    prifix= "num: " if  i<100 else""    
    print(f"{prifix}{i}, " , end="")
print()
for i in range(100):
    if i < 99:
        print(f"{i:02d}, ", end="")
    else:
        print(f"{i:02d}")

