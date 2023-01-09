#!/usr/bin/env python
# coding: utf-8

# # Functions, Scoping, Data Collections 1 & List Comprehensions

# ## Tasks Today:
# 
# <i>Monday Additions (or, and ... if statements)</i>
# 
# 1) String Manipulation <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) strip() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) title() <br>
# 2) Working With Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) min() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) max() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) sum() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) sort() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Copying a List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) 'not in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Checking an Empty List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; j) Removing Instances with a Loop <br>
# 3) List Comprehensions <br>
# 4) Tuples <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) sorted() <br>
# 5) Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) User-Defined vs. Built-In Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Accepting Parameters <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Default Parameters <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Making an Argument Optional <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Keyword Arguments <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) Returning Values <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) *args <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; h) Docstring <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Using a User Function in a Loop <br>
# 6) Scope

# ### String Manipulation

# ##### .lstrip()

# In[8]:


# string.lstrip()
name = "     hJohn Smith"
print(name.lstrip(" " "h"))


# ##### .rstrip()

# In[2]:


# string.rstrip()
name = "Bill Ross     th"
print(name.rstrip(" " "th"))


# ##### .strip()

# In[4]:


# string.strip()
name = "     John Smith     th"
print(name.strip("ah"))


# ##### .title()

# In[15]:


# string.title()
president = "barak obama"

print(president.title())


# ### String Exercise <br>
# <p>Strip all white space and capitalize every name in the list given</p>

# In[20]:


names = ['    coNNor', 'max', ' EVan ', 'JORDAN']
# HINT: You will need to use a for loop for iteration

# list_above = []
# list_above.append(names)
# for x in range(len(1000)):
#     print(x)

names_list = []
for name in names:
    print(name.strip().title())
    names_list.append(name.strip().title())
print(names_list)


# ### Working With Lists

# ##### min()

# In[21]:


# min(list)
numbers = [4,2,97,54,16]

print(min(numbers))


# ##### max()

# In[22]:


# max(list)

print(max(numbers))


# ##### sum()

# In[23]:


# sum(list)

print(sum(numbers))


# ##### sorted()

# In[28]:


# sorted(list) 
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted(numbers))
print(f'regular numbers: {numbers}')

print(f'sorted numbers: {sorted_numbers}')


# ##### .sort() <br>
# <p>Difference between sort and sorted, is that sorted doesn't change original list it returns a copy, while .sort changes the original list</p>

# In[30]:


# list.sort()
print(f'before sort: {numbers}')
print(numbers.sort())
print(numbers)

# use sorted when you don't want to alter original list, use .sort() when you want to alter original list


# ##### Copying a List

# In[31]:


# [:] copies a list, doesn't alter original'
list_1 = numbers[:]
print(list_1)
print(numbers)


# ##### 'in' keyword

# In[32]:


l_teachers = ["Joel","Derek","Conner","Brian","Joe"]

if 'Derek' in l_teachers:
    print('Coding Temple Instructor')
else:
    print('Not an Instructor')
    
for name in l_teachers:
    if "C" in name(0):
        print("Found")
    else:
        print("Not Found")


# In[35]:


# Looking inside of the list for specific characters
# for name in l_teachers:
#     if name[0] == 'C':
#         print('Teacher that starts with C')
#     else:
#         print("We ain't got it boss...")
        
for name in l_teachers:
    if 'C' in name[0]:
        print('Found')
    else:
        print('Not Found')


# ##### 'not in' keyword

# In[33]:


if 'Zack' not in l_teachers:
    print('Not a CT Instructor')


# ##### Checking an Empty List

# In[36]:


# if l_1: or if l_1 = []
l_2 = []

if l_2 == []:
    print('Empty')


# ##### Removing Instances with a Loop

# In[43]:


# while, remove
names = ['Conner',"Joel", "Max","Evan","Rob","Evan"]

while 'Evan' in names:
    names.remove('Evan')
print(names)

for name in names:
    if name == 'Evan':
        names.remove('Evan')
