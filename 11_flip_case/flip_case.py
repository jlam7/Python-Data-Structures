def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    str = ''
    for char in phrase:
        if to_swap.islower() and to_swap == char:
            str = str + char.upper()
        elif to_swap.islower() and to_swap == char.lower():
            str = str + char.lower()
        elif to_swap.isupper() and to_swap == char:
            str = str + char.lower()
        elif to_swap.isupper() and to_swap == char.upper():
            str = str + char.upper()
        else:
            str = str + char
    return str
