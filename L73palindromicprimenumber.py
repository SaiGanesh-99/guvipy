#pallindromic prime number
interval1=int(input("enter the lower limt:"))
interval2=int(input("enter the higher limit:"))
for num in range(interval1,interval2+1):
    reverse=int(str(num)[::-1])
    if num==reverse:
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                print(num)