print(names)


# ### List Exercise <br>
# <p>Remove all duplicates<br><b>Extra: Create a program that will remove any duplicates from a given list</b></p>

# In[45]:


names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
# Hint 1: You will need an append
# Hint 2: Using an empty list will make life easier

names_copy = []

for i in names:
    if i not in names_copy:
        names_copy.append(i)
print(f'new list after removing dups {names_copy}')



# ### List Comprehensions <br>
# <p>Creating a quickly generated list to work with<br>*result*  = [*transform*    *iteration*         *filter*     ]</p>

# ##### In a list comprehension we have a few pieces:
# 1. The first is the counter/ variable - IN this the variable is x
# 2. then we have a transform for the variable
# 3. The finale part of a list comp is called the condition
# 
# ```python
#     [variable, transform, condition]
# ```

# In[47]:


# number comprehension

# With a regular for loop

nums = []

for i in range(100):
    nums.append(i)
print(nums)


# IN a list comprehension we have a few pieces:
# The first is the counter/ variable - IN this the variable is x
# Then we have a transform for the variable 
# The finale part of a list comp is called the condition

#[variable, transform, condition]

print('\n')

# List Comprehension syntax
nums_comp = [i for i in range(100)]

print(nums_comp)


# There are a few benefits to using List comprehensions. The most obvious would be that we now have shorter code to work with instead of using 3+ lines of code in the for loop variant.
# 
# Another is an added benefit to memory usage. Since the list's memory is allocated first before adding elements to it, we don't have to resize the list once we add elements to it.
# 
# Lastly, list comprehensions are considered the "pythonic" way to write code by the PEP8 standards (Python Style Guide)

# In[50]:


# square number comprehension
squares = [x**2 for x in range(10)]

print(squares)

squares_reg = []

for x in range(10):
    squares_reg.append(x**2)

print('\n')
print(squares_reg)


# In[52]:


# string comprehension
names = ['Conner', 'Max','Evan','Rob']

first_char_comp = [name[0] for name in names]

print(first_char_comp)

# For Loop Version
first_char = []

for name in names:
    first_char.append(name[0])
print('\n')
print(first_char)


# In[54]:


# Using the 'if' statement ... if always comes after the for
c_names = [first_name for first_name in names if first_name[0] == 'C']

print(c_names)

# for loop version
c_names_reg = []

for first_name in names:
    if first_name[0] == 'C':
        c_names_reg.append(first_name)

print('\n')
print(c_names_reg)


# ### Tuples <br>
# <p><b>Defined as an immutable list</b></p><br>Seperated by commas using parenthesis

# In[59]:


tup_1 = 1,2,3 # first way of creating a tuple
tup_2 = (1,2,3) # Another/Second way of creating a tuple

print(type(tup_1))
print(type(tup_2))

print(tup_1[0])

print(len(tup_1))

# Looping over a tuple
for number in tup_1:
    print(number)
    
# Looping over a tuple with an index using range and len
for number in range(len(tup_1)):
    print(tup_1[number])


# ##### sorted()

# In[62]:


tup_3 = (20,5,1,3,9,45)

sorted_tup = sorted(tup_3)

random_list = [3,4,66,77,33]
combine_list = sorted_tup + random_list

new_tup = tuple(combine_list)

print('\n')
print(new_tup)
print(combine_list)
print(type(sorted_tup))
print(sorted_tup)


# ##### Adding values to a Tuple

# In[63]:


print(tup_1)

tup_1 = tup_1 + (5,)

print(tup_1)


# ## Functions

# ##### User-Defined vs. Built-In Functions

# In[64]:


# User Defined Function
def sayHello():
    return 'Hello World'
# Showing the function call in memory
print(sayHello)

# Calling The function
print(sayHello())


# ##### Accepting Parameters

# In[67]:


# Order matters
# A variable can be of any type of object
def printFullName(first_name,last_name):
    return f'Hello {first_name}, {last_name}'

