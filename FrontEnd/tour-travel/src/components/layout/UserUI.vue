<template>
  <div class="user-page-container d-flex flex-column">
    <div class="user-detail-container d-flex">
      <div class="left-content d-flex flex-column">
        <div class="left-content-header d-flex">
          <div></div>
          <label>Username</label>
        </div>
        <div class="left-content-body">
          <div class="profile-items d-flex flex-column">
            <div class="d-flex">
              <div class="profile-items-icon"></div>
              <label>My Account</label>
            </div>
            <div class="list-items">
              <div :style="{'font-weight': editProfile ? 'bold' : 'lighter'}" class="choose-edit" @click="chooseEditProfile">Profile</div>
              <div class="choose-edit" @click="chooseEditPassword()" :style="{'font-weight': editPassword ? 'bold' : 'lighter'}">Change Password</div>
            </div>
          </div>
          <div class="history-items d-flex flex-column">
            <div class="d-flex">
              <div class="history-items-icon"></div>
              <label>Purchase Order</label>
            </div>
            <div class="list-items">
              <div class="choose-edit" @click="chooseEditCart" :style="{'font-weight': editCart? 'bold' : 'lighter'}">Cart</div>
            </div>
          </div>
        </div>
      </div>
      <div class="right-content">
        <div class="edit-profile detail-container" v-if="editProfile">
          <div class="detail-header">
            <label>My Current Profile</label>
            <h3>Manage profile information for account security</h3>
          </div>
          <div class="profile-detail-body">
            <InputInfoTemplate
                item="Username"
                :can-editing="false"
                input-type="text"
                value="Team2"
                :is-only-alpha="false"
                :is-only-numeric="false"
                display-inline="inline-block"
            />
            <InputInfoTemplate
                item="Email"
                :can-editing="true"
                input-type="text"
                display-inline="inline-block"
            />
            <InputInfoTemplate
                item="Phone number"
                :can-editing="true"
                input-type="number"
                display-inline="inline-block"
            />
            <InputInfoTemplate
                item="Citizen identification"
                :can-editing="true"
                input-type="number"
                display-inline="inline-block"
            />
            <div>
              <span style="margin-right: 115px; padding: 16px 0px 6px 20px; font-size: 16px;">Gender</span>
              <input type="radio" id="male" value="male" v-model="gender" />
              <label for="male" class="gender">Male</label>
              <input type="radio" id="female" value="female" v-model="gender" />
              <label for="female" class="gender">Female</label>
              <input type="radio" id="other" value="other" v-model="gender" />
              <label for="other" class="gender">Other</label>
            </div>
            <InputInfoTemplate
                item="Birthday"
                :can-editing="true"
                display-inline="inline-block"
            />
            <div class="profile-detail-img"></div>
          </div>
          <div class="profile-detail-footer">
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
        <div class="edit-password detail-container" v-if="editPassword">
          <div class="detail-header">
            <label>Password</label>
            <h3>Please do not reveal your password</h3>
          </div>
          <div class="password-detail-body">
            <InputInfoTemplate
                item="Current Password"
                :can-editing="true"
                input-type="password"
                display-inline="inline-block"
            />
            <InputInfoTemplate
                item="New Password"
                :can-editing="true"
                input-type="number"
                display-inline="inline-block"
            />
            <InputInfoTemplate
                item="Confirm New Password"
                :can-editing="true"
                input-type="number"
                display-inline="inline-block"
            />
            <InputInfoTemplate
                item="Verify code"
                :can-editing="allowEnterCode"
                input-type="text"
                display-inline="inline-block"
            />
            <button
                class="btn-default"
                @click="receiveCode()"
            >
              Get code
            </button>
          </div>
        </div>
        <div class="edit-cart detail-container" v-if="editCart">
          <div class="edit-cart-list d-flex flex-column" v-for="item in historyTour" :key="item.id">
            <div class="tour-img" :style="{'background-image': item.img}"></div>
            <div class="cart-action d-flex flex-column">
              <label class="tour-info">{{ item.info }}</label>
              <div>
                <div>
                  <button
                      class="btn-default"
                      @click="showHistoryTourDetail(item)"
                  >
                    Detail
                  </button>
                </div>
                <div>
                  <button
                      class="btn-default"
                      @click="removeHistoryTour(item)"
                  >
                    Remove
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>
<script>
import InputInfoTemplate from "@/components/base/InputInfoTemplate";
import Footer from "@/components/layout/TheFooter";
export default {
  name: 'User',
  components: {
    InputInfoTemplate,
    Footer
  },
  data() {
    return {
      editProfile: false,
      editPassword: false,
      editCart: false,
      gender: null,
      allowEnterCode: false,
      historyTour: []
    }
  },
  methods: {
    handleUpdateProfile() {

    },
    receiveCode() {
      this.allowEnterCode = true
    },
    chooseEditPassword() {
      this.editPassword = true
      this.editProfile = false
      this.editCart = false
    },
    chooseEditProfile() {
      this.editPassword = false
      this.editProfile = true
      this.editCart = false
    },
    chooseEditCart() {
      this.editPassword = false
      this.editProfile = false
      this.editCart = true
    },
    getHistoryTour() {
      // call api get history tour of this user and assign to historyTour array
    },
    showHistoryTourDetail(tour) {
      console.log(tour)
    },
    removeHistoryTour(tour) {
      console.log(tour)
    }
  },
  mounted() {
    this.editProfile = true
    this.getHistoryTour()
  }
}
</script>
<style>
.user-page-container {
  width: 100vw;
  height: 93%;
  margin-top: 3%;
  align-items: center;
  justify-content: space-between;
}

