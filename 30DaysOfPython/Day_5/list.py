# 1. Declare an empty list
list1 = []
# 2. Declare a list with more than 5 items
list2 = ['banana','lemon','orange','apple','pineapple','melon','frutilla']
# 3. Find the length of your list
largo_lista2 = len(list2)
print(largo_lista2)
# 4. Get the first item, the middle item and the last item of the list
print(list2[0])
print(list2[3])
print(list2[-1])
# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['ignacio', 1.60, 'marrie', 'Manuel Rojas 10465']
print(mixed_data_types)
# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# 7. Print the list using _print()_
print(it_companies)
# 8. Print the number of companies in the list
print(len(it_companies))
# 9. Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])
# 10. Print the list after modifying one of the companies
it_companies[-1] = 'PARB'
print(it_companies)
# 11. Add an IT company to it_companies
it_companies.append('Logitech')
print(it_companies)
# 12. Insert an IT company in the middle of the companies list
it_companies.insert(4, 'Hola mundo')
print(it_companies)
# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[3] = 'IBM excluded!'
print(it_companies)
# 14. Join the it_companies with a string '#;&nbsp; '
it_companies.extend('#;&nbsp')
print(it_companies)
# 15. Check if a certain company exists in the it_companies list.
existe = 'Google' in it_companies
print(existe)
# 16. Sort the list using sort() method
it_companies.sort()
print(it_companies)
# 17. Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)
# 18. Slice out the first 3 companies from the list
print(it_companies[0:3])
# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])
# 20. Slice out the middle IT company or companies from the list
print(it_companies[1:-1])
# 21. Remove the first IT company from the list
it_companies.remove('#')
print(it_companies)
# 22. Remove the middle IT company or companies from the list
del it_companies[4]
print(it_companies)
# 23. Remove the last IT company from the list
del it_companies[-1]
print(it_companies)
# 24. Remove all IT companies from the list
del it_companies[:]
print(it_companies)
# 25. Destroy the IT companies list

# 26.Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end)
print(back_end)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.

full_stack = front_end.copy() + back_end.copy()
print(full_stack)

print('-------------------Exercises: Level 2--------------------')

# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
edades_ordenadas = ages.sort()
print(ages)

# - Sort the list and find the min and max age
min_val = min(ages)
print(min_val)
max_val = max(ages)
print(max_val)

# - Add the min age and the max age again to the list

# - Find the median age (one middle item or two middle items divided by two)
# - Find the average age (sum of all items divided by their number )
# - Find the range of the ages (max minus min)
# - Compare the value of (min - average) and (max - average), use _abs()_ method

# 1. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
# 1. Divide the countries list into two equal lists if it is even if not one more country for the first half.
# 1. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
