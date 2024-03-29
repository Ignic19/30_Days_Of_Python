## 💻 Exercises: Day 9

### Exercises: Level 1
"""
1.  Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

    sh
    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.
"""    
# edad = int(input("Qué edad tienes?: "))
# if edad >= 18:
#     print("You are old enough to learn to drive.")
# else:
#     print("You need 3 more years to learn to drive")

"""
2.  Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to 
print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if 
my_age = your_age. Output:

    sh
    Enter your age: 30
    You are 5 years older than me.
"""
# miedad = int(input("Ingresa mi edad: "))
# tuedad = int(input("Ingresa tu edad: "))
# if miedad > tuedad:
#     print("Yo soy mayor que tú")
# else:
#     print("Tú eres mayor que yo")

"""
3.  Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
if a is less b return a is smaller than b, else a is equal to b. Output:

    sh
    Enter number one: 4
    Enter number two: 3
    4 is greater than 3
"""
# a = (input("Ingresar el valor de a: "))
# b = (input("Ingresar el valor de b: "))
# if a > b:
#     print("a es mayor que b")
# elif b > a:
#     print("b es mayor que a")
# else:
#     print("Tienen el mismo valor")

    ### Exercises: Level 2

# print("1. Write a code which gives grade to students according to theirs scores : 80-100, A; 70-89, B; 60-69, C; 50-59, D; 0-49, F")

# nota = int(input("Ingrese calificación: "))
# if nota >= 80 and nota <= 100:
#     print("Está en grado A")
# elif nota >= 70 and nota <= 89:
#     print("Está en grado B")
# elif nota >= 60 and nota <= 69:
#     print("Está en grado C")
# elif nota >= 50 and nota <= 59:
#     print("Está en grado D")
# elif nota >= 0 and nota <= 49:
#     print("Está en grado F") 


# 1. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
#     September, October or November, the season is Autumn.
#     December, January or February, the season is Winter.
#     March, April or May, the season is Spring
#     June, July or August, the season is Summer

# otoño = ["September", "October", "November"]
# invierno = ["December", "January", "February"]
# primavera = ["March", "April", "May"]
# verano = ["June", "July", "August"]

# mes = input("Ingresa mes del año: ")
# if mes in otoño:
#     print("Este mes pertenece a la estación de otoño")
# elif mes in invierno:
#     print("Este mes pertenece a la estación de invierno")
# elif mes in primavera:
#     print("Este mes pertenece a la estación de primavera")
# elif mes in verano:
#     print("Este mes pertenece a la estación de verano")
# else:
#     print("El mes Pertenece a otra estación del año.")

# 2.  The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']

    # If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
    # If the fruit exists print('That fruit already exist in the list') 
# nuevafruta = input("Ingrese el nombre de una fruta: ")
# if nuevafruta in fruits:
#     print("Su fruta está en el listado de frutas")
# else:
#     fruits.append(nuevafruta)
# print(fruits)

    ### Exercises: Level 3

   # 1. Here we have a person dictionary. Feel free to modify it!
   
"""py
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
"""

     # * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
     # * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
     # * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
     # * If the person is married and if he lives in Finland, print the information in the following format:
