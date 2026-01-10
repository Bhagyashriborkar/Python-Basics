#DIctionary
company = {
  "name": "Tesla",              
  "founder": 'Elon Musk',
  "established": 2003
}
print(company)
print(type(company))
print(company['name'])
company['name'] = 'TESLAA'
print(company)
print(len(company))    
company['location'] = 'US'
print(company)  

# Another way to get item
print(company.get('name'))   
print(company.get('namee'))
print(company.keys())
print(company.values())
company['newkey'] = 'newval'
print(company.keys())
print(company.values())

# TO delete an item, use pop
student = {
    'name' : 'John',
    'age' : 12,
    'class' : 7
}

print(student)

student.pop('class')   
print(student)

# del can also be used to delete an item
student = {
    'name' : 'John',
    'age' : 12,
    'class' : 7
}

print(student)

del student['class']    
print(student)

# Dictionary Looping
new = dict({'name': 'Apple', 'year': 1975, 'founder': 'Steve Jobs and Steve Wozniak'})     # dict is special keyword, wrap your dictionary within dict() 
print(new)
print(type(new))

for item in new:              
  print(item)
for item in new:                
  print(item, new[item])  
  for item, val in new.items(): 
     print(item, val)

# Loop through only keys
for key in new.keys():
  print(key)

  #Nested Disctionary
  company = {
    'name': 'Apple',
    'year': 1975,
    'founders': {
        'first': 'Steve Jobs',
        'second': 'Steve Wozniak'
    }
    }
print(company)
print(company['founders'])
print(company['founders']['first'])
for item, val in company.items():
  print(item, val)
print(type(company['founders']))

