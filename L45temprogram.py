#temp display program using list
temps=[100,90,80,89,85,97,79]
day=input("enter'sunday','monday','tuesday','thursday','friday' ,'saturday':")
if day=="sunday":
    temperature=temps[0]
elif day=="monday":
    temperature=temps[1]
elif day=="tuesday":
    temperature=temps[2]
elif day=="wednesday":
    temperature=temps[3]
elif day=="thursday":
    temperature=temps[4]
elif day=="friday":
    temperature=temps[5]
elif day=="satuday":
    temperature=temps[6]
else:
    print("wrong input")
print(" On ",day,"the tempurature is ",temperature)
