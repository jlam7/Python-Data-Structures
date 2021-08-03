def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lst = phrase.lower().split(' ')
    str = ''

    for word in lst:
        str = str + word.capitalize() + ' '

    return str.strip()
