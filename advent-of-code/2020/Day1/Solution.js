const fs = require("fs");

function solvePartOne(data) {
  const arr = data.split("\n");
  solution = 0;
  length = arr.length;

  for (let i = 0; i < length; i++) {
    for (let j = i + 1; j < length; j++) {
      if (parseInt(arr[i]) + parseInt(arr[j]) === 2020) {
        return parseInt(arr[i]) * parseInt(arr[j]);
      }
    }
  }

  return 0;
}

function solvePartTwo(data) {
  const arr = data.split("\n");
  length = arr.length;

  for (let i = 0; i < length; i++) {
    for (let j = i + 1; j < length; j++) {
      for (let k = j + 1; k < length; k++) {
        if (
          i !== j &&
          parseInt(arr[i]) + parseInt(arr[j]) + parseInt(arr[k]) == 2020
        ) {
          return parseInt(arr[i]) * parseInt(arr[j]) * parseInt(arr[k]);
        }
      }
    }
  }
  return 0;
}

fs.readFile("input.txt", "utf8", (err, data) => {
  if (err) {
    console.error("Error reading the file:", err);
    return;
  }
  const cleanedData = data.replace(/\r/g, "");
  console.log("Part One Solution: " + solvePartOne(cleanedData));
  console.log("Part Two Solution: " + solvePartTwo(cleanedData));
});
