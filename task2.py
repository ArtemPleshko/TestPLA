john_salary = float(3800)
marta_salary = float(4500)
print (john_salary, marta_salary)


john_age = int(28)
marta_age = int(26.3)
print (john_age, marta_age)


john_name = str('JOHN')
marta_name = str('MARTA')
print (john_name, marta_name)


john_gender = bool(True)
marta_gender = bool (False)
print (marta_gender, john_gender)


john_friends = ['Peter', 'Lola', 'Ben']
marte_friends = ['Nina', 'Bob','Kate']
print ('john`s friends:', *john_friends, 'Marta`s friends:', *marte_friends)


list_str = ['Peter', 'Bob', 'Lola', 'Ben', 'Nina', 'Bob','Kate', 'Lola' ]
set_res = set(list_str)
print("The unique elements of list:\n")
list_res = (list(set_res))
for item in list_res:
    print(item)


adres = (46.4825, 30.7233)
print (*adres)


john = {'full_name': 'John', 'age': 28, 'salary': 4500, 'gender': 'male', 'friends': john_friends, 'coordinates': adres }
marta ={'full_name': 'Marta', 'age': 25, 'salary': 2300, 'gender': 'female', 'friends': marte_friends, 'coordinates': adres}
print (john, marta)
