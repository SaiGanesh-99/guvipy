#fibonacci series
n=int(input("enter the number of series:"))
first=0
second=1  #intializing 0,1,1,2,3,5,8,13,21
for i in range(n):
    print(first)
    temp=first
    first=second
    second = temp+second
