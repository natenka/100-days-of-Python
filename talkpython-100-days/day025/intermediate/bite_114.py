'''
As the new junior developer, you have been charged with enhancing the Color class.

Your task will be to implement the following:

add self.rgb to the __init__ method that gets its value from the provided COLOR_NAMES dictionary (k, v = color_name, rgb tuple = e.g.: "ALICEBLUE": (240, 248, 255)). If the value does not exist, just assume it is None.
Convert hex2rgb and rgb2hex into @classmethods.
Validate the values being passed to each of these classmethods and raise a ValueError if called with bad data.
Add a __repr__ method whose value is in the form of Color('white'), with white being the inital value that it was initialized with.
Add a __str__ method whose value is the RGB value of the color if it is found in COLOR_NAMES, else return Unknown.
Take a look at the tests for a better understanding of the values expected.

Good luck!
'''
import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
color_values_module = os.path.join('/tmp', 'color_values.py')
urllib.request.urlretrieve('https://bit.ly/2MSuu4z',
                           color_values_module)
sys.path.append('/tmp')

# should be importable now
from color_values import COLOR_NAMES  # noqa E402

import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
color_values_module = os.path.join('/tmp', 'color_values.py')
urllib.request.urlretrieve('https://bit.ly/2MSuu4z',
                           color_values_module)
sys.path.append('/tmp')

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        self.rgb = COLOR_NAMES.get(color.upper())

    @classmethod
    def hex2rgb(cls, hex_str):
        """Class method that converts a hex value into an rgb one"""
        return tuple(int(hex_str[i:i+1]) for i in range(0, 7, 2))

    @classmethod
    def rgb2hex(cls, rgb):
        """Class method that converts an rgb value into a hex one"""
        if not all(int(i) in range(0,256) for i in rgb):
            raise ValueError
        return '#{:02x}{:02x}{:02x}'.format(*rgb)

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        if not self.rgb: return "Unknown"
        return str(self.rgb)



"""Color class

The following sites were consulted:
    http://www.99colors.net/
    https://www.webucator.com/blog/2015/03/python-color-constants-module/
"""
import os
from string import hexdigits
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
color_values_module = os.path.join('/tmp', 'color_values.py')
urllib.request.urlretrieve('https://bit.ly/2MSuu4z',
                           color_values_module)
sys.path.append('/tmp')

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        self.rgb = COLOR_NAMES.get(self.color.upper(), None)

    @classmethod
    def hex2rgb(cls, hex_value):
        """Converts a hex value into an rgb one"""
        error_message = f"{hex_value} is not a valid hex value!"

        for char in hex_value:
            if char not in hexdigits:
                raise ValueError(error_message)

        if not len(hex_value) == 7 or not hex_value.startswith("#"):
            raise ValueError(error_message)

        return tuple(int(hex_value[i:i + 2], 16) for i in (1, 2, 4))

    @classmethod
    def rgb2hex(cls, rgb_value):
        """Converts an rgb value into a hex one"""
        error_message = f"{rgb_value} is not a valid RGB value!"

        if not isinstance(rgb_value, tuple):
            raise ValueError(error_message)

        valid = [1 for n in rgb_value if not (0 <= n <= 255)]
        if sum(valid) > 0:
            raise ValueError(error_message)

        return f"#{rgb_value[0]:02x}{rgb_value[1]:02x}{rgb_value[2]:02x}"

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        return f"{self.rgb}" if self.rgb else "Unknown"

