<template>
  <div class="form-container d-flex">
      <div class="form-background"></div>
      <div class="form-main d-flex flex-column">
          <div class="header">{{title}}</div>
          <div class="icon-close" @click="closeForm">X</div>
          <div class="d-flex flex-column content">
            <div class="common-infor d-flex flex-column m-b-20" id="contentForm">
                <div class="d-flex">
                    <BaseInput
                    :clas="'w-half m-b-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Tên'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="false"
                    :maxLength="150"
                    :disabled="disabled"
                    :content="oDestination.name"
                    v-on:changeData="(value)=>{this.oDestination.name = value}"
                    />

                    <BaseInput
                    :clas="'w-half m-b-20'"
                    :hasTitle="true"
                    :title="'Địa chỉ'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="false"
                    :maxLength="500"
                    :disabled="disabled"
                    :content="oDestination.address"
                    v-on:changeData="(value)=>{this.oDestination.address = value}"
                    />
                </div>
                
                <div class="d-flex m-b-20">
                    <BaseAutoComplete
                    :clas="'w-half m-r-20'"
                    :hasTitle="true"
                    :title="'Tỉnh'"
                    :notNull="true"
                    :msrequire="true"
                    :placeholder="'Nhập tên tỉnh'"
                    :disable="disabled"
                    :content="oDestination.pronvinceName"
                    :dataFields="dataProvinceField"
                    :dataItem="lstProvince"
                    v-on:returnValue="chooseProvince"
                    />

                    <BaseAutoComplete
                    :clas="'w-half'"
                    :hasTitle="true"
                    :title="'Huyện'"
                    :notNull="true"
                    :msrequire="true"
                    :placeholder="'Nhập tên huyện'"
                    :disable="disabled"
                    :content="oDestination.districtName"
                    :dataFields="dataDistrictField"
                    :dataItem="lstDistrict"
                    v-on:returnValue="chooseDistrict"
                    />
                </div>

                <div class="d-flex m-b-20 w-full">
                    <BaseTextArea
                    :clas="'w-full'"
                    :hasTitle="true"
                    :title="'Mô tả'"
                    :notNull="true"
                    :msrequire="true"
                    :placeholder="'Nhập thông tin mô tả điểm du lịch'"
                    :maxLength="2000"
                    :disabled="disabled"
                    :content="oDestination.describled"
                    v-on:changeData="(value)=>{this.oDestination.describled = value}"
                    />
                </div>
                    
                <div class="block first-block d-flex flex-column m-b-20">
                    <div class="font-bold m-b-20">Giá vé (VND)</div>
                    <div class="w-full d-flex">
                        <BaseInput
                        :clas="'w-30 m-r-20'"
                        :hasTitle="true"
                        :title="'Người lớn'"
                        :msrequire="true"
                        :notNull="true"
                        :isNumber="true"
                        :maxLength="20"
                        :disabled="disabled"
                        :content="oDestination.adultPrice"
                        v-on:changeData="(value)=>{this.oDestination.adultPrice = value}"
                        />

                        <BaseInput
                        :clas="'w-30 m-r-20'"
                        :hasTitle="true"
                        :title="'Trẻ em'"
                        :msrequire="true"
                        :notNull="true"
                        :isNumber="true"
                        :maxLength="20"
                        :disabled="disabled"
                        :content="oDestination.childPrice"
                        v-on:changeData="(value)=>{this.oDestination.childPrice = value}"
                        />

                        <BaseInput
                        :clas="'w-30 m-r-20'"
                        :hasTitle="true"
                        :title="'Em bé'"
                        :msrequire="true"
                        :notNull="true"
                        :isNumber="true"
                        :maxLength="20"
                        :disabled="disabled"
                        :content="oDestination.babyPrice"
                        v-on:changeData="(value)=>{this.oDestination.babyPrice = value}"
                        />
                    </div>
                </div>
            </div>
            
            <div class="d-flex m-b-20">
                <div class="d-flex flex-column w-half m-r-20" style="padding-left:40px">
                    <div class="font-bold m-b-20" >Danh sách ảnh <span style="color:red">*</span></div>
                    <table style="width:200px" id="table-image">
                        <tbody>
                            <tr v-for="(v, index) in lstImage" v-bind:key="index">
                                <td>
                                    <img
                                    :style="{
                                        width: '100px',
                                        height: '100px',
                                    }"
                                    :src="v"
                                    >
                                </td>
                                <td v-if="!isView" class="function" @click="removeImage(index)">Xóa</td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="add-new d-flex" @click="addNewImage">
                        <div>+</div>
                        <div>Thêm ảnh</div>
                    </div>
                    <input v-if="isView" type="file" id="chooseImage" disabled @change="insertImage" style="display: none" accept="image/x-png,image/gif,image/jpeg">
                    <input v-else type="file" id="chooseImage" @change="insertImage" style="display: none" accept="image/x-png,image/gif,image/jpeg">
                </div>

            </div>
          </div>
        <div class="flex-1"></div>
          <div class="action d-flex">
              <div class="flex-1"></div>
              <div class="btn" @click="closeForm">Hủy</div>
              <div v-if="!isView" class="btn btn-save" @click="saveData">Lưu</div>
          </div>
      </div>

      <BasePopUp
        :isShow="showPopUp"
        :type="type"
        :message="message"
        :title="titleP"
        :action1="action1"
        :action2="action2"
        :action3="action3"
        :show="optionPopUp"
        v-on:confirmAction3="()=>{this.showPopUp = false;}"
      />

      <div id="toast"></div>
  </div>
