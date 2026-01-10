courses = ['ba', 'bcom', 'bsc', 'be']

for course in courses:
    print(course)

fruits = ('apple', 'banana', 'mango')

for fruit in fruits:
    print(fruit)

company = {'name': 'Tesla', 'founder':'Elon', 'year': 2003}

for item in company:
    print(item, company[item])

text = 'Hello'
for i in text:
  print(i)

for i in range(5):   
  print(i)

print('------------')

for i in range(3,8):   
  print(i)


courses = ['ba', 'bcom', 'bsc', 'be']
for id, item in enumerate(courses):
  print(id, item)

courses = ['ba', 'bcom', 'bsc', 'be']

for i in range(len(courses)):               
  print(i, courses[i])
courses = ['ba', 'bcom', 'bsc', 'be']

for course in courses:
    if course == 'bcom':
        print(course)
    else:
        print('Course is NOT bcom')

courses = ['ba','bcom','be','bsc']
for item in courses:
   print(item)
   if item == 'bsc':
      break

courses = ['ba', 'bcom', 'bsc', 'be']
for item in courses:
  if item == 'bsc':               
    break                           
  print(item)   

  courses = ['ba','bcom','be','bsc']
  for item in courses:
   if item == 'bsc':
     continue
     print(courses)

name = input('enter your name --- ')
print("let's print characeter separately")
for char in name:
  print(char)

num = [1, 2, 3, 4, 5, 6, 7]
def sqr(item):
  return item * item

for i in num:
  print(i, sqr(i))

num = [10,30,23,43,65,12]  
sum = 0  
for i in num:  
    sum = sum + i     # or we can write sum += i
print("The sum is:",sum) 

num = int(input("Enter the number "))  
for i in range(1,11):  
    c = num * i  
    print(f"{num} x {i} ====> {c}") 

adj = ["red", "big", "tasty"] 
fruits = ["apple", "banana", "cherry"]  

for x in adj:
  for y in fruits:
    print(x, y)

for i in range(4): 
    for j in range(20, 24): 
        print(i, j)

rows = int(input("Enter the rows  :"))   
for i in range(0, rows+1):             
    for j in range(i):                   
        print("*", end='')        
    print()   


 
rows = int(input("Enter the rows : "))  
for i in range(0,rows+1):  

    for j in range(i):  
        print(i, end = '')  
    print()  


nums = [11,23,30,43]  
count = 0;  
for item in nums:  
    count = count + 1;
print("Total length - ",count);

nums = [11,23,30,43]  
count = 0;  
for item in nums:  
    count = count + 1;
    if item == 30:  
        print("item matched")  
        break
print("found at", count, "location");

letters = ['a', 'b', 'c', 'd', 'e']
for letter in letters:
    if letter == 'c':
        print('Found letter')
        break
    else:
        print(letter)
