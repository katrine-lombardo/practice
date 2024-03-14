# The main idea is to count all the occurring characters in a string. If you
# have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal,
# {}.


def count(s):
    freq_dict = {}

    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    return freq_dict


def count_refactored(s):
    return {char: s.count(char) for char in s}


# ---------------------------------- TESTS ----------------------------------

test1 = count("aba")
solution1 = "{'a': 2, 'b': 1}"
print(f"{test1} should = {solution1}")

test2 = count("")
solution2 = "{}"
print(f"{test2} should = {solution2}")

test3 = count("aa")
solution3 = "{'a' : 2}"
print(f"{test3} should = {solution3}")


test4 = count_refactored("aba")
solution4 = "{'a': 2, 'b': 1}"
print(f"{test4} should = {solution4}")

test5 = count_refactored("")
solution5 = "{}"
print(f"{test5} should = {solution5}")

test6 = count_refactored("aa")
solution6 = "{'a' : 2}"
print(f"{test6} should = {solution6}")
