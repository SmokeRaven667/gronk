function solution(n) {
  let numString = n.toString();
  if (numString.length !== 2) {
    console.log("Please enter a two-digit number.");
  }
  return parseInt(numString[0]) + parseInt(numString[1]);
}

console.log(solution(56));