.choose-edit {
  cursor: pointer;
}

label {
  font-weight: bold;
  font-size: 16px;
  margin-left: 10px;
}

h3 {
  margin-left: 10px;
  font-weight: lighter;
}
.user-detail-container {
  width: 80%;
  height: 60%;
  justify-content: space-between;
}

.right-content {
  width: 75%;
}

.left-content {
  width: 20%;
  padding: 40px 0px 40px 0px;
  justify-content: flex-start;
  align-items: center;
}

.left-content-header {
  width: 100%;
  height: 25%;
  justify-content: center;
  align-items: center;
  border-bottom: solid 2px #babec5;
  margin-bottom: 10%;
}
.left-content-header div {
  background-image: url(../../assets/imgs/Image/guest-32.png);
  height: 50px;
  width: 50px;
  border:  #949494 solid 1px;
  border-radius: 50%;
  margin-right: 25px;
  background-size: contain;
  background-repeat: no-repeat;
}

.left-content-header label {
  font-size: 18px;
}

.profile-detail-body {
  height: 370px;
}

.profile-items > :first-child, .history-items > :first-child {
  width: 100%;
  height: 25%;
  justify-content: flex-start;
  align-items: center;
}
.profile-items-icon {
  background-image: url(../../assets/imgs/Image/guest-32.png);
  height: 24px;
  width: 24px;
  background-size: contain;
  background-repeat: no-repeat;
}

.history-items-icon {
  background-image: url(../../assets/imgs/Image/list-ingredients-32.png);
  height: 24px;
  width: 24px;
  background-size: contain;
  background-repeat: no-repeat;
}

.list-items {
  width: fit-content;
  margin-left: 30px;
}

.list-items > div {
  font-size: 14px;
  margin-top: 10px;
  margin-bottom: 10px;
}

.detail-container {
  padding: 6px 20px 6px 6px;
  border: solid 2px #babec5;
  border-radius: 7px;
}
.detail-header {
  border-bottom: solid 2px #babec5;
}

.profile-detail-img {
  background-image: url(../../assets/imgs/Image/guest-32.png);
  height: 100px;
  width: 100px;
  background-size: contain;
  background-repeat: no-repeat;
  border: #949494 solid 1px;
  border-radius: 50%;
  position: relative;
  left: 75%;
  bottom: 270px;
  cursor: pointer;
}

.profile-detail-img::after {
  content: "Image limit 1MB, JPG, PNG";
  position: absolute;
  bottom: -50px;
  left: -30px;
  width: 200px;
}

.gender {
  font-weight: lighter;
  margin-right: 10%;
}

.profile-detail-footer {
  margin-left: 10px;
}

.btn-default {
  position: relative;
  left: 60%;
  bottom: 43px;
}

.edit-cart-list {

}
</style>