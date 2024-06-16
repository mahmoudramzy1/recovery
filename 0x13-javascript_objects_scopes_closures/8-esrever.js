#!/usr/bin/node
exports.esrever = function (list) {
  let n = 0;
  const listr = [];
  for (let i = list.length - 1; i >= list.length / 2; i--) {
    listr[n] = list[i];
    list[i] = list[n];
    list[n] = listr[n];
    n++;
  }
  return list;
};
