'''
Using namedtuples.

Cat:
    - type
    - size
    - favourite_food
    - roars
'''

from collections import namedtuple

Cat = namedtuple('Cat', ['type', 'max_size', 'favourite_food', 'roars'])
# sets the defaults for a new Cat if none are given
Cat.__new__.__defaults__ = ('Unknown', 'Unknown', 'Unknown', False)

c1 = Cat()
print(c1)
c2 = Cat('tiger', 3.9, 'deer', True)
print(c2)
c3 = Cat('lion', 2.5, 'elephant', False)
print(c3)
c3 = c3._replace(roars=True)
print(c3)

print('done')
