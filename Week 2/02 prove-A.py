print('The Mad Libs Activity')
 #print('Please introduce the following words:')
 
    adjective = input ('Adjective: ' )
    animal = input ('Animal: ' )
    verb_1 = input ('Firs verb: ' )
    exclamation = input ('Exclamation: ' )
    verb_2 = input ('Second verb: ' )
    verb_3 = input ('Third verb: ')

print('Your story is: ')

output = f'The other day, I was really in trouble. It all started when I saw a very 
{adjective} {animal} {verb_1} down the hall way. "{exclamation.capitalize()}" I yelled. But all
I could think to do was to {verb_2} over and over. Miraculously,
 that caused it to stop, but not before it tried to {verb_3} right in front of my family. '

print(output)