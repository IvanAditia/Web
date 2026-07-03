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

const popup = document.getElementById('popup')

function openInput(){
	popup.classList.add('show')
}

function closeInput(){
	popup.classList.add('hidden')
}
