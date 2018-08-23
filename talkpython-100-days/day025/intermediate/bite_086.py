def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if not all(value in range(0, 256) for value in rgb):
        raise ValueError('Wrong value')
    return '#{:02x}{:02x}{:02x}'.format(*rgb).upper()
