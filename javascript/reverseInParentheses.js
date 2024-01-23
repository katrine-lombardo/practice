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
// Strategy:
// 1. Determine the number of "parenthesed" strings (for testing).
// 2. Get the index location for each open-parenthesis and store in an array so
//    I know where to insert the substring.
// 3. Make an empty array to store each individual substring.
// 4. Double-check the number of substrings = step 1.
// 4. Reverse the order of the characters in the substrings.
// 5. Loop through the original array to replace substrings corresponding to the
//    index location from step 2.

function solution(inputString) {}

inputString0 = solution("(bar)");
print(`${inputString0} should = "rab"`);

inputString1 = solution("foo(bar)baz");
print(`${inputString1} should =  "foorabbaz"`);

inputString2 = solution("foo(bar)baz(blim)");
print(`${inputString2} should = "foorabbazmilb"`);

inputString3 = solution("foo(bar(baz))blim");
print(`${inputString3} should = "foobazrabblim"`);
