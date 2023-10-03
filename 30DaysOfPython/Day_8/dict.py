## 💻 Exercises: Day 8

# 1. Create  an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {'name': 'Skye', 'color': 'brown', 'breed': 'yorkshire', 'legs': 4, 'age': 5}
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, 
# marital status, skills, country, city and address as keys for the dictionary
student = {
'first_name': 'Ignacio', 
'last_name': 'Canales', 
'gender': 'male', 
'age': 26, 
'marital_status':'merried', 
'skills': ['HTML','CSS','Python','SQL'],
'country':'Chile', 
'city':'Santiago', 
'address':{
	'calle': 'Manuel Rojas',
	'numeracion': '10465'
	}
}
print(student)

# 4. Get the length of the student dictionary
print('largo del diccionario:')
print(len(student))

# 5. Get the value of skills and check the data type, it should be a list
print(student.get('skills'))
print(type('skills'))

# 6. Modify the skills values by adding one or two skills
print('item 6')
student['skills'].append('Mysql')
print(student)

# 7. Get the dictionary keys as a list
print('item 7')
keys = student.keys()
print(keys)

# 8. Get the dictionary values as a list
print('item 8')
values = student.values()
print(values)

# 9. Change the dictionary to a list of tuples using _items()_ method
print('item 9')
print(student.items())

# 10. Delete one of the items in the dictionary
print('item 9')
student.pop('city')
print(student)

# 11. Delete one of the dictionaries
del dog
print(dog)