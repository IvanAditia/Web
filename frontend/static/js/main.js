const socket = io();

socket.on('connect', () => {
	socket.emit('get_data');
	console.log('Terhubung');
});

socket.on('market_data', (harga) => {
	test(harga);
});

const test = (harga) => {
	console.log(harga.isi.length)
	console.log(harga)
}