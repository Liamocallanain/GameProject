yesNoValid=False
while not yesNoValid:
    yesNO=input("Enter your answer y/n")
    if yesNO in ["y","Y","n","N","Yes","No"]:
        yesNoValid=True
    else:
        yesNoValid=False
        
print("Thank you for your valid input")

