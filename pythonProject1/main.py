userCountry = input("Where are you from?")
userName: str = input("What is your name?")


if userCountry == "colombia":
    print("I am from colombia too")
    userCity = input("What city are  from?")
    if userCity == "cali" or userCity == "cartagena":
        print("Wow! I was born and raised there")
        familyLastName = input("What is your family last name")
        if familyLastName == "montano" or familyLastName == "sevillano":
            print("Omg! That is my family last name!!")
            grandParents = input("Which are your grandparents name?")
            if grandParents == "clemencia" or grandParents == "alfonso":
                print("omg! We are  relatives")
    else:
        print("I am happy we are from the same country")
else:
    print("Welcome to san Francisco " + userName)

