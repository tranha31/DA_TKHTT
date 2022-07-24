<template>
  <div class="user-page-container d-flex flex-column">
    <div class="user-detail-container d-flex">
      <div class="left-content d-flex flex-column">
        <div class="left-content-header d-flex">
          <div></div>
          <label>{{ userInfos ? userInfos.UserName : 'Username'}}</label>
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
            <div class="d-flex" @click="choosePurchareOrder" >
              <div class="history-items-icon"></div>
              <label style="cursor:pointer;">Purchase Order</label>
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
                :is-only-alpha="false"
                :is-only-numeric="false"
                display-inline="inline-block"
                v-model="userInfos.UserName"
            />
            <InputInfoTemplate
                item="Email"
                :can-editing="true"
                input-type="text"
                display-inline="inline-block"
                v-model="userInfos.Email"
            />
            <InputInfoTemplate
                item="Phone number"
                :can-editing="true"
                input-type="number"
                display-inline="inline-block"
                v-model="userInfos.PhoneNumber"
            />
            <InputInfoTemplate
                item="Citizen identification"
                :can-editing="true"
                input-type="number"
                display-inline="inline-block"
                v-model="userInfos.IdentityNumber"
            />
            <InputInfoTemplate
                item="Name"
                :can-editing="true"
                input-type="text"
                display-inline="inline-block"
                v-model="userInfos.Name"
            />
            <InputInfoTemplate
                item="Address"
                :can-editing="true"
                input-type="text"
                display-inline="inline-block"
                v-model="userInfos.Address"
            />
            <!-- <div>
              <span style="margin-right: 115px; padding: 16px 0px 6px 20px; font-size: 16px;">Gender</span>
              <input type="radio" id="male" value="male" v-model="gender" />
              <label for="male" class="gender">Male</label>
              <input type="radio" id="female" value="female" v-model="gender" />
              <label for="female" class="gender">Female</label>
              <input type="radio" id="other" value="other" v-model="gender" />
              <label for="other" class="gender">Other</label>
            </div> -->
            <!-- <InputInfoTemplate
                item="Birthday"
                :can-editing="true"
                display-inline="inline-block"
            /> -->
            <div class="profile-detail-img"></div>
          </div>
          <div class="profile-detail-footer">
            <div>
              <button
                  class="btn-default"
                  @click="handleUpdateProfile()"
                  style="position: relative; left: 1%; bottom: 20px;"
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
                v-model="editPasswordOld"
            />
            <InputInfoTemplate
                item="New Password"
                :can-editing="true"
                input-type="password"
                display-inline="inline-block"
                v-model="editPasswordNew"
            />
            <InputInfoTemplate
                item="Confirm New Password"
                :can-editing="true"
                input-type="password"
                display-inline="inline-block"
                v-model="editPasswordConf"
            />
            <InputInfoTemplate
                item="Verify code"
                :can-editing="allowEnterCode"
                input-type="text"
                display-inline="inline-block"
                v-model="verityCode"
            />
            <button
                class="btn-default"
                @click="receiveCode()"
            >
              Get code
            </button>
            <div>
              <button
                  class="btn-save-pass"
                  @click="handleUpdatePassword()"
              >
                Save
              </button>
            </div>
          </div>
        </div>
        <div class="edit-purchase detail-container" v-if="editPurchase">
          <div class="edit-cart-list d-flex w-full mb-30" v-for="item in listOrder" :key="item.id">
            <img class="tour-img w-half" :src="item.img">
            <div class="cart-action d-flex flex-column" style="padding-left:15px">
              <label class="tour-info">{{ item.info }}</label>
              <div class="flex-1"></div>
              <div class="d-flex">
                <div>
                  <button
                      class="btn-default"
                      @click="viewContract(item)"
                      style="position:unset"
                  >
                    View
                  </button>
                </div>
                <div>
                  <button
                      class="btn-default"
                      @click="editTour(item)"
                      style="position:unset"
                  >
                    Edit
                  </button>
                </div>
                <div v-if="item.status == 0">
                  <button
                      class="btn-default"
                      @click="deleteOrder(item)"
                      style="position:unset"
                  >
                    Delete
                  </button>
                </div>
                <div v-else>
                  <button
                      class="btn-default"
                      @click="cancelOrder(item)"
                      style="position:unset"
                  >
                    Cancel
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="edit-cart detail-container" v-if="editCart">
          <div class="edit-cart-list d-flex w-full mb-30" v-for="item in historyTour" :key="item.id">
            <img class="tour-img w-half" :src="item.img">
            <div class="cart-action d-flex flex-column" style="padding-left:15px">
              <label class="tour-info">{{ item.info }}</label>
              <div class="flex-1"></div>
              <div class="d-flex">
                <div>
                  <button
                      class="btn-default"
                      @click="showHistoryTourDetail(item)"
                      style="position:unset"
                  >
                    Detail
                  </button>
                </div>
                <div>
                  <button
                      class="btn-default"
                      @click="removeHistoryTour(item)"
                      style="position:unset"
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

    <TheCreateTour v-if="showForm"
    :oTour="oTour"
    :mode="2"
    :oData="oData"
    :TitleTour="'Khởi tạo tour'"
    v-on:closeForm="closeForm"
    />
    <BaseLoad :load="showLoad"/>
  </div>
