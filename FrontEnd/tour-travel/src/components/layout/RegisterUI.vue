<template>
  <div class="login-page d-flex">
    <div class="login-form-container d-flex">
      <div class="form-container d-flex flex-column">
        <div class="form-label d-flex">
          <div>
            <label>Sign in</label>
          </div>
          <div class="label-focus">
            <label>Register</label>
          </div>
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
            <InputInfoTemplate
                item="Confirm Password"
                is-editing="true"
                placeholder="Confirm Password"
                input-type="password"
                v-model="confirmPassword"
            />
            <InputInfoTemplate
                item="Username"
                is-editing="true"
                placeholder="Username"
                input-type="text"
                v-model="username"
            />
            <InputInfoTemplate
                item="Phone Number"
                is-editing="true"
                placeholder="Phone number"
                input-type="number"
                v-model="phoneNumber"
            />
          </div>
          <div class="form-info-action d-flex flex-column">
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
  name: 'Register',
  components: {
    InputInfoTemplate
  },
  data() {
    return {
      email: null,
      password: null,
      confirmPassword: null,
      username: null,
      phoneNumber: null
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
  width: 70%;
  height: 90%;
  border-radius: 14px;
  background-color: #ffffff;
  justify-content: flex-start;
}

.form-label {
  padding: 0px;
  justify-content: space-around;
}

.form-label > div {
  width: 50%;
  text-align: center;
  border-bottom: solid 2px #babec5;
}

label {
  width: 100%;
  height: 96px;
  font-size: 28px;
  cursor: pointer;
}

.label-focus {
  border-bottom: solid 4px #e89327 !important;
}

.form-info {
  justify-content: space-around;
  height: 100%;
}

.form-info-action {
  padding: 16px 20px 6px 20px;
  width: 100%;
  height: 100px;
  /*justify-content: space-around;*/
}

.btn {
  border: 1px solid #e89327;
  padding: 8px 20px;
  border-radius: 7px;
  cursor: pointer;
  font-size: 16px;
}
</style>