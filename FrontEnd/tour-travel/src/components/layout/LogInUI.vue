<template>
  <div class="login-page d-flex">
    <div class="login-form-container d-flex">
      <div class="d-flex flex-column">
        <div class="form-label d-flex">
          <div class="label-focus">
            <label>Sign in</label>
          </div>
          <div>
            <label @click="directToRegister">Register</label>
          </div>
        </div>
        <div class="form-info d-flex flex-column">
          <div class="form-info-input">
            <InputInfoTemplate
                item="Email"
                :can-editing="true"
                placeholder="Email"
                input-type="text"
                v-model="email"
                width-input="400px"
            />
            <InputInfoTemplate
                item="Password"
                :can-editing="true"
                placeholder="Password"
                input-type="password"
                v-model="password"
                width-input="400px"
            />
          </div>
          <div class="form-info-action d-flex flex-column">
            <div>
              <a href="#">Forgot password?</a>
            </div>
            <button class="btn" @click="handleSignIn()">Sign In</button>
          </div>
        </div>
      </div>
    </div>
    <div class="login-background d-flex flex-column">
<!--      <img src="../../assets/imgs/Image/bg_login.jpg">-->
    </div>
  </div>
</template>
<script>
import InputInfoTemplate from "@/components/base/InputInfoTemplate";
import AuthApi from "@/js/api/AuthApi";
export default {
  name: 'LogIn',
  components: {
    InputInfoTemplate
  },
  data() {
    return {
      email: null,
      password: null
    }
  },
  methods: {
    directToRegister() {
      this.$router.push({ path: '/register'})
    },
    async handleSignIn() {
      if (!this.email || !this.password) {
        this.$notify({
          group: 'default',
          title: 'Error',
          text: 'Please full email and password',
          duration: 3000,
          type: 'error',
          position: 'bottom right'
        })
      } else {
        if (!this.email.toLowerCase().match(
                /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
            )) {
          this.$notify({
            group: 'default',
            title: 'Error',
            text: 'Email was not valid!',
            duration: 4000,
            type: 'error',
            position: 'bottom right'
          })
        } else {
          let signInResponse = await AuthApi.signIn({
            email: this.email,
            password: this.password
          })
          if (signInResponse === 'No account with email existed!' || signInResponse === 'Wrong password!' || !signInResponse) {
            this.$notify({
              group: 'default',
              title: 'Error',
              text: signInResponse,
              duration: 4000,
              type: 'error',
              position: 'bottom right'
            })
          } else {
            this.$notify({
              group: 'default',
              title: 'Success',
              text: 'Log in success!',
              duration: 4000,
              type: 'success',
              position: 'bottom right'
            })
          }
        }
      }
    }
  }
}

</script>
<style scoped>
@import url(../../css/common/common.css);
.login-page {
  width: 100vw;
  height: 100%;
}

.login-form-container {
  width: 50%;
  justify-content: center;
  align-items: center;
}

.login-form-container > div:first-child {
  justify-content: center;
  border: solid 3px #ffc021;
  border-radius: 10px;
  padding: 20px 20px;
}

.form-label {
  justify-content: space-around;

}

.form-label > div {
  width: 50%;
  text-align: center;
}

label {
  cursor: pointer;
  font-size: 24px;
}

.label-focus {
  border-bottom: 2px solid #ffc021;
}

.label-focus > label {
  color: #ffc021;
  font-weight: bold;
}

.form-info-input {
  margin-top: 30px;
  margin-bottom: 40px;
  width: 100%;
}

.btn {
  margin-top: 15px;
  border-radius: 8px;
  background-color: #ffc021;
  font-size: 16px;
  font-weight: bolder;
}

.login-background {
  width: 50%;
  height: 100%;
  justify-content: center;
  background-image: url(../../assets/imgs/Image/bg_login.jpg);
  background-repeat: no-repeat;
  background-size: cover;
}
</style>