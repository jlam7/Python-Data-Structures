def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reversed = list(phrase)
    reversed.reverse()
    newPhrase = ''.join(reversed)
    return newPhrase
