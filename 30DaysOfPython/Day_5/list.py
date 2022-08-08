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
# 23. Remove the last IT company from the list
# 24. Remove all IT companies from the list
# 25. Destroy the IT companies list