</template>

<script>
import BaseAutoComplete from '../base/BaseAutoComplete.vue'
// import DatePicker from 'vue2-datepicker';
// import 'vue2-datepicker/index.css';
import BasePopUp from '../base/BasePopUp.vue';
import BaseInput from '../base/BaseInput.vue';
import BaseTextArea from '../base/BaseTextArea.vue'
import ProvinceAPI from '../../js/api/province'
import DistrictAPI from '../../js/api/districtapi'
import DestinationAPI from '../../js/api/destinationapi'
import Destination from '../../js/entity/destination'
export default {
  components: { BaseAutoComplete, BaseInput, BaseTextArea, BasePopUp },
  props:{
    destination : Object,
    listImage : Array,
    modeTemplate: Number,
    title: String,
    disabled : Boolean,
    isView: Boolean,
  },
  data(){
      return{
            startTime: null,
            endTime: null,
            oDestination : this.destination,
            lstProvince : [],
            lstDistrict : [],
            dataProvinceField : {value: "ProvinceName"},
            dataDistrictField : {value: "DistrictName"},
            lstImage : this.listImage,

            showPopUp : false,
            type: "error",
            message: null,
            titleP: null,
            action1: "Hủy",
            action2 : "Đóng",
            action3 : "Lưu",
            optionPopUp : [false, false],
            
      }
  },
  async created(){
    await ProvinceAPI.getAll()
    .then(res=>{
        this.lstProvince = res.data;
    })

    if(this.oDestination.provinceID){
        await DistrictAPI.getAll(this.oDestination.provinceID)
        .then(res=>{
            this.lstDistrict = res.data;
        })
    }
  },
  watch:{
    destination : function(){
        this.oDestination = this.destination
    },
    listImage : function(){
        this.lstImage = this.listImage
    }
  },
  methods:{
      closeForm(){
          this.oDestination = new Destination();
          this.lstImage = [];
          this.$emit("closeForm");
      },
      async chooseProvince(pName){
        var me = this;
        var province = this.lstProvince.filter(x=>x.ProvinceName == pName);
        if(province.length == 1){
            me.lstDistrict = [];
            me.oDestination.pronvinceName = province[0].ProvinceName;
            me.oDestination.provinceID = province[0].ProvinceID;
            me.oDestination.districtName = "";
            me.oDestination.districtID = null;
            await DistrictAPI.getAll(province[0].ProvinceID)
            .then(res=>{
                var district = res.data;
                me.lstDistrict = district
            })
        }
      },
      chooseDistrict(dName){
        var district = this.lstDistrict.filter(x=>x.DistrictName == dName);
        if(district.length == 1){
            this.oDestination.districtName = district[0].DistrictName;
            this.oDestination.districtID = district[0].DistrictID;
        }
      },

      addNewImage(){
        var inputImage = document.getElementById("chooseImage")
        inputImage.click();
      },

      insertImage(){
        var me = this;
        var image = document.getElementById("chooseImage");
        var file = image.files[0];
        var reader = new FileReader();
        reader.onload = function(e){
            var lstImg = me.lstImage;
            me.lstImage = [];
            lstImg.push(e.target.result);
            me.lstImage = lstImg;
        }
        if(file){
            reader.readAsDataURL(file);
        }
      },

      removeImage(index){
        var lstImg = this.lstImage;
        this.lstImage = [];
        lstImg.splice(index, 1); 
        this.lstImage = lstImg
      },

      saveData(){
        if(this.validateBeforeSave()){
            var data = {
                "data" : this.oDestination,
                "image" : this.lstImage,
                "action" : this.modeTemplate
            }

            data = JSON.stringify(data);
            this.saveDataOnServer(data);
        }
        else{
            this.showPopUp = true;
            this.titleP = "Cảnh báo";
        }
      },

      async saveDataOnServer(data){
        await DestinationAPI.update(data)
        .then(res=>{
            if(res.data.error == "DupliacteName"){
                this.toast({
                    title: "Tên điểm du lịch đã tồn tại",
                    type: "error",
                    duration: 3000,
                });
            }
            else{
                this.closeForm();
            }
            
        })
        .catch(()=>{
            this.toast({
                title: "Có lỗi xảy ra. Vui lòng thử lại",
                type: "error",
                duration: 3000,
            });
        })
      },

      validateBeforeSave(){
        var input = document.querySelectorAll("#contentForm input,textarea");
        var check = true;
        input.forEach(e => {
            if(e.getAttribute("notNull")){
                if(!e.value){
                    check = false;
                    this.message = "Tồn tại trường bắt buộc nhập đang bỏ trống";
                }
            }
            if(e.classList.contains("error")){
                check = false;
                this.message = "Tồn tại trường nhập liệu có giá trị không hợp lệ";
            }
        })
        var image = document.querySelectorAll("#table-image img");
        if(image.length == 0){
            check = false;
            this.message = "Chưa chọn ảnh";
        }

        var autocomplete = document.querySelectorAll("#contentForm .main-autocomplete");
        autocomplete.forEach(e=>{
            if(e.classList.contains("error")){
                check = false;
                this.message = "Tồn tại trường nhập liệu có giá trị không hợp lệ";
            }
            if(e.getAttribute("notNull")){
                if(!e.querySelector("input").value){
                    check = false;
                    this.message = "Tồn tại trường bắt buộc nhập đang bỏ trống";
                }
            }
        })
        return check;
      },

      /**
     * Khởi tạo toast
     */
    toast({ title, type, duration }) {
        const main = document.getElementById("toast");
        if (main) {
            const toast = document.createElement("div");
            //auto remove toast
            const autoRemove = setTimeout(function () {
            main.removeChild(toast);
            }, duration + 1000);

            toast.onclick = function (e) {
            if (e.target.closest(".delete-toast")) {
                main.removeChild(toast);
                clearTimeout(autoRemove);
            }
            };
            const delay = (duration / 1000).toFixed(2);
            // const icons = {
            //     success: `'fas', 'check-circle'`,
            //     info: 'fas fa-info-circle',
            //     warning: 'fas fa-exclamation-circle',
            //     error: 'fas fa-exclamation-triangle',

            // }
            toast.classList.add("toast-message");
            toast.style.animation = `slideInLeft ease .5s, fadeOut linear 1s ${delay}s forwards`;
            toast.innerHTML = `
                <div class="icon-toast icon-toast-${type}" id="icon-toast">
                    
                </div>
                <div class="content-toast" id="content-toast">${title}</div>
                <div class="delete-toast delete-toast-${type}" id="delete-toast">
                    
                </div>`;
            main.appendChild(toast);
        }
    },
  }
}
</script>

<style>
@import url(../../css/form/createform.css);
.form-container input{
    border-radius: 5px;
}

#avatarHotel{
    height: 100px;
    width: 100px;
    background-color: #babec5;
    background-repeat: no-repeat;
    background-size: cover;
}

.image-destination{
    background-repeat: no-repeat;
}
</style>