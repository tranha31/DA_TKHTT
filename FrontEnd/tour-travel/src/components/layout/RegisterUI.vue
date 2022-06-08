<template>
  <div class="login-page-container">
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
                  can-editing="true"
                  placeholder="Email"
                  input-type="text"
                  v-model="email"
              />
              <InputInfoTemplate
                  item="Password"
                  can-editing="true"
                  placeholder="Password"
                  input-type="password"
                  v-model="password"
              />
              <InputInfoTemplate
                  item="Confirm Password"
                  can-editing="true"
                  placeholder="Confirm Password"
                  input-type="password"
                  v-model="confirmPassword"
              />
              <InputInfoTemplate
                  item="Username"
                  can-editing="true"
                  placeholder="Username"
                  input-type="text"
                  v-model="username"
              />
              <InputInfoTemplate
                  item="Phone Number"
                  can-editing="true"
                  placeholder="Phone number"
                  input-type="number"
                  v-model="phoneNumber"
              />
              <div @click="showUploadSign = true" style="padding: 16px 0px 6px 20px;">
                Upload Signature
              </div>
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
    <Modal v-if="showUploadSign" :actions="[]">
      <div slot="header">
        <h3>Upload your signature</h3>
      </div>
      <template slot="body">
        <div class="upload-container">
          <div class="upload-display d-flex pb-6 mr-12">
            <div>Display area</div>
            <div>
              <button class="btn-default" @click="handleUploadSign()">Upload</button>
            </div>
          </div>
          <div class="upload-commit">
            <input type="checkbox" id="checkbox" v-model="commitSignature" />
            <label for="checkbox">I commit that the signature is legally valid</label>
          </div>
        </div>
        <div class="list-buttons d-flex">
          <button
              slot="footer"
              class="btn-default"
              style="background-color: #949494 !important"
              @click="showUploadSign = false"
          >
            CLOSE
          </button>
          <button
              slot="footer"
              class="btn-default"
              @click="handleSaveUploadSign()"
          >
            SAVE
          </button>
        </div>
      </template>
    </Modal>
  </div>
</template>
<script>
import InputInfoTemplate from "@/components/base/InputInfoTemplate";
import Modal from "@/components/base/Modal";
export default {
  name: 'Register',
  components: {
    InputInfoTemplate,
    Modal
  },
  data() {
    return {
      email: null,
      password: null,
      confirmPassword: null,
      username: null,
      phoneNumber: null,
      showUploadSign: false,
      commitSignature: false
    }
  },
  watch: {
  },
  methods: {
    handleUploadSign() {

    },
    handleSaveUploadSign() {
      this.showUploadSign = false
    }

  }
}

</script>
<style>
@import url(../../css/common/common.css);
.login-page-container {
  width: 100vw;
  height: 100%;
}

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

.form-label label {
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

.upload-display > :first-child {
  background-color: #949494;
  height: 200px;
  width: 200px;
  margin-right: 50px;
}

.list-buttons {
  margin-top: 20px;
  justify-content: flex-end;
}
</style>