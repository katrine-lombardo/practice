// Given a sequence of integers as an array, determine whether it is
// possible to obtain a strictly increasing sequence by removing no
// more than one element from the array.

// For sequence = [1, 3, 2, 1], the output should be
// solution(sequence) = false.
// There is no one element in this array that can be removed in order
// to get a strictly increasing sequence.

// For sequence = [1, 3, 2], the output should be
// solution(sequence) = true.
// You can remove 3 from the array to get the strictly increasing
// sequence [1, 2]. Alternately, you can remove 2 to get the strictly
// increasing sequence [1, 3].

// STRATEGY
// Loop through the array
// Create an empty container variable to pass in the temporary "tries"
// Create a true/false ticker variable
// Place all items into tempContainer and remove the num at current index
// Loop through the number range
// If the ticker is true, then break out the loop and return true
// If the ticker is false, empty the container variable and continue the loop

function solution(sequence) {
  for (let i = 0; i < sequence.length; i++) {
    let tempSequence = sequence.slice();
    tempSequence.splice(i, 1);

    let isIncreasing = true;
    for (let j = 0; j < tempSequence.length - 1; j++) {
      if (tempSequence[j] >= tempSequence[j + 1]) {
        isIncreasing = false;
        break;
      }
    }

    if (isIncreasing) {
      return true;
    }
  }
  return false;
}

const sample1 = solution([1, 3, 2, 1]); // --> false
console.log(sample1);

const sample2 = solution([1, 3, 2]); // --> true
console.log(sample2);

const sample3 = solution([1, 2, 1, 2]); // --> false
console.log(sample3);
