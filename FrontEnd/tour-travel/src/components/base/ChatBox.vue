<template>
  <div class="chat-box-container d-flex">
    <div v-if="showChatBox" class="chat-box mr-12">
      <div class="chat-box-header d-flex">
        <label>Admin</label>
        <label class="close-chat-box" style="cursor: pointer" @click="showChatBox = false">X</label>
      </div>
      <div class="chat-box-body d-flex">
        <perfect-scrollbar>
          <div v-for="(msg, index) in allMsg" :key="index" :class="{'msg-user': msg.Owner === 'user', 'msg-admin': msg.Owner === 'admin'}">
            {{ msg.Content }}
          </div>
        </perfect-scrollbar>
      </div>
      <div class="chat-box-footer d-flex">
        <div class="add-file" @click="addFile()"></div>
        <input type="text" v-model="currentMsg" @keyup.enter="sendMsg()"/>
        <div class="send-msg" @click="sendMsg()"></div>
      </div>
    </div>
    <div class="chat-action" @click="showChatBox = !showChatBox"></div>
  </div>
</template>

<script>
import {PerfectScrollbar} from 'vue2-perfect-scrollbar'
import ChatApi from "@/js/api/ChatApi";
export default {
  name: 'ChatBox',
  components: {
    PerfectScrollbar
  },
  props: {
    positionLeft: {
      type: String,
      default: '90%'
    },
    positionTop: {
      type: String,
      default: '1220px'
    }
  },
  data() {
    return {
      showChatBox: false,
      currentMsg: null,
      sentMsg: [],
      receivedMsg: [],
      allMsg: [],
    }
  },
  methods: {
    async sendMsg() {
      if (this.sentMsg.length <= 0) {
        if (!this.$store.state.account.currentUser.ChatRoomID) {
          await ChatApi.createNewChat({ UserID: this.$store.state.account.currentUser.UserID })
          let newRoomResponse = await ChatApi.getUserChatRoom({ UserID: this.$store.state.account.currentUser.UserID })

          if (newRoomResponse) {
            this.$store.commit('account/setAccounts', {
              UserID: this.$store.state.account.currentUser.UserID,
              UserName: this.$store.state.account.currentUser.UserName,
              ChatRoomID: newRoomResponse ? newRoomResponse.RefID : null
            })

            this.$socket.emit('requireConnect', newRoomResponse.RefID)
            this.sentMsg.push(this.currentMsg)
          } else {
            this.$notify({
              group: 'default',
              title: 'Error',
              text: 'Error when chat to Admin!',
              duration: 4000,
              type: 'error',
              position: 'bottom right'
            })
          }
        } else {
          this.$socket.emit('userConnected', this.$store.state.account.currentUser.UserID)
          this.sentMsg.push(this.currentMsg)
        }
      }

      let willSendMsg = {
        Content: this.currentMsg,
        Owner: 'user',
        Time: new Date(),
        TypeOfContent: '0',
        RoleInConversation: '1'
      }

      this.allMsg.push(willSendMsg)
      this.$socket.emit('toAdmin', {
        UserID: this.$store.state.account.currentUser.UserID,
        RoomID: this.$store.state.account.currentUser.RoomID,
        message: willSendMsg
      })
      this.currentMsg = null
    },
    async addFile() {

    },
    handleReceivedMsg(msg) {
      console.log('msg:', msg)
      this.allMsg.push(msg)
    }
  },
  mounted() {
    this.sockets.subscribe('toUser', msg => {
      this.handleReceivedMsg(msg)
    })
  }
}
</script>

<style scoped>
.chat-box-container {
  position: fixed;
  cursor: pointer;
  top: 305px;
  right: 100px;
}

.chat-action {
  background-image: url(../../assets/imgs/Image/chat.png);
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  width: 48px;
  height: 48px;
  background-color: #EB4747;
  border-radius: 50%;
}

.chat-box {
  width: 300px;
  height: 400px;
  background-color: #ffffff;
  position: absolute;
  right: 50px;
  top: -160px;
  border: solid #babec5 1px;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  border-bottom: none;
  box-shadow: -5px 0px 5px 0px #e8e7e6;
}

.chat-box-header {
  background-color: #151B40;
  color: #ffffff;
  height: 10%;
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
  justify-content: space-between;
  padding: 0 10px;
  align-items: center;
}

.chat-box-body {
  height: 77%;
  padding: 0 10px;
}

.chat-box-footer {
  height: 13%;
  align-items: center;
  padding: 0 10px;
  justify-content: space-between;
  box-shadow: 0px -2px 6px 0px #e8e7e6;
}

.add-file {
  background-image: url(../../assets/icons/add-svgrepo-com.svg);
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  width: 20px;
  height: 20px;
}

.send-msg {
  background-image: url(../../assets/icons/send-svgrepo-com.svg);
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  width: 20px;
  height: 20px;
}

.msg-user {
  background-color: #ffc021;
  border-radius: 8px;
  padding: 5px;
  width: fit-content;
  margin: 5px 0;
  max-width: 220px;
}

.msg-admin {
  background-color: #949494;
  border-radius: 8px;
  padding: 5px;
  width: fit-content;
  max-width: 220px;
  margin: 5px 0;
}
</style>