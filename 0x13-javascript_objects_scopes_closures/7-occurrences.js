#!/usr/bin/node
'use strict';
exports.nbOccurences = function (list, searchElement) {
  return list.filter(element => element === searchElement).length;
}
