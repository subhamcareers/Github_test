#fucntion with return value

def food(f):
    tip=0.1*f
    f=f+tip
    fperson=f/num
    return fperson
def movie(m):
    return m/num

num=int(input("No.of Friends: "))
ftotal=int(input("Spent on Food:"))
mtotal=int(input("Spent on Movie: "))

x=food(ftotal)
y=movie(mtotal)
print("The Per person is : ",x+y)
