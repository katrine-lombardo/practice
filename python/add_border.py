"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture =  ["abc",
            "ded"]
the output should be

solution(picture) = ["*****",
                     "*abc*",
                     "*ded*",
                     "*****"]
"""


def solution(picture):
    framed_picture = []
    picture_width = len(picture[0])
    framed_picture_width = picture_width + 2
    framed_picture.append("*" * framed_picture_width)
    for row in picture:
        pic_plus_frame = "*" + row + "*"
        framed_picture.append(pic_plus_frame)
    framed_picture.append("*" * framed_picture_width)
    return framed_picture


def refactored_solution(picture):
    return (
        ["*" * (2 + len(picture[0]))]
        + [f"*{row}*" for row in picture]
        + ["*" * (2 + len(picture[0]))]
    )


# ------- TESTS -------
print("-------TESTS-------")
picture1 = ["abc", "ded"]
solution1 = ["*****", "*abc*", "*ded*", "*****"]
test1 = solution(picture1)

picture2 = ["a"]
solution2 = ["***", "*a*", "***"]
test2 = solution(picture2)

picture3 = ["aa", "**", "zz"]
solution3 = ["****", "*aa*", "****", "*zz*", "****"]
test3 = solution(picture3)

if test1 == solution1 and test2 == solution2 and test3 == solution3:
    print("Yay! All tests passed")
else:
    print("Errors")


test4 = refactored_solution(picture1)
test5 = refactored_solution(picture2)
test6 = refactored_solution(picture3)


if test4 == solution1 and test5 == solution2 and test6 == solution3:
    print("Yay! All refactored tests passed")
else:
    print("Refactored errors")
