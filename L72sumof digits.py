#sum of digits
n=int(input("enter:"))
result=0
while n>0:
    digit=n%10
    result=result+digit
    n=n//10
print("sum is:",result)
