<template>
  <div class="chat-container d-flex">
    <div class="list-user d-flex flex-column">
        <div v-for="(e, i) in 3" v-bind:key="i" class="user d-flex">
            <div class="icon"></div>
            <div class="username">Tran Quang Ha</div>
        </div>
    </div>
    <div class="content-chat flex-1">
        <div class="content d-flex flex-column">
            <div class="message d-flex w-full user-message">
                <div class="content w-half">
                    AAA AAAA aaaaa  aaaaa aaaaaa
                </div>
                <div class="flex-1"></div>
            </div>
            <div class="message d-flex w-full admin-message">
                <div class="flex-1"></div>
                <div class="content w-half">aaaa aaaaa aaaa aaaa</div>
            </div>
        </div>
        <div class="input-message d-flex">
            <div class="attach"></div>
            <input type="text" />
            <div class="send"></div>
        </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
@import url(../../css/content/chat.css);
</style>