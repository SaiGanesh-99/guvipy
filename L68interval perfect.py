interval1= int(input("enter the lower limit"))
interval2=int(input("enter the higher limit:"))
for num in range(interval1,interval2+1):
    result=0
    for i in range(1,num):
        if num%i==0:
            result=result+i
    if num==result:
        print(num)
