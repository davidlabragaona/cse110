#presentation line
print('\nPlease enter the following:\n')

#We store the variables for the story
adjective = input('adjetive: ')
animal = input('animal: ')
verb1 = input('verb: ')
exclamation = input('exclamation: ')
verb2 = input('verb: ')
verb3 = input('verb: ')

#Returning the story
print('\nYour story is:\n')

print('The other day, I was really in trouble. It all started when I saw a very')

#Here we use the format and create the story using our variables
print('{} {} {} "{}!" I {}. But all'.format(adjective, animal, verb1, exclamation.capitalize(), verb1))
print('I could think to do was to {} over and over. Miraculously,'.format(verb2))
print('that caused it to stop, but not before it tried to ' + verb3)
print('right in front of my family.')