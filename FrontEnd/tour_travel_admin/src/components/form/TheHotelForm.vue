<template>
  <div class="form-container d-flex">
      <div class="form-background"></div>
      <div class="form-main d-flex flex-column">
          <div class="header">Thêm mới</div>
          <div class="icon-close" @click="closeForm">X</div>
          <div class="d-flex flex-column content">
            <div class="common-infor d-flex flex-column m-b-20">
                <div class="d-flex">
                    <BaseInput
                    :clas="'w-half m-b-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Tên khách sạn'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="false"
                    @contentInput="newHotelDatas.Name = $event"
                    />

                    <BaseInput
                    :clas="'w-30 m-b-20'"
                    :hasTitle="true"
                    :title="'Mã khách sạn'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="false"
                    @contentInput="newHotelDatas.HotelCode = $event"
                    />
                </div>
                
                <div class="d-flex">
                    <BaseInput
                    :clas="'w-half m-b-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Mã đối tác'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="false"
                    @contentInput="newHotelDatas.ParnerID = $event"
                    />

                    <BaseInput
                    :clas="'w-30 m-b-20'"
                    :hasTitle="true"
                    :title="'Diện tích'"
                    :msrequire="false"
                    :notNull="false"
                    :isNumber="false"
                    @contentInput="newHotelDatas.Acreage = $event"
                    />
                </div>
                    
                <div class="block first-block d-flex">
                    <BaseInput
                    :clas="'w-half m-b-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Địa chỉ'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="false"
                    @contentInput="newHotelDatas.Address = $event"
                    />
                    <BaseInput
                    :clas="'w-20 m-b-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Số điện thoại'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="false"
                    @contentInput="newHotelDatas.PhoneNumber = $event"
                    />
                    <BaseInput
                    :clas="'w-20 m-b-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Xếp hạng (Số sao)'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="true"
                    @contentInput="newHotelDatas.Rank = $event"
                    />
                </div>
                <div class="block second-block d-flex ">
                    <BaseInput
                    :clas="'w-half m-b-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Email'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="false"
                    @contentInput="newHotelDatas.Email = $event"
                    />

                    <BaseInput
                    :clas="'w-20 m-b-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Slogan'"
                    :msrequire="false"
                    :notNull="false"
                    :isNumber="false"
                    @contentInput="newHotelDatas.Solgan = $event"
                    />

                    <BaseAutoComplete
                    :clas="'w-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Tour liên quan'"
                    :notNull="true"
                    :msrequire="true"
                    :placeholder="'Nhập mã tour'"
                    />

                </div>

                <div class="d-flex m-b-20">
                    <BaseTextArea
                    :clas="'w-half m-r-20'"
                    :hasTitle="true"
                    :title="'Mô tả'"
                    :notNull="true"
                    :msrequire="true"
                    :placeholder="'Nhập thông tin mô tả khách sạn'"
                    @contentInput="newHotelDatas.Described= $event"
                    />

                    <div class="d-flex flex-column w-20  m-r-20">
                        <BaseInput
                        :clas="'w-full m-b-10'"
                        :hasTitle="true"
                        :title="'Mô tả ngắn 1'"
                        :msrequire="false"
                        :notNull="false"
                        :isNumber="false"
                        @contentInput="newHotelDatas.SortDes1 = $event"
                        />

                        <BaseInput
                        :clas="'w-full m-b-10'"
                        :hasTitle="true"
                        :title="'Mô tả ngắn 2'"
                        :msrequire="false"
                        :notNull="false"
                        :isNumber="false"
                        @contentInput="newHotelDatas.SortDes2 = $event"
                        />

                        <BaseInput
                        :clas="'w-full m-b-10'"
                        :hasTitle="true"
                        :title="'Mô tả ngắn 3'"
                        :msrequire="false"
                        :notNull="false"
                        :isNumber="false"
                        @contentInput="newHotelDatas.SortDes3 = $event"
                        />
                    </div>

                    <BaseTextArea
                    :clas="'w-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Mô tả'"
                    :notNull="true"
                    :msrequire="true"
                    :placeholder="'Nhập mô tả phòng'"
                    @contentInput="newHotelDatas.DescribedRoom = $event"
                    />
                </div>
            </div>
            
            <div class="d-flex m-b-20">
                <div class="d-flex flex-column w-half m-r-20" style="padding-left:40px">
                    <div class="font-bold m-b-20" >Danh sách ảnh <span style="color:red">*</span></div>
                    <table>
                        <tbody>
                            <tr>
                                <td>
                                    <input type="file" accept="image/x-png,image/gif,image/jpeg">
                                </td>
                                <td class="function">Xóa</td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="add-new d-flex">
                        <div>+</div>
                        <div>Thêm ảnh</div>
                    </div>
                </div>

                <div class="d-flex flex-column w-half">
                    <div class="font-bold m-b-20" >Ảnh đại diện<span style="color:red">*</span></div>
                    <label for="avatar" id="avatarHotel"></label>
                    <input type="file" id="avatar" accept="image/x-png,image/gif,image/jpeg" class="d-none" @change="chooseAvatar"> 
                </div>

            </div>
          </div>

          <div class="action d-flex">
              <div class="flex-1"></div>
              <div class="btn" @click="closeForm">Hủy</div>
              <div class="btn btn-save" @click="handleSaveNewHotel()">Lưu</div>
          </div>
      </div>
  </div>
</template>

<script>
import BaseAutoComplete from '../base/BaseAutoComplete.vue'
// import DatePicker from 'vue2-datepicker';
// import 'vue2-datepicker/index.css';
import BaseInput from '../base/BaseInput.vue';
import BaseTextArea from '../base/BaseTextArea.vue'
import HotelAPI from '../../js/api/hotel'
export default {
  components: { BaseAutoComplete, BaseInput, BaseTextArea },
  data(){
      return{
          startTime: null,
          endTime: null,
          newHotelDatas: {}
      }
  },
  methods:{
      closeForm(){
          this.$emit("closeForm");
      },
      chooseAvatar(){
        var image = document.querySelector("#avatar");

        var file = image.files[0];
        var reader = new FileReader();
        reader.onloadend = function(){
            document.getElementById('avatarHotel').style.backgroundImage = "url(" + reader.result + ")";
        }
        if(file){
            reader.readAsDataURL(file);
        }
      },
      async handleSaveNewHotel() {
        let allSortDescribed = '{SortDescribed1: ' + this.newHotelDatas.SortDes1 +
            ', SortDescribed2: ' + this.newHotelDatas.SortDes2 +
            ', SortDescribed3: ' + this.newHotelDatas.SortDes3 + '}'
        this.newHotelDatas.SortDescribed = allSortDescribed
        let addNewHotelResponse = await HotelAPI.addNewHotel(this.newHotelDatas)
        this.$emit("response-action", addNewHotelResponse.data);
      },
  },
  mounted() {
    this.newHotelDatas = {
      Name: null,
      HotelCode: null,
      ParnerID: null,
      Acreage: null,
      Address: null,
      PhoneNumber: null,
      Rank: null,
      Email: null,
      Solgan: null,
      Described: null,
      SortDes1: null,
      SortDes2: null,
      SortDes3: null,
      DescribedRoom: null
    }
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
</style>