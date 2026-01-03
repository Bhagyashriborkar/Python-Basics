#Arithmatic Operators
num1 = 6
num2 = 2
print(num1,num2)
print(type(num1),type(num2))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(4 ** 2)

print(9 // 3)
print(8 // 3)
print(7 // 3)
print(6 // 3)

print(9 % 3)
print(8 % 3)
print(7 % 3)
print(6 % 3)

print(5 * 4 + 1)          
print(1 + 5 * 4)           
print(5 * (4 + 1) ) 

#Comparison Operators

print(2 == 2)
print(3 == 1)
print(3 != 2)
 
print(3 > 2)
print(3 < 2)
 
print(3 >= 3)
print(3 >= 2)
 
print(3 <= 2)

#Assignment Operator

num = 5
print(num)
num += 1
print(num)

num = 9
print(num)
num -= 1
print(num)

num = 5
print(num)
num *= 2
print(num)

num = 9
print(num)
num /= 2
print(num)

#Logical Operators

print(True and True)
print(True and False)
print(False & False)

print(not True)
print(not False)

x = 9
print(x > 5 and x < 2)
print(x > 10 or x < 11)
print(not(x > 10 and x < 11))

#Some functions related to int and float

print(abs(-2))
print(abs(-2.1))
print(round(3.45))
print(round(-3.95))
print(round(3.46, 1))   
print(round(3.46, 2))  

print(round(3.469, 1))   
print(round(3.469, 2))   
new1 = 2.1
new2 = 0.3

print(new1 + new2)
print(new1 - new2)
fir = 3  
sec = 0.1  
print (fir + sec)
num1 = 'Hello'
num2 = '5'
print(num1 + num2)

#Type casting Integers

m = 4
n = 5
print(m,type(m))
print(n,type(n))
print('addtion =', m + n)
print()


m = int(m)
n = int(n)
print(m,type(m))
print(n,type(n))
print('addtion =', m + n)
print()

num = 2.0
print(type(num))
num = str(num)
print(type(num))
num = 'True'
print(type(num))
num = bool(num)
print(type(num))

num = input('enter some integer  -  ')   
print(num)
print(type(num))

num = input('Enter some number --- ')        
print(num, type(num))
new = int(num)          
print(new, type(new))

num1 = input('Enter first number:  ')
num2 = input('Enter second number:  ')
print(num1 + num2)    
print(int(num1) + int(num2))

X = 5
Y = 2
if(X > Y):
    print('Yes,X is greater  than Y')

if 9 > 5:
    print('four is greater than five')
else:
    print('four is smaller than five')

# multiple if else => use elif
 
height = 176
if height < 140:
    print('too short')
elif height < 180:
    print('height is ok')
else:
    print('too tall')


is_subscribed = False
if is_subscribed:              
    print('Thank you for the subscription!')  
else:
    print('Please subscribe')

# Nested If
 
x = 7
if x > 10:
    print('x is greater than 10')
    if x > 20:
        print('x is greater than 20')
        if x > 30:
            print('x is greater than 30')
        else:
            print('x is smaller than 30')
    else:
        print('x is smaller than 20')
else:
    print('x is smaller than 10')

x= 3
y = 4
 
if x < y and x + y > 5:
    print('both statements are true')
 
if x < y or x > y:
    print('one of the statement is true')
 
if x < y and not x + y < 5:
    print('both the statements must be true')  
