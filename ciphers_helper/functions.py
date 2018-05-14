def clean_char(c: chr) -> chr:
    """
    Will return the char in upper case or delete if not a char in [a-zA-Z]
    :param c: The char to clean
    :return: The cleaned char
    """
    if ord(c) in range(ord('A'), ord('Z') + 1):
        return c
    elif ord(c) in range(ord('a'), ord('z') + 1):
        c = c.upper()
    else:
        c = ''
    return c


def get_position(c: chr) -> int:
    """
    Maps the position of the char as [0..25] -> [A-Z] ; -1 otherwise
    :param c: The char to get the position from
    :return: The position
    """
    c = clean_char(c)
    if c == '':
        return -1

    return ord(c) - ord('A')
