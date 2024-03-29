# Write a function named setAlarm/set_alarm/set-alarm/setalarm (depending on language)
# which receives two parameters. The first parameter, employed, is true whenever you are
# employed and the second parameter, vacation is true whenever you are on vacation.

# The function should return true if you are employed and not on vacation (because these
# are the circumstances under which you need to set an alarm). It should return false otherwise.

# Examples:
# employed | vacation
# true     | true     => false
# true     | false    => true
# false    | true     => false
# false    | false    => false

# STRATEGY
# The only time the function returns true is if employed=True AND vacation=False
# Likely overkill to map out combos...


def set_alarm(employed, vacation):
    return True if employed == True and vacation == False else False


print(set_alarm(True, True))
print(set_alarm(True, False))
print(set_alarm(False, True))
print(set_alarm(False, False))


def refactored_set_alarm(employed, vacation):
    return employed and not vacation


print(refactored_set_alarm(True, True))
print(refactored_set_alarm(True, False))
print(refactored_set_alarm(False, True))
print(refactored_set_alarm(False, False))
