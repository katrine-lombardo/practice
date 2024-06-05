/*
The challenge: Write a function which multiplies two numbers, without using the
multiplication symbol " * ".
*/

// input: two integers
// output: one integer
// strategy:
// 1. Create empty variable to store result
// 2. Iterate through a range starting at 1 and ending at the second number
// 3. For each number in the range, increment the empty variable by the amount
//    equal to the first given number
// 4. Return the empty variable

function multiply(num, toNum) {
  var product = 0;
  for (var i = 1; i <= toNum; i++) {
    product += num;
  }

  return product;
}

console.log(multiply(2, 5));
console.log(multiply(2, 3));
console.log(multiply(0, 0));
