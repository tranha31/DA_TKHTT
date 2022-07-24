<template>
  <div>
    <div class="form-background"></div>
    <div class="login d-flex">
        <div class="content d-flex flex-column">
            <div class="mb-20 font-bold">Username</div>
            <input type="text" class="mb-20" v-model="userName">
            <div class="mb-20 font-bold">Password</div>
            <input type="password" class="mb-20" v-model="passWord">
            <div class="flex-1"></div>
            <div class="btn btn-save btn-login" @click="login">Login</div>
        </div>
    </div>
  </div>
</template>

<script>
import UserAPI from "../js/api/userapi";
export default {
    data(){
        return{
            userName : "",
            passWord : "",
        }
    },
    methods:{
        async login(){
            if(!this.userName || !this.passWord){
                this.$notify({
                    group: 'default',
                    title: 'Error',
                    text: 'Please full username and password!',
                    duration: 4000,
                    type: 'error',
                    position: 'bottom right'
                })
            }
            else{
                var data = {
                    "username": this.userName,
                    "password": this.passWord
                }
                data = JSON.stringify(data)
                await UserAPI.getAdmin(data)
                .then(res=>{
                    if(res.data.error){
                        this.$notify({
                            group: 'default',
                            title: 'Error',
                            text: res.data.error,
                            duration: 4000,
                            type: 'error',
                            position: 'bottom right'
                        })
                    }
                    else{
                        var id = res.data.data.RefID
                        sessionStorage.setItem("idAdmin", id);
                        this.$router.push({path : '/admin/tourrequest'});
                    }
                })
            }
        }
    }
}
</script>

<style>
.login{
    position: fixed;
    left: 0;
    top: 0;
    height: 100vh;
    width: 100vw;
    z-index: 1000;
    align-items: center;
    justify-content: center;
}
.form-background{
    position: fixed;
    width: 100vw;
    height: 100vh;
    background: rgba(0,0,0,.4);
    opacity: 0.5;
}

.login .content{
    width: 500px;
    height: 300px;
    background-color: #fff;
    border-radius: 5px;
    padding: 20px
}

.login .content input{
    height: 36px;
    padding: 5px;
    border: 1px solid #babec5;
    border-radius: 3px;
}

.login .content .btn-login{
    height: 50px;
    font-size: 20px;
    text-align: center;
}

</style>