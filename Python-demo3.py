#Tuple
courses = ('ba', 'bcom', 'bsc')
print(courses)
print(type(courses))     
print(courses[1])
print(courses.count('ba'))
print(courses.count('baa'))
print(courses.index('bsc'))

courses =('ba','bcom','bsc','bsc','ba')
print(type(courses))
print(courses.count('bsc'))
print(courses.index('bsc'))

for item in courses:
    print(item)

for id, item in enumerate(courses):    
  print(id, item)
print(len(courses))

nums = (3,5,6)
print(type(nums))

# Mix of str and int and bool is allowed in tuple

data = ('ba', 2, True, 'bsc')
print(data)
print(type(data))

# For the sake of it, let's check data type of each of the object

print(type(data[0]))
print(type(data[1]))
print(type(data[2]))

# Let's do the same with for loop
for item in data:
  print(item, type(item))

  print(('a','b','c')+(2,4,5))

  # More than two tuples can also be added the same way

new = ('50',)
new1 = ('apple',)
new2 = ('mango','orange')
print(new + new1 + new2)

# check whether an element is in the tuple

fruits = ('apple','mango')

print('mango' in fruits)     
print('mangoes' in fruits)

#  Algebraic operations like max, min etc

print(max(2, 1, 3, 7))
print(min(2, 1, 3, 7))

# To convert list into a tuple
num = [1, 2, 3, 4]
new = tuple(num)
print(num)
print(new)

# Just like list, you can use -1 to get the last element, and -2 to get second last element

num = (1, 2, 3, 4, 5, 6, 7)
print(num[-1])
print(num[-2])
print(num[6]) 

courses = ('ba', 'bcom', 'bsc', 'be', 'ma', 'mcom',' msc', 'me')
print(courses[3:5])   
print(courses[3:])   
print(courses[:3])
print(courses[-3:])

