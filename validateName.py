name=input("Enter your name")
def validateName(name):
    try:
        # Name should contain only letters
        if not name.isalpha():
            raise ValueError("Name can only contain letters.")

    except ValueError as e:
        print(e)
        return False
    else:
        return True


if validateName(name):
    print(f"{name} is a valid name.")
else:
    print(f"{name} is not a valid name.")


