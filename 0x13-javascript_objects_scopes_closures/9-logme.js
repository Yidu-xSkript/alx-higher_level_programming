#!/usr/bin/node
'use strict';
const log = [];
exports.logMe = function (item) {
  console.log(`${log.length}: ${item}`);
  log[log.length] = item;
};
