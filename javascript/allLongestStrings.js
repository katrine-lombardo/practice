/* Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].
*/

// STRATEGY
// Input: Array of strings
// Output: Array of string(s)
// Find item in the array with the max length
// Return a filtered list containing only items of that length

function solution(inputArray) {
  const inputLengthArray = inputArray.map((word) => word.length);
  const longestWord = Math.max(...inputLengthArray);
  const longestWordArray = inputArray.filter(
    (word) => word.length === longestWord
  );
  return longestWordArray;
}

const example1 = solution(["aba", "aa", "ad", "vcd", "aba"]);
console.log(`${example1} should be ["aba", "vcd", "aba"]`);

const example2 = solution(["aa"]);
console.log(`${example2} should be ["aa"]`);

const example3 = solution(["abc", "eeee", "abcd", "dcd"]);
console.log(`${example3} should be ["eeee", "abcd"]`);