</template>
<script>
import InputInfoTemplate from "@/components/base/InputInfoTemplate";
import Footer from "@/components/layout/TheFooter";
import TheCreateTour from '../../components/form/TheCreateTour.vue'
import BaseLoad from '../../components/base/BaseLoad.vue'
import AuthApi from "@/js/api/AuthApi";
import TourAPI from "@/js/api/tourapi";
import Tour from '../../js/entity/tour';
export default {
  name: 'User',
  components: {
    InputInfoTemplate,
    Footer,
    TheCreateTour,
    BaseLoad
  },
  data() {
    return {
      editProfile: false,
      editPassword: false,
      editCart: false,
      editPurchase: false,
      gender: null,
      allowEnterCode: false,
      historyTour: [],
      listOrder: [],
      userInfos: null,
      userInfosClone: null,
      editPasswordOld: null,
      editPasswordNew: null,
      editPasswordConf: null,
      verityCode: null,

      showLoad: false,
      showForm : false,
      oTour : new Tour(),
      oData: null,
    }
  },
  methods: {
    async handleUpdateProfile() {
      if (JSON.stringify(this.userInfos) !== JSON.stringify(this.userInfosClone)) {
        let updateResponse = await AuthApi.updateGeneralInfos({
          UserID: this.userInfos.UserID,
          Email: this.userInfos.Email,
          PhoneNumber: this.userInfos.PhoneNumber,
          Identification : this.userInfos.IdentityNumber,
          Name : this.userInfos.Name,
          Address: this.userInfos.Address
        })
        if (updateResponse) {
          this.$notify({
            group: 'default',
            title: 'Success',
            text: updateResponse,
            duration: 3000,
            type: 'success',
            position: 'bottom right'
          })
        }
      }
    },
    async handleUpdatePassword() {
      if (this.editPasswordNew !== this.editPasswordConf) {
        this.$notify({
          group: 'default',
          title: 'Error',
          text: 'Confirm password not match!',
          duration: 3000,
          type: 'error',
          position: 'bottom right'
        })
      } else if (this.editPasswordOld !== this.userInfos.Password) {
        this.$notify({
          group: 'default',
          title: 'Error',
          text: 'Current password not true!',
          duration: 3000,
          type: 'error',
          position: 'bottom right'
        })
      } else if (this.editPasswordOld === this.editPasswordNew) {
        this.$notify({
          group: 'default',
          title: 'Error',
          text: 'Old and New Password must be different!',
          duration: 3000,
          type: 'error',
          position: 'bottom right'
        })
      } else {
        let updatePasswordResponse = await AuthApi.updatePassword({
          UserID: this.userInfos.UserID,
          Password: this.editPasswordNew
        })

        if (updatePasswordResponse) {
          this.$notify({
            group: 'default',
            title: 'Success',
            text: updatePasswordResponse,
            duration: 3000,
            type: 'success',
            position: 'bottom right'
          })
        }
      }
    },
    receiveCode() {
      this.allowEnterCode = true
    },
    chooseEditPassword() {
      this.editPassword = true
      this.editProfile = false
      this.editCart = false
      this.editPurchase = false
    },
    chooseEditProfile() {
      this.editPassword = false
      this.editProfile = true
      this.editCart = false
      this.editPurchase = false
    },
    chooseEditCart() {
      this.editPassword = false
      this.editProfile = false
      this.editCart = true
      this.editPurchase = false
    },
    choosePurchareOrder(){
      this.editPassword = false
      this.editProfile = false
      this.editCart = false
      this.editPurchase = true
    },
    async getHistoryTour() {
      await TourAPI.getInCart(this.$store.state.account.currentUser.UserID)
      .then(res=>{
        this.historyTour = []
        var data = res.data.data
        var image = res.data.listImage
        for(var i=0; i<data.length; i++){
            var item = data[i]
            var img = image[i].Image
            var randIndex = Math.floor(Math.random() * img.length)
            var object = {
                id: item.TourID,
                img: img[randIndex],
                info: item.TourName,
                
            };
            this.historyTour.push(object)
        }
      })
    },

    async getListOrder(){
      await TourAPI.getTourOrder(this.$store.state.account.currentUser.UserID)
      .then(res=>{
        this.listOrder = []
        var data = res.data.data
        var image = res.data.listImage
        for(var i=0; i<data.length; i++){
            var item = data[i]
            var img = image[i].Image
            var randIndex = Math.floor(Math.random() * img.length)
            var object = {
                id: item.TourID,
                img: img[randIndex],
                info: item.TourName,
                status: item.Status,
            };
            this.listOrder.push(object)
        }
      })
    },

    showHistoryTourDetail(tour) {
      this.$router.push({ path: '/tour/'+tour.id})
    },
    async removeHistoryTour(tour) {
      await TourAPI.deleteInCart(tour.id, this.$store.state.account.currentUser.UserID)
      .then(()=>{
        this.getHistoryTour()
      })
      .catch(()=>{
        this.$notify({
          group: 'default',
          title: 'Error',
          text: 'Has error. Please try again!',
          type: 'error',
          position: 'bottom right'
        })
      })
    },
    async loadUserInformation() {
      this.userInfos = await AuthApi.getUserInformation({
        UserID: this.$store.state.account.currentUser.UserID
      })

      this.userInfosClone = JSON.parse(JSON.stringify(this.userInfos))
    },

    viewContract(tour){
      window.open("http://127.0.0.1:5000/tour/gettourtemp?id="+tour.id)
    },

    /**
     * Show form tạo tour
     */
    async editTour(tour){
      var id = tour.id
      this.showLoad = true
      await TourAPI.getByID(id)
      .then(res=>{
          var data = res.data
          var tour = new Tour();
          this.oTour = tour;
          this.oTour.Name = data.Master.TourName
          this.oTour.TourCode = data.Master.ContractCode
          this.oTour.CreatedTime = data.Master.CreatedTime
          this.oTour.TotalAmount = Number.parseInt(data.Master.TotalCost)
          this.oTour.Departure = data.Master.ProvinceDestinationName
          this.oTour.DepartureID = data.Master.ProvinceDestinationID
          this.oTour.StartPoint = data.Master.ProvinceStartName
          this.oTour.StartPointID = data.Master.ProvinceStartID
          this.oTour.PickUpPoint = data.Master.PickupAdress
          this.oTour.NumberAdult = Number.parseInt(data.Contract.NumberAdult)
          this.oTour.NumberChild = Number.parseInt(data.Contract.NumberChild)
          this.oTour.NumberBaby = Number.parseInt(data.Contract.NumberBaby)
          this.oTour.TotalDay = Number.parseInt(data.Contract.TotalHour)

          var pickupTime = new Date(data.Master.PickupTime)
          var startTime = new Date(data.Contract.StartTime)
          var endTime = new Date(data.Contract.EndTime)
          this.oTour.PickUpTime = new Date(pickupTime.setTime(pickupTime.getTime() - (7*60*60*1000)))
          this.oTour.StartTime = new Date(startTime.setTime(startTime.getTime() - (7*60*60*1000)))
          this.oTour.EndTime = new Date(endTime.setTime(endTime.getTime() - (7*60*60*1000)))
          
          this.oTour.Sample = data.Info.Sample
          this.oTour.Status = data.Info.Status
          this.oTour.IsPayment = data.Info.IsPayment
          this.oTour.TourID = data.Info.RefID
          
          data.Schedule.forEach(e=>{
              e.Morning.forEach(k=>{
                  var time = new Date(k.Time)
                  k.Time = new Date(time.setTime(time.getTime() - (7*60*60*1000)))
              })

              e.Afternoon.forEach(k=>{
                  var time = new Date(k.Time)
                  k.Time = new Date(time.setTime(time.getTime() - (7*60*60*1000)))
              })

              e.Evening.forEach(k=>{
                  var time = new Date(k.Time)
                  k.Time = new Date(time.setTime(time.getTime() - (7*60*60*1000)))
              })
          })

          data.AttachOption.forEach(e=>{
              e.Price = e.Price.toString()
                              .replace(/\D/g, "")
                              .replace(/\B(?=(\d{3})+(?!\d))/g, ".")
          })

          this.oData = data
          this.showForm = true;

          this.showLoad = false
      })
      .catch(()=>{
          this.showLoad = false
          this.$notify({
            group: 'default',
            title: 'Error',
            text: 'Has error. Please try again!',
            type: 'error',
            position: 'bottom right'
          })
      })
    },

    closeForm(){
      this.showForm = false;
      this.getListOrder()
    },
  },
  async mounted() {
    if (!this.$store.state.account.currentUser || (this.$store.state.account.currentUser && !this.$store.state.account.currentUser.UserID)) {
      this.$notify({
        group: 'default',
        title: 'Error',
        text: 'Please completed login first!',
        type: 'error',
        position: 'bottom right'
      })
      this.$router.push({ path: '/login'})
      return
    }
    await this.loadUserInformation()

    this.editProfile = true
    await this.getHistoryTour()
    await this.getListOrder()
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
  /* height: 370px; */
  padding: 10px 20px;
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
  left: 65%;
  bottom: 43px;
}

.edit-cart, .edit-purchase{
  height: 650px;
  overflow: auto;
}

.edit-cart-list {
  height: 300px;
}

.password-detail-body {
  padding: 10px 20px;
}

.btn-save-pass {
  background-color: #e89327;
  border: none;
  border-radius: 2px;
  padding: 4px 16px 4px 16px;
  cursor: pointer;
}
</style>