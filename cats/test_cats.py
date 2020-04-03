from cats import Cat

# four example tests
# Cat = namedtuple('Cat', ['type', 'max_size', 'favourite_food', 'roars'])


def test_cat_defaults():
    c1 = Cat()
    c2 = Cat('Unknown', 'Unknown', 'Unknown', False)
    assert c1 == c2


def test_cat_attributes():
    c3 = Cat('lion', 2.5, 'elephant', True)

    assert c3.type == 'lion'
    assert c3.max_size == 2.5
    assert c3.favourite_food == 'elephant'
    assert c3.roars is True


def test_asdict():
    # asdict() should return a dictionary.
    c_cat = Cat('tiger', 3.9, 'deer', True)
    c_dict = c_cat._asdict()
    expected = {'type': 'tiger',
                'max_size': 3.9,
                'favourite_food': 'deer',
                'roars': True
                }

    assert c_dict == expected


def test_cat_replace():
    # replace() should change passed in fields
    c_before = Cat('cheetah', 1.5, 'rabbit', True)
    c_after = c_before._replace(roars=False)
    c_expected = Cat('cheetah', 1.5, 'rabbit', False)

    assert c_after == c_expected
