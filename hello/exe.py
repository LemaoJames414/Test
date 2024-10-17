""""
number_list = [1,2,3,5,7,8,9]
#print odd number that is bigger than 3
for x in number_list:
    if x < 3:
        print('number < 3')
        continue
    print(x,'will %2')
    if x % 2 == 0:
        break
else:
    print('Not found')

while number_list:
    x = number_list.pop()
    print(x)
    if x % 2 == 0:
        break
"""
'''
number = int(input('Enter a random number: '))
num = (number)

match num:
    case 10:
        print('the number is 10')
    case 20:
        print('The number is 20')
    case 30:
        print('The number is 30')
'''






