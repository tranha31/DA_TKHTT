<template>
  <div class="login-page-container">
    <div class="login-page d-flex">
      <div class="login-form-container d-flex">
        <div class="d-flex flex-column">
          <div class="form-label d-flex">
            <div>
              <label @click="directToLogin">Sign in</label>
            </div>
            <div class="label-focus">
              <label>Register</label>
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
              <InputInfoTemplate
                  item="Confirm Password"
                  :can-editing="true"
                  placeholder="Confirm Password"
                  input-type="password"
                  v-model="confirmPassword"
                  width-input="400px"
              />
              <InputInfoTemplate
                  item="Username"
                  :can-editing="true"
                  placeholder="Username"
                  input-type="text"
                  v-model="username"
                  width-input="400px"
              />
              <InputInfoTemplate
                  item="Phone Number"
                  :can-editing="true"
                  placeholder="Phone number"
                  input-type="number"
                  v-model="phoneNumber"
                  width-input="400px"
              />
              <div @click="showUploadSign = true" style="padding: 16px 0px 6px 20px;">
                Upload Signature
              </div>
            </div>
            <div class="form-info-action d-flex flex-column">
              <button class="btn" @click="handleRegisterNewUser()">Register new account</button>
            </div>
          </div>
        </div>
      </div>
      <div class="login-background d-flex flex-column">
<!--        <img src="../../assets/imgs/Image/bg_login.jpg">-->
      </div>
    </div>
    <Modal v-if="showUploadSign" :actions="[]">
      <div slot="header">
        <h3>Upload your signature</h3>
      </div>
      <template slot="body">
        <div class="upload-container">
          <div class="upload-display d-flex pb-6 mr-12 mb-20">
            <div class="display-area d-flex">
              <img v-if="signatureUrl" :src="signatureUrl" />
              <div v-else>Display area</div>
            </div>
            <div>
              <input type="file" @change="selectSignature" style="display: none" ref="signatureInput"/>
              <button class="btn-default" @click="$refs.signatureInput.click()">Upload</button>
            </div>
          </div>
          <div class="upload-commit mb-20">
            <input type="checkbox" id="checkbox" v-model="commitSignature" />
            <label for="checkbox">I commit that the signature is legally valid</label>
          </div>
        </div>
        <div class="list-buttons d-flex">
          <button
              slot="footer"
              style="background-color: #949494 !important"
              @click="showUploadSign = false"
              class="button-default"
          >
            CLOSE
          </button>
          <button
              slot="footer"
              @click="handleSaveUploadSign()"
              class="button-default"
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
import AuthApi from "@/js/api/AuthApi";
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
      commitSignature: false,
      signatureObject: null,
      signatureUrl: null
    }
  },
  watch: {
  },
  methods: {
    handleSaveUploadSign() {
      this.showUploadSign = false
    },
    directToLogin() {
      this.$router.push({ path: '/login'})
    },
    async handleRegisterNewUser() {
      if (!this.email || !this.password || !this.confirmPassword || !this.username || !this.phoneNumber) {
        this.$notify({
          group: 'default',
          title: 'Error',
          text: 'Enter all input fields!',
          duration: 3000,
          type: 'error',
          position: 'bottom right'
        })
      } else if (!this.email.toLowerCase().match(
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      )) {
        this.$notify({
          group: 'default',
          title: 'Error',
          text: 'Email was not valid!',
          duration: 3000,
          type: 'error',
          position: 'bottom right'
        })
      } else if (this.password !== this.confirmPassword) {
        this.$notify({
          group: 'default',
          title: 'Error',
          text: 'Confirm password not match!',
          duration: 3000,
          type: 'error',
          position: 'bottom right'
        })
      } else if (!this.signatureObject || !this.commitSignature) {
        this.$notify({
          group: 'default',
          title: 'Error',
          text: 'Must upload your signature and commit it!',
          duration: 3000,
          type: 'error',
          position: 'bottom right'
        })
      } else {
        const registerResponse = await AuthApi.register({
          email: this.email,
          password: this.password,
          username: this.username,
          phone: this.phoneNumber
        })

        if (registerResponse === 'Account with email already existed!') {
          this.$notify({
            group: 'default',
            title: 'Error',
            text: registerResponse,
            duration: 3000,
            type: 'error',
            position: 'bottom right'
          })
        } else {
          this.$notify({
            group: 'default',
            title: 'Success',
            text: 'Register new user success!',
            duration: 4000,
            type: 'success',
            position: 'bottom right'
          })
        }
      }
    },
    async selectSignature(event) {
      this.signatureObject = event.target.files[0]
      this.signatureUrl = URL.createObjectURL(this.signatureObject)
      console.log(this.signatureUrl)
    }
  }
}

</script>
<style scoped>
@import url(../../css/common/common.css);
.login-page-container {
  width: 100vw;
  height: 100%;
}

.login-page {
  width: 100%;
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

.upload-display {
  justify-content: space-between;
}

.upload-display > div:first-child {
  width: 70%;
  height: 200px;
}

.upload-commit > label {
  font-size: 16px;
}

.list-buttons {
  justify-content: flex-end;
}

.button-default {
  margin-left: 8px;
  background-color: #e89327;
  border: none;
  border-radius: 2px;
  padding: 4px 16px 4px 16px;
  cursor: pointer;
}

.display-area {
  border: solid #949494 1px;
  border-radius: 8px;
  justify-content: center;
  align-items: center;
}

.display-area > img {
  width: 90%;
  height: 90%;
}
</style>