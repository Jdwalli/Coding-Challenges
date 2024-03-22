const fs = require("fs");

regexPattern = /^(\d+)-(\d+) (\w): (\w+)$/;

function solvePartOne(data) {
  const arr = data.split("\n");
  validPasswords = 0;

  for (let i = 0; i < arr.length; i++) {
    const match = arr[i].trim().match(regexPattern);

    if (match) {
      min = parseInt(match[1]);
      max = parseInt(match[2]);
      targetChar = match[3];
      password = match[4];

      letterCount = 0;

      for (let charIndex = 0; charIndex < password.length; charIndex++) {
        if (password.charAt(charIndex) == targetChar) {
          letterCount++;
        }
      }

      if (letterCount >= min && letterCount <= max) {
        validPasswords++;
      }
    }
  }

  return validPasswords;
}

function solvePartTwo(data) {
  const arr = data.split("\n");
  validPasswords = 0;

  for (let i = 0; i < arr.length; i++) {
    const match = arr[i].trim().match(regexPattern);

    if (match) {
      firstIndexPos = parseInt(match[1]) - 1;
      secondIndexPos = parseInt(match[2]) - 1;
      targetChar = match[3];
      password = match[4];

      charactersFound = 0
      if (password.charAt(firstIndexPos) === targetChar) {
        charactersFound++
      }

      if (password.charAt(secondIndexPos) === targetChar) {
        charactersFound++
      }

      if (charactersFound == 1) {
        validPasswords++
      }

      
    }
  }

  return validPasswords;
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
