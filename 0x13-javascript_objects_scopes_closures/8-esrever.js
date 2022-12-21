#!/usr/bin/node
'use strict';
exports.esrever = function (list) {
  const _list = [];
  let n = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    _list[n] = list[i];
    n++;
  }
  return _list;
}
