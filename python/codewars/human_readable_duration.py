"""
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.
"""

# STRATEGY
# Input: integer
# Output: string
# Goal: Convert seconds to a combination of years, days, hours, minutes and seconds.
# Steps:
# 1. Establish conversion rates for 4 duration types.
# 2. Save conversions into a dictionary for lookup.
# 3. Create storage variable for duration balance.
# 4. Create results variable to concatenate string amounts as applicable.
# 5. Looping through each K:V entry in the dict, start with largest time
#    quantity. If seconds = 0, return now.
#       If the seconds divided by year value yields a number greater than zero,
#       append either "1 year" or "x years" depending on the number. Decrement
#       the seconds * years from the duration balance.
#       If the seconds divided by day value yields a number greater than zero,
#       append either "1 day" or "x day" depending on the number. Decrement
#       the seconds * hours from the duration balance.
#       ETC
# 6. If there is a comma and space at the end of the sentence, return the slice
#    beginning at index 0 and ending at 2 from the end.


def format_duration(seconds):
    if seconds == 0:
        return "now"

    conversions = [
        ("year", 31536000),
        ("day", 86400),
        ("hour", 3600),
        ("minute", 60),
        ("second", 1),
    ]

    durations = []
    remaining_seconds = seconds

    for unit, value in conversions:
        quantity = remaining_seconds // value
        if quantity > 0:
            durations.append(f"{quantity} {unit}{'s' if quantity > 1 else ''}")
        remaining_seconds %= value

    return (
        durations[0]
        if len(durations) == 1
        else ", ".join(durations[:-1]) + " and " + durations[-1]
    )


# Tests
zero_seconds = 0
print(f"{format_duration(zero_seconds)} should = now")

one_second = 1
print(f"{format_duration(one_second)} should = 1 second")

sixtytwo_seconds = 62
print(f"{format_duration(sixtytwo_seconds)} should = 1 minute and 2 seconds")

half_year = 15731080
print(
    f"{format_duration(half_year)} should = 182 days, 1 hour, 44 minutes and 40 seconds"
)

many_years = 242062374
print(
    f"{format_duration(many_years)} should = 7 years, 246 days, 15 hours, 32 minutes and 54 seconds"
)
