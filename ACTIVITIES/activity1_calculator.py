import math as m

# Operations
def sum(n1, n2):
   n3 = n1 + n2
   return decimal(n3)
def minus(n1, n2):
   n3 = n1 - n2
   return decimal(n3)
def multiply(n1, n2):
   n3 = n1 * n2
   return decimal(n3)
def divide(n1, n2):
   n3 = n1 / n2
   return decimal(n3)
def root(n1):
   n3 = m.sqrt(n1)
   return decimal(n3)
def sin(n1):
   n3 = m.sin(n1)
   return decimal(n3)
def cos(n1):
   n3 = m.cos(n1)
   return decimal(n3)
def tan(n1):
   n3 = m.tan(n1)
   return decimal(n3)
def log(n1):
   n3 = m.log(n1)
   return decimal(n3)

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
x = str(input("WELCOME TO YOUR CALCULATOR\nA - Sum\nB - Minus\nC - Multply\nD - Divide\nE - Square root\nF - Sen\nG - Cose\nH - Tan\nI - Log\nJ - Exit\nOption: ")).upper()
while x != 'J':
   while x > 'J' or x.isdigit() == True or isfloat(x) == True or len(x) != 1:
       x = str(input("Error, introduce the option again: ").upper())

   n1 = str(input("First value: "))
   while n1.isdigit() == False and isfloat(n1) == False:
       n1 = str(input("Error, introduce the first value again: "))
   n1 = float(n1)

   if x < 'E':
       n2 = str(input("Second value: "))
       while n2.isdigit() == False and isfloat(n1) == False:
           n2 = str(input("Error, introduce the second value again: "))
       n2 = float(n2)


   if x == 'A':
       print("Result:", sum(n1, n2))
   elif x == 'B':
       print("Result:", minus(n1, n2))
   elif x == 'C':
       print("Result:", multiply(n1, n2))
   elif x == 'D':
       print("Result:", divide(n1, n2))
   elif x == 'E':
       print("Result:", root(n1))
   elif x == 'F':
       print("Result:", sin(n1))
   elif x == 'G':
       print("Result:", cos(n1))
   elif x == 'H':
       print("Result:", tan(n1))
   else:
       print("Result:", log(n1))


   x = str(input("Do you want to initiate the calculator again? (Y/N) ").upper())
   while x != "Y" and x != "N":
       x = str(input("Error, introduce the option again (Y/N) ").upper())
   if x == "Y":
       x = str(input("WELCOME TO YOUR CALCULATOR\nA - Sum\nB - Minus\nC - Multply\nD - Divide\nE - Square root\nF - Sen\nG - Cose\nH - Tan\nI - Log\nJ - Exit\nOption: ")).upper()
   else:
       break
print("Bye")
