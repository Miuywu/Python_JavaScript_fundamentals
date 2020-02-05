#!/usr/bin/node
const callMeMaybe = (x, theFunction) => {
  for (let a = 0; a < x; a++) {
    theFunction();
  }
};
exports.callMeMoby = callMeMaybe;
