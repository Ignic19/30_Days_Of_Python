1# first_name = input("Escribe tu nombre: ")
# last_name = input("Escribe tu apellido: ")
# def generate_full_name ():
#     # first_name = 'Asabeneh'
#     # last_name = 'Yetayeh'
#     saludo = 'Hola'
#     space = ' '
#     full_name = saludo + space + first_name + space + last_name
#     return full_name
# print(generate_full_name())

def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))


## 💻 Exercises: Day 11

### Exercises: Level 1

# 1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.
# def _add_two_numbers_(num1, num2):
#     resultado_suma = num1 + num2
#     return resultado_suma
# print(_add_two_numbers_(3, 5))
    
# 2. Area of a circle is calculated as follows: area = π x r x r. 
# Write a function that calculates _area_of_circle_.
# Al quere agregar un input, éste debe estar antes de la function y se debe quitar el argumento del print final.
# x = int(input("Ingresa el radio de tu circulo: "))
# def _area_of_circle_():
#     area_circle = 3.14 * x * x
#     return area_circle
# print("El área del circulo es:",(_area_of_circle_()))
# print(_area_of_circle_())

# 3. Write a function called add_all_nums which takes arbitrary number of arguments 
# and sums all the arguments. Check if all the list items are number types. 
# If not do give a reasonable feedback.
# def add_all_nums():

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.
def _convert_c_to_f_(c):
    fahrenheit = (c * 9/5) + 32
    return fahrenheit
print("40°C a F°: ")
print(_convert_c_to_f_(40))

# 5. Write a function called check-season, it takes a month parameter and returns the 
# season: Autumn, Winter, Spring or Summer.

mes = input("Ingresa mes del año: ")

# def check_season():
#     # estacion = {
#     otono = ["September", "October", "November"]
#     # invierno = ["December", "January", "February"]
#     # primavera = ["March", "April", "May"]
#     # verano = ["June", "July", "August"]
# # }
#     if mes in otono:
#         print("Este mes pertenece a la estación de otoño")
#     # elif mes in invierno:
#     #     print("Este mes pertenece a la estación de invierno")
#     # elif mes in primavera:
#     #     print("Este mes pertenece a la estación de primavera")
#     # elif mes in verano:
#     #     print("Este mes pertenece a la estación de verano")
#     else:
#         print("El mes pertenece a otra estación del año.")
#     # return estacion1
# print(check_season())

# 6. Write a function called calculate_slope which return the 
# slope of a linear equation.


# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, 
# _solve_quadratic_eqn_.
def _solve_quadratic_eqn_(a, b, x, c):
    quadratic_eq = (a*x)**2 + (b*x) + c

    return quadratic_eq
print(_solve_quadratic_eqn_(20, 3, 2, 26))

# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.


# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

# ```py
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]
# ```

# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

# ```py
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
# ```

# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

# ```py
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  # [2, 7, 9]
# ```

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

# ```py
# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10)) # 55
# print(sum_all_numbers(100)) # 5050
# ```

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

### Exercises: Level 2

# 1.  Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

# ```py
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
# ```

# 1. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
# 1. Call your function _is_empty_, it takes a parameter and it checks if it is empty or not
# 1. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

### Exercises: Level 3

# 1. Write a function called is_prime, which checks if a number is prime.
# 1. Write a functions which checks if all items are unique in the list.
# 1. Write a function which checks if all the items of the list are of the same data type.
# 1. Write a function which check if provided variable is a valid python variable
# 1. Go to the data folder and access the countries-data.py file.

# - Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# - Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.