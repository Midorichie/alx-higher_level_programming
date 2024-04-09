#!/usr/bin/node
// class square that defines a square and inherits from Rectangle of 4-rectangle.js

const Rectangle = require('./4-rectangle');

module.exports = class square extends Rectangle {
	// a class square that defines a square
	
	constructor (size) {
		super(size, size);
	}
};
