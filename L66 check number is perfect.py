#to check it is a perfect number
#factor of 6 is 1,2,3 . 1+2+3=6 therfor it is a perfect number
num= int(input("enter a number:"))
result=0  #initialization
for i in range(1,num):
    if num%i==0:
        result= result+i
if result==num:
    print(num," is a perfect number")
else:
    print(num," is not a perfect number")
