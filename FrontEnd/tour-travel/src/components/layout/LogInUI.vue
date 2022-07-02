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
            <button class="btn">Sign In</button>
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