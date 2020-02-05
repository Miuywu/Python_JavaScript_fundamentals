#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
    console.log("Missing size");
} else {
    for (let a = 0; a < parseInt(process.argv[2]); a++) {
        let line = "";
        for (let b = 0; b < parseInt(process.argv[2]); b++) {
            line += "X";
        }
    console.log(line);
    }
}
