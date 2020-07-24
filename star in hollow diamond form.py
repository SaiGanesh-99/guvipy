for row in range(5):
    for col in range(5):
        if (col==2 and row==0):
            print("*",end="")
        elif row==1 and (col==1 or col==3):
            print("*",end="")
        elif row==2 and (col==0 or col==4):
            print("*",end="")
        elif row==3 and (col==1 or col==3):
            print("*",end="")
        elif (row==4 and col==2):
            print("*",end="")
        else:
            print (end=" ")
    print()
#my own code 
