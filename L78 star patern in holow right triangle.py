#printing star in hollow riht angle triangle
n=int(input("entr no of rows"))
for row in range(n):
    for col in range(n):
        if row==n-1 or col==0 or row==col:
            print("*",end="")
        else:
            print(end=" ")
    print()
  
