/*
Some people are standing in a row in a park. There are trees between them which
cannot be moved. Your task is to rearrange the people by their heights in a
non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] is the height of a person standing in the ith position.
*/

// NOTES
// Input: array of ints (peoples' heights) and -1 (indicates tree)
// Output: array of ints and -1
// Potential edge cases: List of only trees, empty lists
// Logic: I want to sort the list (doesn't specify if in place or not) but only
// the characters that do not equal -1.
// Steps:
// 1. I can loop through the list to extract values not equal to -1.
// 2. I can create a list to contain the indexes as a map for where the sorted
//    heights should be inserted.
// 3. I'll sort the values-only list by ascending value.
// 4. I'll loop through the original list and reassign the value at that index
//    to the new value from the values-only sorted list.

function solution(a) {}

const example1 = solution([-1, 150, 190, 170, -1, -1, 160, 180]);
console.log(`${example1} should = [-1, 150, 160, 170, -1, -1, 180, 190]`);

const example2 = solution([-1, -1, -1, -1, -1]);
console.log(`${example2} should = [-1, -1, -1, -1, -1]`);

const example3 = solution([-1]);
console.log(`${example3} should = [-1]`);
