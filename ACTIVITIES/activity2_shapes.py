import math as m

# Menu
def menu():
    x = str(input(
        "1 - Square\n2 - Triangle (max. value: 10)\n3 - Circle\n4 - Exit\nOption: "))
    while x > "4" or x < "1":
        x = str(input("Error, try again: "))
    return x

# Figures
def square(a, b):
    area = a * b
    perimeter = 2 * a + 2 * b
    print(b * "* ")
    for i in range(a - 2):
        print("*" + (b * 2 - 3) * " " + "*")
    print(b * "* ")
    return area, perimeter

def triangle(a, b):
    area = (a * b) / 2
    perimeter = a * 2 + b
    mig = int(b / 2) + 81
    space1 = int(b / 2)
    # Punt de dalt
    print(mig * " " + "*")
    # Part del mig
    for i in range(a - 2):
        print((mig - space1) * " " + "*" + (2 * space1 - 1) * " " + "*")
        space1 += int(b / 2)
    # Base
    m = 3
    n = 0
    while m <= a + 1 or m <= b + 1:
        if a <= m or b <= m:
            space2 = int(b / 2 + n)
            break
        m += 2
        n += 1
    base = mig - (a - 1) * (int(b / 2))
    print(base * " ", end="")
    for i in range(b):
        print("*" + " " * space2, end="")
    print()
    return decimal(area), perimeter

def circle(r):
    for i in range(int(-r), int(r + 1)):
        for j in range(int(-r), int(r + 1)):
            if m.sqrt(i ** 2 + j ** 2) < r:
                print("*", end="")
            else:
                print(" ", end="")
        print("")

    area = m.pi * r ** 2
    perimeter = 2 * m.pi * r
    return decimal(area), perimeter

# If it is a float
def isfloat(n1):
    try:
        float(n1)
        return True
    except ValueError:
        return False

# Transform the number to float or int to delete the .0
def decimal(n1):
    n1 = str(n1)
    pos = n1.find(".")
    if n1.find(".") == -1 or n1[pos + 1] == "0":
        n1 = float(n1)
        n1 = int(n1)
    elif n1[pos + 1] > "0":
        n1 = float(n1)
    else:
        try:
            new_n1 = n1[pos + 2]
            n1 = float(n1)
        except:
            n1 = float(n1)
            n1 = int(n1)
    return n1

# Main
x = menu()
cont_metre = 0

while x != "4":
    if x <= "3":
        if x == "3":
            r = str(input("Radius: "))
            while r.isdigit() == False and isfloat(r) == True:
                r = str(input("Error, wrong radius: "))
            r = int(r)
        else:
            a = str(input("Height: "))
            while a.isdigit() == False and isfloat(a) == True:
                a = str(input("Error, wrong height: "))
            a = int(a)
            b = str(input("Base: "))
            while b.isdigit() == False and isfloat(b) == True:
                b = str(input("Error, wrong base: "))
            b = int(b)

    if x == "1":
        area, perimeter = square(a, b)
        print("Area: {0} m²\nPerimeter: {1} m".format(area, perimeter))
        cont_metre += perimeter
    elif x == "2":
        area, perimeter = triangle(a, b)
        cont_metre += perimeter
        print("Area: {0} m²\nPerimeter: {1} m".format(area, perimeter))
    else:
        area, perimeter = circle(r)
        cont_metre += perimeter
        print("Area: {0:.2f} m²\nPerimeter: {1:.2f} m".format(area, perimeter))

    x = str(input("Do you want to change option? (Y/N) ").upper())
    while x != "Y" and x != "N":
        x = str(input("Error, try again (Y/N) ").upper())
    if x == "Y":
        x = menu()
    else:
        x = "4"

print("You have consumed a total of: {0} meters".format(cont_metre))
print("Bye")