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
export default {
  name: 'ChatBox',
  components: {
    PerfectScrollbar
  },
  data() {
    return {
      showChatBox: false,
      currentMsg: null,
      sentMsg: [],
      receivedMsg: [],
      allMsg: [
        {
          Content: 'Ha lau, kan wo',
          Owner: 'user',
          Time: '2022-07-15 10:10:10',
          TypeOfContent: '0',
          RoleInConversation: '1'
        },
        {
          Content: 'Ni shi hai pa shen me',
          Owner: 'user',
          Time: '2022-07-15 10:10:12',
          TypeOfContent: '0',
          RoleInConversation: '1'
        },
        {
          Content: 'shen me di lao tian huang. ji mo cai shuo ai dao di ai de gai bu gai',
          Owner: 'admin',
          Time: '2022-07-15 10:10:13',
          TypeOfContent: '0',
          RoleInConversation: '0'
        },
        {
          Content: 'shen me ti jiu tian zhang',
          Owner: 'user',
          Time: '2022-07-15 10:10:14',
          TypeOfContent: '0',
          RoleInConversation: '1'
        }
      ]
    }
  },
  methods: {
    sendMsg() {
      this.allMsg.push({
        Content: this.currentMsg,
        Owner: 'user',
        Time: new Date(),
        TypeOfContent: '0',
        RoleInConversation: '1'
      })
      this.currentMsg = null
    },
    async addFile() {

    }
  }
}
</script>

<style scoped>
.chat-box-container {
  position: absolute;
  left: 90%;
  top: 1220px;
  cursor: pointer;
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