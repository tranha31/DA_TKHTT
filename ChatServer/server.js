const express = require('express')
const app = express()

const http = require('http')
const server = http.createServer(app)
const io = require('socket.io')(server)

let users = {}

io.on('connection', (socket) => {
	// khi user lần đầu chat, sẽ emit requireConnect
	// các tin nhắn đầu tiên sẽ đc lưu luôn vào db
	// bên admin sẽ bắt event requireConnect và load chat room từ db
	socket.on('requireConnect', RoomID => {
		socket.emit('requireConnect', RoomID)
	})

	// khi user bắt đầu chat, sẽ emit userConnected
	// id của user sẽ đc thêm vào danh sách
	socket.on('userConnected', UserID => {
		users[UserID] = null
		users[UserID] = socket.id
		// socket.emit('userConnected', userID)
	})

	// khi user chat với admin, sẽ emit toAdmin
	// bên admin sẽ bắt event toAdmin
	socket.on('toAdmin', data => {
		io.emit('toAdmin', data)
	})

	// khi admin chat với user, sẽ emit toUser
	// bên user sẽ bắt event toUser
	socket.on('toUser', data => {
		let receiver = users[data.UserID]
		console.log('receiver:', receiver)
		io.to(receiver).emit('toUser', data.message)
	})
})

server.listen(3000, () => {
	console.log('listening on port 3000...')
})