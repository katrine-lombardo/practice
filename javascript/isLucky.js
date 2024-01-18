/*
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false.
*/

// STRATEGY
// Input: int
// Output: bool
// Notes: Edge cases could include 1-digit integers, or odd-numbered length of
// integers (though codeSignal confirms that it will always be even).
// Logic:
// I can convert the int to a string to produce the two slices.
// I could alternatively use concatenate and the index number at half the length
// of the string.
// To sum each number in the int individually, I can loop through each half one
// time and store the sum in a counter variable.
// The final test is if the sums equal one another.

function solution(n) {}

const example1 = solution(1230);
console.log(`${example1} should = true`);

const example2 = solution(239017);
console.log(`${example2} should = false`);

const example3 = solution(134008);
console.log(`${example3} should = true`);
