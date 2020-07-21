#swapping without variable
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print("before swapping")
print(a)
print(b)
a=a+b
b=a-b
a=a-b
print("after swapping:")
print(a)
print(b)
