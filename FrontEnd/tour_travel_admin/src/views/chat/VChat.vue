<template>
  <div class="chat-container d-flex">
    <div class="list-user d-flex flex-column">
        <div v-for="(room, index) in allChatRoom" :key="index" class="user d-flex">
            <div class="icon"></div>
            <div class="username">{{room.UserName}}</div>
        </div>
    </div>
    <div class="content-chat flex-1">
        <div class="content d-flex flex-column">
            <div
                class="message d-flex w-full"
                v-for="(message, index) in allMsg"
                :key="index"
                :class="{'user-message': message.Owner === 'user', 'admin-message': message.Owner === 'admin'}"
            >
              <div class="flex-1" v-if="message.Owner === 'admin'"></div>
              <div class="content w-half">
                {{message.Content}}
              </div>
              <div class="flex-1" v-if="message.Owner === 'user'"></div>
            </div>
        </div>
        <div class="input-message d-flex">
            <div class="attach"></div>
            <input type="text" v-model="currentMsg" @keyup.enter="handleSendMsg()"/>
            <div class="send" @click="handleSendMsg()"></div>
        </div>
    </div>
  </div>
</template>

<script>
import ChatAPI from '../../js/api/chat'
import UserAPI from '../../js/api/user'
export default {
  name: 'VChat',
  data() {
    return {
      allMsg: [],
      currentMsg: null,
      allChatRoom: [],
      currentChatUser: null
    }
  },
  methods: {
    handleReceivedMsg(msg) {
      this.allMsg.push(msg.message)
    },
    handleSendMsg() {
      if (this.currentMsg && this.currentMsg !== '') {
        let willSendMsg = {
          Content: this.currentMsg,
          Owner: 'admin',
          Time: new Date(),
          TypeOfContent: '0',
          RoleInConversation: '0'
        }
        this.allMsg.push(willSendMsg)
        this.currentMsg = null
        this.$socket.emit('toUser', {
          UserID: this.currentChatUser.UserID,
          message: willSendMsg
        })
      }
    },
    async initData() {
      let chatRooms = await ChatAPI.getAllChatRoomByAmount(10);

      let allUsersID = ''
      chatRooms.data.forEach(room => {
        allUsersID = allUsersID + room.UserID + ', '
      })

      let allUsersResponse = await UserAPI.getAllUsersByListID(allUsersID.substring(0, allUsersID.length - 2))
      let allUsers = allUsersResponse.data

      this.allChatRoom = chatRooms.data
      this.allChatRoom.forEach(room => {
        room.UserName = allUsers.filter(user => user.UserID === room.UserID)[0].UserName
      })
      this.currentChatUser = this.allChatRoom[0]
    }
  },
  async mounted() {
    if (!sessionStorage.getItem("idAdmin")) {
      this.$router.push({ path: '/admin/login'})
      return
    }
    else{
      await this.initData()
      this.sockets.subscribe('toAdmin', msg => {
        this.handleReceivedMsg(msg)
      })
    }
    
  }
}
</script>

<style>
@import url(../../css/content/chat.css);
</style>