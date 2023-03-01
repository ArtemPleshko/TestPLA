####
mytuple = (0, True, False)
a = all(mytuple)
print (a)
####
x = bool(1)
####
x = 5
print(callable(x))

def testFunction():
  print("Test")

y = testFunction
print(callable(y))
####

class Person:
  name = "John"
  age = 36
  country = "Norway"

print(dir(Person))

###########
def check_odd(number):
    if number % 2 == 1:
          return True

    return False
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_iterator = filter(check_odd, numbers)
odd_numbers = list(odd_iterator)

print(odd_numbers)
##############

numbers = [1, 2, 3, 4, 2, 5]
result = isinstance(numbers, list)
print(result)
##################

numbers = [1, 2, 5]
length = len(numbers)
print(length)
#######################3

def calculateSquare(n):
    return n*n
numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

#############
languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3, 6]

result = zip(languages, versions)
print(list (result))

