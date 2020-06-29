y=0
x=7
while y<=100:
    z=int(input("Guess the Number!"))
    if z>=8:
        print("Too High")
        y=y+1
    elif z==7:
        y=y+100
    elif z<=7:
        print("Too Low")
        y=y+1
print("Well Done You Guessed Correct")
