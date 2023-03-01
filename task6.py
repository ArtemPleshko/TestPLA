#1 type of loops
#for
primes = [2, 3, 5, 7]
for prime in primes:
    print('for', prime)
#while
count = 0
while count < 5:
    count += 1
    print('while', count)

#while+else
count=0
while(count<5):
    count += 1
else:
    print("count value reached %d" %(count))

#2

var = 10
a = "true" if (var == 10) else "false"
print (a)

#3

a =[1, 2, 3, 4, 5, 6, 7, 8]
for element in a:
    if element %2 == 0:
        print (element)
