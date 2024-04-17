"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"
"""

# STRATEGY
# Input: tuple of 3
# Output: string (length 6)
# Steps:
# 1. Prepare for edge cases (out of range values)
# 2. Research formula to convert RGB to HEX.
#       R/G/B0 = Take the first number and divide by 16.
#       R/G/B1 = Take the remainder of the first digit and multiply by 16.
# 3. Create a dictionary to hold RGB to HEX values.
# 4. Populate a formatted array or string to hold the return value.

import math


def rgb(r, g, b):
    conversion_chart = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }
    conversion_chart[0] = 0

    hex_code = ""
    rgb_list = [r, g, b]

    for colour in rgb_list:
        if colour > 0 and colour <= 255:
            colour0 = math.floor(colour / 16)
            colour1 = colour % 16
            hex0 = conversion_chart.get(colour0)
            hex1 = conversion_chart.get(colour1)
            hex_code += f"{hex0}{hex1}"
        else:
            hex_code += "00" if colour <= 0 else "FF"

    return hex_code


def refactored_rgb(r, g, b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    return f"{r:02X}{g:02X}{b:02X}"


## TESTS

print(f"{rgb(255, 255, 255)} = FFFFFF")
print(f"{rgb(220, 20, 60)} = DC143C")
print(f"{rgb(1, 2, 3)} = 010203")
print(f"{rgb(-20, 275, 125)} = 00FF7D")

print(f"{refactored_rgb(255, 255, 255)} = FFFFFF")
print(f"{refactored_rgb(220, 20, 60)} = DC143C")
print(f"{refactored_rgb(1, 2, 3)} = 010203")
print(f"{refactored_rgb(-20, 275, 125)} = 00FF7D")
