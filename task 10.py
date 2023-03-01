ip = input().split('.')
for n in ip:
    if not (0<= int (n) <= 255):
        print ('Error, please enter correct IP')
        break
else:
    print ('Correct IP')