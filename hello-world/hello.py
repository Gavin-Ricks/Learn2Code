#importing directories
import os

#testing Global Variables
xteen = 142
#Clearing Screen
os.system('clear')



#Initializing directory Firstime
def hello(name, age):
    xteen = 12
    print("Hello", name + ", to your doom!")
    if age < 18:
        print("Sorry Creep, ur older than be so i dont like you")
    else:
        print("Prepare for doom and despair! Today's a bad day to be a lil kid!")
    print(xteen)

def main():
    age = int(input("What is your age? "))
    name  = input("What is your name?").strip()

    #printing weakahhglobals
    print(xteen)

    #Calling hello
    hello(name,age)

main()