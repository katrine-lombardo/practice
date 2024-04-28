/*
Your job is to write a function which increments a string, to create a new
string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the
new string. Examples:

foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100
*/

// STRATEGY
// Input: string possibly ended with integer(s)
// Output: string ended with incremented integer(s)
// Steps:
// 1. Determine wither the string contains any digits.
// 2. Split the string to separate the digit and convert to integer.
// 3. Join the string to the string-converted integer.

function incrementString(strng) {
    strng.toLowerCase();
    const letters = strng.split("")
}

// TESTS
const test1 = incrementString("foobar000");
console.log(`${test1} = foobar001`);
const test2 = incrementString("foobar999");
console.log(`${test2} = foobar1000`);
