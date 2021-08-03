def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!')
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    d = {}
    vowels = 'aeiou'

    for char in phrase:
        if char.lower() in vowels:
            if char.lower() in d:
                d[char.lower()] += 1
            else:
                d[char.lower()] = 1

    return d
