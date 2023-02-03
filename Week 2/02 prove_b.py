print('The Mad Libs game \n\n\nPlease introduce the following words:\n')
adjective_1 = input ('An adjective: ' )
animal = input ('An animal: ' )
verb_1 = input ('A verb: ' )
exclamation = input ('Exclamation: ' )
verb_2 = input ('An other verb: ' )
verb_3 = input ('An other verb: ')
adjective_2 = input ('An other adjetive: ')
adjective_3 = input ('An other adjetive: ')
verb_4 = input ('An other verb: ')

output = f'You story is:\n\nThe other day, I was really in trouble. It all started when I saw a very \n{adjective_1} {animal} {verb_1} down the hall way. "{exclamation.capitalize()}" I yelled. But all \nI could think to do was to {verb_2} over and over. Miraculously, \nthat caused it to stop, but not before it tried to {verb_3} right in front of my family.\nIt was so {adjective_2}, my family started to laft, and said "it just a very {adjective_3} {animal}".\nIt is not scary, but I was scared, since that I cannot {verb_4}.'

print(output)
