def Hello():
    print('Hello world')
Hello()
Hello()
def hello(name):
    print(f' hello{name}')
hello('megha')
hello(234)
print(type(hello))

def addthis(first,second):
    print(first+second)
addthis(45,48)

def hello_you(name):
    print(f'hello{name.upper}')
    print(hello_you('studens'))

def hi(name):    
    message = "Hi "+name  
    return message  

name = input("Enter the name:")    
print(hi(name))

def add():  
    a = 40  
    b = 30  
    c = a+b  
    return c  

print("The sum is:", add())

def add(a,b):  
    return a+b; 

a = int(input("Enter a: "))    
b = int(input("Enter b: "))    
    
print("Sum = ",add(a,b)) 


p = int(input("Enter the principle amount? "))    
r = float(input("Enter the rate of interest? "))  
t = float(input("Enter the time in years?"))    

def simple_interest(p,t,r):    
    return (p*t*r)/100    

  
print("Simple Interest: ",simple_interest(p,r,t))  

def find_distance(speed, time):        
    print(speed, time)
    return speed * time
d = find_distance(speed=10, time=3)    
print(d)

d = find_distance(time=3, speed=10)     
print(d)

d = find_distance(3,10)     
print(d)