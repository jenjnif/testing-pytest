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
