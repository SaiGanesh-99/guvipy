# prime numbers b/w the interval
interval1=int(input("enter the first interval:"))
interval2=int(input("enter the second interval:"))
for num in range(interval1,interval2+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
