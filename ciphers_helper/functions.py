def clean_char(c):
    if ord(c) in range(ord('A'), ord('Z') + 1):
        return c
    elif ord(c) in range(ord('a'), ord('z') + 1):
        c = c.upper()
    else:
        c = ''
    return c


def get_position(c):
    c = clean_char(c)
    if c == '':
        return -1

    return ord(c) - ord('A')
