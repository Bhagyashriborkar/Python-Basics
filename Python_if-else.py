a = 58
b = 78
if a > b:
    print("a is greater than b")

n = int(input('Enter a number to check:'))
if n%2 == 0:
    print("Number is even.")
if n % 2 !=0:
    print("Number is odd.")
if n==0:
    print("Number is  neither even or odd .rather you entered zero.")

a = int(input("Enter  the value of a :"));
b = int(input("Enter the value of b :"));
c = int(input("Enter the value of c :"));
if a > b and a > c:
    print("a is largest input.")
if b > a and b > c:
    print("b is  largest input.")
if c > a and c > b:
    print("c is  largest input.")

#If Else
m = 700
n = 675
if m > n:
    print("m is greater than n.")
else:
    print("m is not greater than n.")

age = int (input("Enter your age? "))  
if age>=18:  
    print("You are eligible to vote !!");  
else:  
    print("Sorry! you have to wait !!");

#If Elif Else
x = 3
if x == 1:
    print('x is one')
elif x == 2:
    print('x is two')
elif x == 3:
    print('x is three')
else:
    print('x is not found')

# Check whether the inptted number is 30, 40 or 50. 

number = int(input("Enter the number?  "))  

if number==30:  
    print("The number you entered is: 30 ")  
elif number==40:  
    print("The number you entered is: 40") 
elif number==50:  
    print("The number you entered is: 50")
else:  
    print(" You have entered a random number other than 30, 40 and 50.")  


marks = int(input("Enter the marks? "))  

if marks > 85 and marks <= 100:  
   print("Congrats ! you scored grade A ...")  
elif marks > 60 and marks <= 85:  
   print("You scored grade B + ...")  
elif marks > 40 and marks <= 60:  
   print("You scored grade B ...")  
elif (marks > 30 and marks <= 40):  
   print("You scored grade C ...")  
else:  
   print("Sorry you are fail !!")  

#Nested IF
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")
