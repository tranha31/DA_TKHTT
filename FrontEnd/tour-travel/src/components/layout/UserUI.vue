<template>
  <div class="user-page-container d-flex flex-column">
    <div class="user-detail-container d-flex">
      <div class="left-content">
        <div class="left-content-header">
          <div>
            <img src="../../assets/imgs/Image/guest-32.png" />
          </div>
          <span>Username</span>
        </div>
        <div class="left-content-body">
          <div class="profile-items">
            <div>
              <div>
                <img src="../../assets/imgs/Image/guest-32.png" />
              </div>
              <span>My Account</span>
            </div>
            <div class="list-items">
              <div>Profile</div>
              <div>Change Password</div>
            </div>
          </div>
          <div class="history-items">
            <div>
              <div>
                <img src="../../assets/imgs/Image/list-ingredients-32.png" />
              </div>
              <span>Purchase Order</span>
            </div>
            <div class="list-items">
              <div>Cart</div>
            </div>
          </div>
        </div>
      </div>
      <div class="right-content">
        <div class="profile-detail-container" v-if="editProfile">
          <div class="profile-detail-header">
            <label>My Current Profile</label>
            <h3>Manage profile information for account security</h3>
          </div>
          <div class="profile-detail-body">
            <InputInfoTemplate
                item="Username"
                can-editing="false"
                input-type="text"
            />
            <InputInfoTemplate
                item="Email"
                can-editing="true"
                input-type="text"
            />
            <InputInfoTemplate
                item="Phone number"
                can-editing="true"
                input-type="number"
            />
            <InputInfoTemplate
                item="Citizen identification"
                can-editing="true"
                input-type="number"
            />
            <div>
              <input type="radio" id="male" value="male" v-model="gender" />
              <label for="male">Male</label>
              <input type="radio" id="female" value="female" v-model="gender" />
              <label for="female">Female</label>
              <input type="radio" id="other" value="other" v-model="gender" />
              <label for="other">Other</label>
            </div>
            <InputInfoTemplate
                item="Birthday"
                can-editing="true"
            />
            <div>
              <img src="../../assets/imgs/Image/guest-32.png" />
            </div>
            <div>
              <button
                  class="btn-default"
                  @click="handleUpdateProfile()"
              >
                SAVE
              </button>
            </div>
          </div>
        </div>
        <div v-if="editPassword">
          <div class="password-detail-header">
            <label>Password</label>
            <h3>Please do not reveal your password</h3>
          </div>
          <div class="password-detail-body">
            <InputInfoTemplate
                item="Current Password"
                can-editing="true"
                input-type="password"
            />
            <InputInfoTemplate
                item="New Password"
                can-editing="true"
                input-type="number"
            />
            <InputInfoTemplate
                item="Confirm New Password"
                can-editing="true"
                input-type="number"
            />
            <div>
              <button
                  class="btn-default"
                  @click="receiveCode()"
              >
                Get code
              </button>
            </div>
            <InputInfoTemplate
                item="Verify code"
                can-editing="true"
                input-type="text"
            />
          </div>
        </div>
        <div v-if="editCart"></div>
      </div>
    </div>
    <div class="user-page-footer">

    </div>
  </div>
</template>
<script>
import InputInfoTemplate from "@/components/base/InputInfoTemplate";
export default {
  name: 'User',
  components: {
    InputInfoTemplate
  },
  data() {
    return {
      editProfile: false,
      editPassword: false,
      editCart: false,
      gender: null
    }
  },
  methods: {
    handleUpdateProfile() {

    },
    receiveCode() {

    }
  },
  created() {
    this.editProfile = true
  }
}
</script>
<style>

</style>