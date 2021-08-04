def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """

    min = float('inf')
    max = 0
    min_str = ''
    max_str = ''
    instance = ''

    for key in d.keys():
        if isinstance(key, int):
            instance = 'int'
            if key < min:
                min = key
            if key > max:
                max = key
        elif isinstance(key, str):
            instance = 'str'
            if len(key) < min:
                min = len(key)
                min_str = key
            if len(key) > max:
                max = len(key)
                max_str = key

    tuple1 = (min, max)
    tuple2 = (min_str, max_str)

    if instance == 'int':
        return tuple1
    else:
        return tuple2
