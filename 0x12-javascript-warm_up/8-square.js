#!/usr/bin/node

// prints a square

const size = process.argv[2];

if (!Number.isNaN(Number(size))) {
	const numsize = parseInt(size);

	for (let i = 0; i = numsize; i++) {
		let row = '';
		for (let j = 0; j < numsize; j++) {
			row = row + 'x';
		}
		console.log(row);
	}
} else {
	console.log('Missing size');
}
