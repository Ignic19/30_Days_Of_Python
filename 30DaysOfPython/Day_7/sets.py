## 💻 Exercises: Day 7


# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


### Exercises: Level 1

# 1. Find the length of the set it_companies
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(["Opera", "Xiaomi"])
print(it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove("Google")
print(it_companies)

# 5. What is the difference between remove and discard
print("el método remove muestra error si no encuentra el item, a diferencia que discard no muestra error")

### Exercises: Level 2

# 1. Join A and B
C = A.union(B)
print(C)

# 2. Find A intersection B
D = A.intersection(B)
print(D)

# 3. Is A subset of B
E = A.issubset(B)
print(E)

# 4. Are A and B disjoint sets
F = A.isdisjoint(B)
print(F)

G = B.isdisjoint(A)
print(G)

# 5. Join A with B and B with A
H = A.union(B)
I = B.union(A)
print(H)
print(I)

# 6. What is the symmetric difference between A and B
J = A.symmetric_difference(B)
print(J)

# 7. Delete the sets completely
# del A
# del B
# del it_companies
# print(A + b + it_companies)

### Exercises: Level 3

# 1. Convert the ages to a set and compare the length 
# of the list and the set, which one is bigger?
st = set(age)
print(age)

# 2. Explain the difference between the following data types: 
# string, list, tuple and set


# 3. _I am a teacher and I love to inspire and teach people._ 
# How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
