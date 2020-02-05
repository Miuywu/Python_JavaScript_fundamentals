#!/usr/bin/node
let max = 0;
let max2 = 0;
for (let b = 2; b < process.argv.length; b++) {
  if (parseInt(process.argv[b]) > max) {
    max2 = max;
    max = parseInt(process.argv[b]);
  }
}
console.log(max2);
