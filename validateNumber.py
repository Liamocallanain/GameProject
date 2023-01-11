validNum=False
num=int(input("Please input a number between 1 and 10"))
while not validNum:
    if num>=1 and num<=10:
        validNum=True
    else:
        print("Please enter a valid number")
            
print("Your number is valid")
    