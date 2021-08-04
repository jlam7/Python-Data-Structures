def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    if isinstance(collection, list):
        if start != None:
            new_list = collection[start:]
            if new_list.count(sought):
                return True
        else:
            if collection.count(sought):
                return True

    if isinstance(collection, str):
        if start != None:
            new_str = collection[start:]
            if new_str.count(sought):
                return True
        else:
            if collection.count(sought):
                return True

    if isinstance(collection, tuple):
        if start != None:
            for el in collection:
                if collection.index(el) >= start and el == sought:
                    return True
        else:
            for el in collection:
                if el == sought:
                    return True

    if isinstance(collection, set):
        s = {sought}
        union = s & collection

        if len(union):
            return True

    if isinstance(collection, dict):
        if sought in collection.values():
            return True

    return False
