print('Program Grade Calculator')
print()
letter = globals()
usuario_grades = float(input('Please, introduce your grade: '))
if usuario_grades >=90:
    letter = 'A'
    print()
    print('Congratulation, you passed the course')
elif usuario_grades >=80:
    letter = 'B'
    print()
    print('Good job, you passed the course')
elif usuario_grades >=70:
    letter = 'C'
    print()
    print('You passed the course')
elif usuario_grades >=60:
    letter = 'D'
    print()
    print('The next time you will do better,\n you did´n pass the course')
else:
    letter = 'F'
    print()
    print('You did´n get percentages to pass the course')
output = f'Your letter grade is: {letter}'
print()
print(output)
