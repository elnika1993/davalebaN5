x = (input("Enter name and sname: "))
m = (input("Enter age: "))
a = (input("Enter corona type:\n1 for Delta, 2 for Omicron, 3 for Deltacron: "))
t = float(input("Enter temperature: "))
z = {"1": "delta", "2": "omicron", "3": "deltacron"}


def corona():

    def stat():    #Covid passport (boloshi gamoitans sul)
        print("")
        print("Covid Passport:\nName,Sname:", x, "\nAge:", m, "\nTemperature:", t,
              "\nCovid Status: POSITIVE", "\nCarantin time: 2 weeks!")

    if a == "1" and t >= 36.5 and t <=37.5:
        print("You have", z["1"], "\nTemperature is normal! Stay home.")
        stat()
    elif a == "1" and t >= 37.6:
        print("You have", z["1"], "\nTemperature is NOT normal! Call 911.")
        stat()
    elif a == "2" and t >= 36.5 and t <= 37.5:
        print("You have", z["2"], "\nTemperature is normal! Stay home.")
        stat()
    elif a == "2" and t >= 37.6:
        print("You have", z["2"], "\nTemperature is NOT normal! Call 911.")
        stat()
    elif a == "3":
        print("deltacron does not exist! ")
    else:
        print("Enter corona type(1,2,3) and Temperature more accurate")

corona()
