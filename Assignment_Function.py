"""Assignment - 2 Function.ipynb

"""

# 1. Write a Python function to find the maximum of three numbers.

def max_num(a,b,c):
  if a >= b and a >= c:
    return a
  elif  b >=c:
    return b
  else:
    return c


maximum_num = max_num(10,50,30)
print('Maximum number is: ', maximum_num)

# 2. Write a Python function to sum all the numbers in a list.
# output : 20


def sum_of_num(lst):
  sum = 0
  for i in lst:
    sum += i
  return sum

# Given list
lst = (8, 2, 3, 0, 7)
n = sum_of_num(lst)
print('Sum of all numbers: ',n)

# 3. Write a Python function to multiply all the numbers in a list.
# output : -336

def multiply(lst):
  product = 1
  for i in lst:
    product = product * i
  return product

# Given list
lst =  (8, 2, 3, -1, 7)
n = multiply(lst)
print('Multiply of all the numbers: ',n)

# 4. Write a Python function to reverse a string.

def reverse_string(str):
  rev = ''
  for i in s:
    rev = i + rev
  return rev


s= "1234abcd"
reverse_string(s)

# 5. Write a Python function to check whether a number falls within a given range.

def find_range(i, start, end):
  if i in range(start, end+1):
    print(f'{i} is lies in the range.')
  else:
    print(f'{i} is not lies in the range.')


find_range(25, 20, 50)

# 6. Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Output : No. of Upper case characters : 3
# output : No. of Lower case Characters : 12


def count_string(s):
  lower_count = 0
  upper_count = 0

  for i in st:
    if i.islower():
      lower_count += 1
    elif i.isupper():
      upper_count += 1
  print('No. of lower case character: ',lower_count)
  print('No. of upper case character: ',upper_count)

st =  'The quick Brow Fox'
count_string(st)

# 7. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Output : [1,2,3,4,5]

def distinct_element(lst):
  result = []
  for i in lst:
    if i not in result:
      result.append(i)
  return result

lst = [1,2,3,3,3,3,4,5]
n = distinct_element(lst)
print('Distinct element is: ',n)

# 8.  Write a Python function that checks whether a passed string is a palindrome or not.

def check_palindrome(st):
  if st == st[::-1]:
    return 'Its a palindrome'
  else:
    return 'Its not a palindrome'


check_palindrome('madam')

# 9. Write a Python program that accepts a hyphen-separated sequence of words as input
# and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# output :  black-green-red-white-yellow


st = input('Enter hypen seperated word: ')

# split the word
word = st.split('-')

# sort the word
word.sort()

#join the word by hypen
result = ('-').join(word)

print('Hypen seperated word: ', result)

# 10. Write a Python program to detect the number of local variables declared in a function.

def sample_variable():
  a = 10
  b = 20
  c = a+b
  print('Number of local variables: ', len(locals()))
sample_variable()

# 11. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
#     also create a lambda function that multiplies argument x with argument y and prints the result.
#     Sample Output:25 , 48


# addition of number
add = lambda x:x + 15

a = int(input('Enter the number: '))
print('After adding 15: ',add(a))


# Multiplication of number
multiply = lambda x,y : x*y

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
print('Multiplication of the two number: ', multiply(a,b))

# 12 .  Write a Python program to create a function that takes one argument,
#        and that argument will be multiplied with an unknown given number.
# Output:
	       # Double the number of 15 = 30
	       # Triple the number of 15 = 45
	       # Quadruple the number of 15 = 60
	       # Quintuple the number 15 = 75


def multiple_of(n):
  return lambda x : x * n

double = multiple_of(2)
triple = multiple_of(3)
quadruple = multiple_of(4)
quintuple = multiple_of(5)


# given number
num = 15

print('Double the number of 15:     ', double(num))
print('Triple the number of 15:     ', triple(num))
print('Quadruple the number of 15:  ', quadruple(num))
print('Quintuple the number of 15:  ', quintuple(num))

# 13. Write a Python program to sort a list of tuples using Lambda.
#     output : [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)


# Given list
marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

result = sorted(marks, key = lambda x : x[1])
print(result)

# 14.  Write a Python program to sort a list of dictionaries using Lambda.
       # output : [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
       #            {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
        #           {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]


# Given dictionary
dic = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
       {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
        {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

result = sorted(dic, key = lambda x : x['color'])
print(result)

# 15. Write a Python program to filter a list of integers using Lambda from given list.


# Given list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x : x % 2 ==0, lst))
print('Even number: ',result)


# for odd
result = list(filter(lambda x : x % 2 !=0, lst))
print('Odd numbers: ', result)

# 16 Write a Python program to square and cube every number in a given list of integers using Lambda.


# To display square from given list
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(map(lambda x: x**2, lst1))
print('Square of the numbers: ', result)


# To display cube from given list
result = list(map(lambda x: x**3, lst1))
print('Cube of the numbers: ', result)

# 18. Write a Python program to find if a given string starts with a given character using Lambda.


# Given string

string = (lambda s, i : s.startswith(i))
print(string('hello','h'))

# 19. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
      # output : [2, 5, 7, 8, 9, -10, -3, -1]



# Given list
lst = [-1, 2, -3, 5, 7, 8, 9, -10]

result = sorted(lst, key = lambda x : x < 0)
print('Sorted list: ', result)


# Using filter method
positive = list(filter(lambda x : x >= 0, lst))
negative = list(filter(lambda x : x < 0, lst))

result = positive + negative
print('Sorted list: ', result)

# 20. Write a Python program to count the even and odd numbers in a given array of integers using Lambda.
      # output : Number of even numbers in the above array: 3
	    #        : Number of odd numbers in the above array: 5



# Display even numbers
lst = [1, 2, 3, 5, 7, 8, 9, 10]

even = len(list(filter(lambda x : x % 2 == 0,lst)))
print('Number of even numbers in the above array: ', even)


# Display odd numbers
odd = len(list(filter(lambda x : x % 2 != 0, lst)))
print('Number of odd numbers in the above array: ', odd)

# 21. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
      # output : [19, 65, 57, 39, 152, 190]



# Given list
ls = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

res = list(filter(lambda x : (x%19 ==0 or x%13 ==0), ls))
print('Divisible by 13 or 19: ', res)

# 22. Write a Python program to check whether a given string contains
       # a capital letter, a lower case letter, a number and a minimum length using lambda.


password = lambda s : (
             any(map(lambda x : x.isupper(),s)) and
             any(map(lambda x : x.islower(),s)) and
             any(map(lambda x : x.isdigit(),s)) and
             len(s) >= 8
             )

text = 'abhSt12AP'
resul = password(text)
print(resul)