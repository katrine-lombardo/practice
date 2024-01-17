/*
Given two strings, find the number of common characters between them.

Example:
For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.
Strings have 3 common characters - 2 "a"s and 1 "c".
*/

// NOTES
// Each array's length < 15 characters (important to know for big-O)
// Edge cases could include empty arrays
// Doesn't specify upper or lower case

// STRATEGY
// First thought is a loop within a loop, which is bad for complexity but let's
// try it first.
// Create a counter variable to store our result
// Loop through each item in first array
// If the lowercase item from the first array is equal to the lowercase item in
// the second array, increment the counter variable
// Afterwards, remove that letter from the second array since it is "used up"
// Return the counter variable

function solution(s1, s2) {
  s1 = s1.toLowerCase();
  s2 = s2.toLowerCase();

  let matches = 0;

  for (let i = 0; i < s1.length; i++) {
    if (s2.includes(s1[i])) {
      matches++;
      s2 = s2.replace(s1[i], "");
    }
  }
  return matches;
}

const example1 = solution("aabcc", "adcaa");
console.log(`${example1} should be 3`);

const example2 = solution("zzzz", "zzzzzzz");
console.log(`${example2} should be 4`);

const example3 = solution("abca", "xyzbac");
console.log(`${example3} should be 3`);
