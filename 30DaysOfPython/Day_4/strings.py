# 1.Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
x = ('Thirty ' + 'Days ' + 'Of ' + 'Python')
print(x)

# 2.Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
y = ('Coding ' + 'For ' + 'All')
print(y)

# 3.Declare a variable named company and assign it to an initial value "Coding For All"
company = "Coding for All"

# 4.Print the variable company using print().
print(company)

# 5.Print the length of the company string using len() method and print().
print(len(company))

# 6.Change all the characters to uppercase letters using upper() method.
print(company.swapcase())

# 7.Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8.Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9.Cut(slice) out the first word of Coding For All string.
sinprimera = company[7:]
print(sinprimera)

# 10.Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding'))

# 11.Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding' , 'Python'))

# 12.Change Python for Everyone to Python for All using the replace method or other methods.
frase = "Python for Everyone"
print(frase.replace(frase, 'Python for All'))

# 13.Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

# 14."Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Aple, IBM, Oracle, Amazon"
print(companies.split(','))

# 15.What is the character at index 0 in the string Coding For All.
num0 = company[0]
print(num0)

# 16.What is the last index of the string Coding For All.
last_num = company[-1]
print(last_num)
# print(company.rfind('l'))

# 17.What character is at index 10 in "Coding For All" string.
num10 = company[10]
print(num10)