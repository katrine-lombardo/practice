/*
Your task is to sort a given string. Each word in the string will contain a
single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input
String will only contain valid consecutive numbers.
*/
// Any repeating characters
// Gabe would return true
// Blender return false

// STRATEGY
// Input: string containing one int (or empty)
// Output: rearranged original string
// Steps (starting with naive approach):
// 1. Splice string so that we can iterate through each word.
// 2. Create a variable to hold the list of digits in range 1-9.
// 3. Create an empty object to hold the new string order.
// 4. If the letter in the word is equal to the letter converted to integer, add
//    a key value pair to the object, where the letter is the key, and the value
//    is the word.
// 5. If the letter is not equal, pass to the next letter.
// 6. Create an empty string variable.
// 7. Append the object's values plus a space to the new string.
// 8. Return the new string minus the last index.

function order(words) {
  let wordObject = {};
  let wordArray = words.split(" ");

  for (let word of wordArray) {
    for (let letter of word) {
      if (parseInt(letter) > 0 && parseInt(letter) < 10) {
        wordObject[letter] = word;
      }
    }
  }
  const newSentence = Object.values(wordObject).join(" ");
  return newSentence;
}

function refactoredOrder(words) {
  if (words === "") {
    return "";
  }
  let wordArray = words.split(" ");
  let orderedWords = [];

  for (let word of wordArray) {
    const position = parseInt(word.match(/\d+/)[0]);
    orderedWords[position - 1] = word;
  }
  return orderedWords.join(" ");
}

// ---------------- TESTS ----------------

const test1 = order("is2 Thi1s T4est 3a");
console.log(`Thi1s is2 3a T4est = ${test1}`);

const test2 = order("4of Fo1r pe6ople g3ood th5e the2");
console.log(`Fo1r the2 g3ood 4of th5e pe6ople = ${test2}`);

const test3 = order("");
console.log(` = ${test3}`);

// ---------------- REFACTORED TESTS ----------------

const refactoredTest1 = refactoredOrder("is2 Thi1s T4est 3a");
console.log(`Thi1s is2 3a T4est = ${refactoredTest1}`);

const refactoredTest2 = refactoredOrder("4of Fo1r pe6ople g3ood th5e the2");
console.log(`Fo1r the2 g3ood 4of th5e pe6ople = ${refactoredTest2}`);

const refactoredTest3 = refactoredOrder("");
console.log(` = ${refactoredTest3}`);
