from typing import Union


def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    hobby1 = list()
    hobby2 = list()

    for el in a:
        if a.index(el) == 2:
            hobby1.append(el)

    for el in b:
        if b.index(el) == 2:
            hobby2.append(el)

    for el in hobby1[0]:
        if el in hobby2[0]:
            return True
    return False
