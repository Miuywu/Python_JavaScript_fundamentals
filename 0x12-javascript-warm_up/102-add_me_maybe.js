#!/usr/bin/node
const callMeMaybe = (number, theFunction) => {
  theFunction(number);
};
exports.addMeMaybe = callMeMaybe;
