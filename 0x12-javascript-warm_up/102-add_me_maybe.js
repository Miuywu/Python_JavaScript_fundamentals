#!/usr/bin/node
const callMeMaybe = (number, theFunction) => {
  theFunction(number + 1);
};
exports.addMeMaybe = callMeMaybe;
