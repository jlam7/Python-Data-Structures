def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    s1 = str(num1)
    s2 = str(num2)

    s1_dict = {}
    s2_dict = {}

    for char in s1:
        if char in s1_dict.keys():
            s1_dict[char] += 1
        else:
            s1_dict[char] = 1
    for char in s2:
        if char in s2_dict.keys():
            s2_dict[char] += 1
        else:
            s2_dict[char] = 1

    for key in s1_dict.keys():
        if key not in s2_dict.keys():
            return False
        if s1_dict[key] != s2_dict[key]:
            return False
    return True
