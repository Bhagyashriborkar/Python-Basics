#Basic List Programs
Courses = ['bsc','bcs','msc','ma','bcom','ba']
print("Courses")
print(type(Courses))
print(Courses[1])
print(Courses[4])
print(Courses[:2])
print(Courses[2:])
print(Courses[-1])
print(Courses[:-2])
Courses.append('BE')
print(Courses)
Courses.insert(3,'ME')
print(Courses)
c = 'B.pharm'
Courses.append(c)
print(Courses)
new = ['11th','12th']
Courses.append(new)
print(Courses)
print(Courses[-2])
Courses.pop()
print(Courses)
Courses.remove('ba')
print(Courses)
Courses.sort()
print(Courses)
fruits = ['mango', 'apple', 'orange', 'kiwi', 'pineapple', 'papaya']
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
nums = [34,56,78,98,65]
print(nums)
nums.sort()
print(nums)
print(max(nums))
print(min(nums))
print(sum(nums))


countries = ['Russia', 'India', 'US', 'Japan', 'Germany', 'Italy', 'Zambia']
print(len(countries))
print(max(countries))
print(min(countries))
for item in countries:
    print(item)
print(len("How are you?"))
for item in countries:
    print(item,len(item))
for item in countries:
    print(item, item.upper(),len(item))   
for item in countries:
    print(f'{item}, {item.upper()},{len(item)}')   

# Use enumerate() function to get index of element.

for id, item in enumerate(countries):    
  print(id, item)

cubes = []   
for i in range(5):        
  cubes.append(i ** 3)
print(cubes)

cubes = []    
for i in range(5):       
  print("i = ", i)
  cubes.append(i ** 3)
  print("Number appended (i ** 3) = ", i ** 3)
  print("Current status of cubes list = ", cubes)
print()
print('Outside for loop')
print(cubes)


#Nested list

fruits = [['mango','apple','pineapple'], ['sitafal', 'orange']]
print(fruits)
print(len(fruits))
print(fruits[0])
print(fruits[1])
print(fruits[0],type(fruits[0]))
print(fruits[1],type(fruits[1]))
print(fruits[0][0])
print(fruits[1][0])
print(fruits[0][2])

