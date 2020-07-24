n=int(input("enter the no of rows:"))
for row in range(n):
    for col in range(n):
        if row==col or row==0 or col==(n-1):
            print("*",end="")
        else:
            print(end=" ")
    print()
 
