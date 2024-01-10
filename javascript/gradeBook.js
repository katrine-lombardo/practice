// Complete the function so that it finds the average of the three
// scores passed to it and returns the letter value associated with that grade.

// Numerical Score	Letter Grade
// 90 <= score <= 100	'A'
// 80 <= score < 90	'B'
// 70 <= score < 80	'C'
// 60 <= score < 70	'D'
// 0 <= score < 60	'F'
// Tested values are all between 0 and 100. Theres is no need to check for
// negative values or values greater than 100.

// STRATEGY
// Map out scores
// Add all nums together
// Divide sum by 3
// Return solution

function getGrade(s1, s2, s3) {
  const letterScores = {
    A: [90, 100],
    B: [80, 90],
    C: [70, 80],
    D: [60, 70],
    F: [0, 60],
  };

  let avg = (s1 + s2 + s3) / 3;

  for (let grade in letterScores) {
    let range = letterScores[grade];
    if (avg >= range[0] && avg <= range[1]) {
      return grade;
    }
  }
}

let example1 = getGrade(95, 90, 93);
console.log(example1);

let example2 = getGrade(70, 70, 100);
console.log(example2);

let example3 = getGrade(75, 70, 79);
console.log(example3);
