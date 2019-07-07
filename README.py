#is it possible to pause program for invalid input?
#request input from the user(sex)
def male_or_female():
    x = input("Are you male or female?\n")
    if x == "male":
        return x
    elif x == "female":
        return x
    else:
        return "select male or female!\n"
#request input from the user(age)
def how_old():
    y = input("How old are you?\n")
    return y
#concat
def concat():
    a = male_or_female()
    b = how_old()
    print("you are " + a + " and " + b + " years old.")


def main():
    concat()

if __name__ == "__main__":
        main()
