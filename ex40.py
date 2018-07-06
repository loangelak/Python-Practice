mystuff = {'apple': 'I AM APPLES!'}
print mystuff['apple'] #get apple from dict

import mystuff
mystuff.apple() #get apple from the module
print mystuff.tangerine #same thing, it's just a variable

#dict style
mystuff['apples']

#module style
mystuff.apples()
print mystuff.tangerine

#class style
thing = MyStuff()
thing.apples()
print thing.tangerine