print(printFullName('Joel', 'Carter'))
print(printFullName('Carter', 'Joel'))

print(printFullName(last_name="Carter",first_name = "Joel"))


# ##### Default Parameters

# In[72]:


# default parameters need to be AFTER non-default parameters at all times

def printAgentName(first_name, last_name = 'Bond'):
    return f'The name is...{first_name} {last_name}'

printAgentName('James')

# DON'T DO THIS PLEASE 
# def printAgentAgain(last_name = 'Bond', first_name):
#     return f'The name is...{first_name} {last_name}'

# printAgentAgain(first_name ='James')


# ##### Making an Argument Optional

# In[73]:


def printHorseName(first, middle = "", last = "Ed"):
    return f"Hello {first} {middle} {last}"

printHorseName("Mr")


# ##### Keyword Arguments

# In[74]:


# last_name='Max', first_name='Smith' in the function call
def printSuperHero(name, power = "flying"):
    return f'{name} and superpower is {power}'

printSuperHero('IronMan')
# see above


# # Creating a start, stop, step function

# In[75]:


def my_range(stop,start=0,step = 1):
    for i in range(start,stop,step):
        print(i)
my_range(20,1)


# ##### Returning Values

# In[76]:


def addNums(num1,num2):
    return num1 + num2

addNums(5,2)


# ##### *args / **kwargs (AKA KeyWord Args)

# In[1]:


# stands for arguments, takes ANY number of arguments as parameters
# must be last if muliple parameters are present
def printArgs(num1,*args, **kwargs):
    print(num1)
    print(args)
    
    for arg in args:
        print(arg)
        
    for kwarg in kwargs:
        print(kwarg)
        
printArgs(36,'DragonZord','vanilla',2,3,testing="joel")


# ##### Docstring

# In[79]:


def printNames(list_1):
    """
        printNames(list_1)
        Function requires a list to be passed as a parameter
        and will print the contents of the list. Expecting 
        a list of names(strings) to be passed.
    """
    for name in list_1:
        print(name)
        
printNames(['George','Ramon','Peter'])
help(printNames)


# ##### Using a User Function in a Loop

# In[82]:


def printInput(answer):
    print(answer)

response = input('Are you ready to quit??')

while True:
    ask = input('What do you want to do?')
    
    printInput(ask)
    
    response = input('Ready Yet?')
    if response.lower() == 'quit':
        break


# ## Function Exercise <br>
# <p>Write a function that loops through a list of first_names and a list of last_names, combines the two and return a list of full_names</p>

# In[2]:


first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']

def nameList(fn , ln):
    l = len(fn)
    i = 0
    while i < l:
        print('{0} {1}'.format(fn[i], ln [i]))
        i += 1
# Output: ['John Smith', 'Evan Smith', 'Jordan Williams', 'Max Bell']


# ## Scope <br>
# <p>Scope refers to the ability to access variables, different types of scope include:<br>a) Global<br>b) Function (local)<br>c) Class (local)</p>

# In[86]:


# placement of variable declaration matters
number = 3 # Global Variable

def myFunc():
    num_3 = 6 # Local Function Variable
    return num_3

print(number)
return_num = myFunc()

print(return_num)


# # Exercises

# ## Exercise 1 <br>
# <p>Given a list as a parameter,write a function that returns a list of numbers that are less than ten</b></i></p><br>
# <p> For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]</p>

# In[ ]:


# Use the following list - [1,11,14,5,8,9]
a_list = [1,11,14,5,8,9]

def list_func():
    for i in range(len(a_list)):
        if a_list[i] < 10:
            print(a_list[i])
            
print(list_func())


# ## Exercise 2 <br>
# <p>Write a function that takes in two lists and returns the two lists merged together and sorted<br>
# <b><i>Hint: You can use the .sort() method</i></b></p>

# In[ ]:


l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def add_lists():
    large_list = l_1 + l_2
    large_list.sort
    print(large_list)

print(add_lists())

