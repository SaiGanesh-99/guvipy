# * in diamond form
def pyramid(rows):
    for i in range(rows):
        print(" "*(rows-i-1)+"* "*(i+1))  #"* " the space near star to give space between stars
    for j in range(rows-1,0,-1):
        print(" "*(rows-j)+"* "*(j))
