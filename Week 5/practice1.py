print ('Program for compare 2 number')
print()
print('Welcome')
print()

numb_1 = int(input('please, Introduce the first number: '))
numb_2 = int(input('Please, Introduce the second number: '))

if numb_1 > numb_2:
    print()
    print(f'The number: {numb_1} is greather than number: {numb_2}')
elif numb_1 < numb_2:
    print()
    print(f'The number: {numb_1} is less than number: {numb_2}')
else:
    print()
    print('The numbers are equal')
print()
print('Progran for my favorite animal')
print()
favorite_animal = input('What is your favorite animal: '  )
if favorite_animal.lower() == 'dog':
    print('Awesone this my favorite too!!!')
else:
    print(f'{favorite_animal} is a great animal')

print ('Program end')
