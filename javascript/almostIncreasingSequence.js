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

function solution(sequence) {}

const sample1 = solution([1, 3, 2, 1]);
console.log(sample1);

const sample2 = solution([1, 3, 2]);
console.log(sample2);

const sample3 = solution([1, 2, 1, 2]);
console.log(sample3);
