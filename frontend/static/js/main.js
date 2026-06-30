const socket = io();

socket.on('connect', () => {
	socket.emit('get_data');
	console.log('Terhubung');
});

let marketData = null;

socket.on('market_data', (data) => {
	test(data);
});

const test = (data) => {
	console.log(data)
}