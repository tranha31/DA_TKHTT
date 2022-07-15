const express = require('express')
const app = express()

const http = require('http')
const server = http.createServer(app)
const io = require('socket.io')(server)

io.on('connection', (socket) => {
	socket.on('msg', message => {
		io.emit('msg', message)
	})
})

server.listen(3000, () => {
	console.log('listening on port 3000...')
})