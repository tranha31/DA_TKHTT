<template>
  <div class="login-page d-flex">
    <div class="login-form-container d-flex">
      <div class="form-container d-flex flex-column">
        <div class="form-label">
          <label>Sign in</label>
        </div>
        <div class="form-info d-flex flex-column">
          <div class="form-info-input">
            <InputInfoTemplate
                item="Email"
                is-editing="true"
                placeholder="Email"
                input-type="text"
                v-model="email"
            />
            <InputInfoTemplate
                item="Password"
                is-editing="true"
                placeholder="Password"
                input-type="password"
                v-model="password"
            />
          </div>
          <div class="form-info-action d-flex flex-column">
            <div>
              <a href="#">Forgot password?</a>
            </div>
            <button class="btn">Sign In</button>
            <button class="btn">Register new account</button>
          </div>
        </div>
      </div>
    </div>
    <div class="login-background d-flex flex-column">
      <img src="../../assets/imgs/Image/bg_login.jpg">
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
  }
}

</script>
<style>
@import url(../../css/common/common.css);
.login-page {
  width: 100vw;
  height: 100%;
}

.login-form-container {
  width: 50%;
  height: 100%;
  justify-content: center;
  align-items: center;
}

.login-background {
  width: 50%;
  height: 100%;
  justify-content: center;
}

img {
  max-width: 100%;
  max-height: 100%;
  min-height: 99.5%;
}

.form-container {
  width: 60%;
  height: 70%;
  border-radius: 14px;
  background-color: #ffffff;
  justify-content: flex-start;
}

.form-label {
  border-bottom: solid 2px #01B075;
  padding: 6px 0px 6px 20px;
}

label {
  width: 100%;
  height: 96px;
  font-size: 32px;
}

.form-info {
  justify-content: space-around;
  height: 80%;
}

.form-info-action {
  padding: 16px 20px 6px 20px;
  width: 100%;
  height: 140px;
  justify-content: space-around;
}

.btn {
  border: 1px solid #01B075;
  padding: 8px 20px;
  border-radius: 18px;
  cursor: pointer;
  background-color: #ffffff;
  font-size: 16px;
}
</style>