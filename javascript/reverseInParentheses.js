/*
Write a function that reverses characters in (possibly nested) parentheses in the input string.
Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
solution(inputString) = "rab";

For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";

For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb";

For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".
*/

// NOTES
// Input: string
// Output: string
// Edge cases: Are there spaces in a word, and how would that be reversed
// (trimmed?)? Nested parentheses should be noted. Empty parentheses. Large
// number of nested parentheses. The challenge alludes to wanting the characters
// reversed in-place rather than copied, but I would clarify that.
// Logic: I need to isolate each section of the string, and work from the
// inside-out to reverse in that specific order, and concatenate to the eventual
// result string.

// Strategy that worked:
// 1. Create an empty stack to keep track of the idx location of parentheses.
// 2. Create an empty str to store the final output.
// 3. Iterate through each character of the string to find those parentheses.
// 4. If the char is an open parenthesis, save the current state to the stack
//    and reset result to an empty string.
// 5. If the character isn't a parenthesis, add that character to the result.
// 6. If the char is a close parenthesis, pop the current state from the stack
//    and add the reversed characters to the result variable.

// (old) Strategy that did not work:
// 1. Determine the number of "parenthesed" strings (for testing).
// 2. Get the index location for each open-parenthesis and store in an array so
//    I know where to insert the substring.
// 3. Make an empty array to store each individual substring.
// 4. Double-check the number of substrings = step 1.
// 4. Reverse the order of the characters in the substrings.
// 5. Loop through the original array to replace substrings corresponding to the
//    index location from step 2.

function solution(inputString) {
  let stack = [];
  let result = "";

  for (let char of inputString) {
    if (char === "(") {
      stack.push(result);
      result = "";
    } else if (char === ")") {
      result = stack.pop() + result.split("").reverse().join("");
    } else {
      result += char;
    }
  }

  return result;
}

inputString0 = solution("(bar)");
console.log(`${inputString0} should = "rab"`);

inputString1 = solution("foo(bar)baz");
console.log(`${inputString1} should = "foorabbaz"`);

inputString2 = solution("foo(bar)baz(blim)");
console.log(`${inputString2} should = "foorabbazmilb"`);

inputString3 = solution("foo(bar(baz))blim");
console.log(`${inputString3} should = "foobazrabblim"`);
