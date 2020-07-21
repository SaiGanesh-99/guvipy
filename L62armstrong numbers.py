#armstrong numbers
for i in range(10001):
    num=i
    result=0
    n=len(str(i))       #we cant find ;length of numbers thats y changing thatinto string
    while (i!=0):
        digit=i%10
        result = result+digit**n
        i=i//10
    if num == result:
        print(num)
       
