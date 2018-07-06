#Dictionaries
things = ['a', 'b', 'c', 'd']
print things[1]

things[1] = 'z'
print things[1]

print things

stuff = {'name': 'Hannibal', 'age': '36', 'height': 6 * 12 + 2 }
print stuff['name']

print stuff['age']

print stuff['height']

stuff['city'] = 'San Francisco'

print stuff['city']

stuff[1] = "Wow"

stuff[2] = "Neato"

print stuff[1]

print stuff
#{'city': 'San Francisco', 2: 'Neato', 'name': 'Hannibal', 1: 'Wow', 'age': 36, 'height': 74}

del stuff['city']
del stuff[1]
del stuff[2]
stuff
#{'name': 'Hannibal', 'age': 36, 'height': 74}