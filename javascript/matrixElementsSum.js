// After becoming famous, the CodeBots decided to move into a new building
// together. Each of the rooms has a different cost, and some of them are free,
// but there's a rumour that all the free rooms are haunted! Since the CodeBots
// are quite superstitious, they refuse to stay in any of the free rooms, or
// any of the rooms below any of the free rooms.

// Given matrix, a rectangular matrix of integers, where each value represents
// the cost of the room, your task is to return the total sum of all rooms that
// are suitable for the CodeBots (ie: add up all the values that don't appear
// below a 0).

// Example: For matrix = [
//           [0, 1, 1, 2],
//           [0, 5, 0, 0],
//           [2, 0, 3, 3]]
// the output should be
// solution(matrix) = 9.

// STRATEGY
// Input: Array of arrays
// Output: Integer
// Note: Each array will be the same length
//
// We'll want to loop through each element in each array
// If there is a zero, that index should be tracked to ignore in the next loop
// W'll use a tracker variable to track indexes to ignore (array)
// If the index is equal to an index in the tracker variable, do not count
// Else, we'll want to increment the room result tracker variable (integer)
// I want to add a condition where if each index is accounted for in the array,
// immediately break out and return the counter variable instead of continuing
// to loop.
// Edge cases: Single-room floors (array length = 1), single-story buildings

function solution(matrix) {
  let indexTracker = [];
  let roomTracker = 0;

  for (let i = 0; i < matrix.length; i++) {
    if (matrix[i].length === indexTracker.length) {
      break;
    }
    for (let j = 0; j < matrix[i].length; j++) {
      if (!indexTracker.includes(j)) {
        roomTracker += matrix[i][j];
        if (matrix[i][j] === 0) {
          indexTracker.push(j);
        }
      }
    }
  }
  return roomTracker;
}

let sample1 = solution([
  [0, 1, 1, 2],
  [0, 5, 0, 0],
  [2, 0, 3, 3],
]);
console.log(`${sample1} should be 9`);

let sample2 = solution([
  [1, 1, 1, 0],
  [0, 5, 0, 1],
  [2, 1, 3, 10],
]);
console.log(`${sample2} should be 9`);

let sample3 = solution([
  [1, 1, 1],
  [2, 2, 2],
  [3, 3, 3],
]);
console.log(`${sample3} should be 18`);

let sample4 = solution([[5], [3], [0], [2], [2]]);
console.log(`${sample4} should be 8`);
