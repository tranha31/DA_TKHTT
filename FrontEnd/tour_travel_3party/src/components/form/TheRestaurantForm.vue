<template>
  <div class="form-container d-flex">
      <div class="form-background"></div>
      <div class="form-main d-flex flex-column">
          <div class="header">Thêm mới</div>
          <div class="icon-close" @click="closeForm">X</div>
          <div class="d-flex flex-column content">
            <div class="common-infor d-flex flex-column m-b-20" style="border:unset">
                <div class="d-flex">
                    <BaseInput
                    :clas="'w-half m-b-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Tên nhà hàng'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="false"
                    />

                    <BaseInput
                    :clas="'w-20 m-b-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Loại đồ ăn'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="false"
                    />

                    <div class="d-flex flex-column w-20 m-b-20 m-r-20">
                        <div class="title-input">Giờ mở cửa&nbsp;&nbsp;<span style="color:red">*</span></div>
                        <date-picker v-model="time1" type="time"  placeholder="Select date tine" format='mm:hh'></date-picker>
                    </div>
                    
                </div>

                <BaseInput
                :clas="'w-20 m-b-20 m-r-20'"
                :hasTitle="true"
                :title="'Số điện thoại'"
                :msrequire="true"
                :notNull="true"
                :isNumber="false"
                />
                
                <div class="d-flex">
                    <BaseTextArea
                    :clas="'w-full m-r-20 m-b-20'"
                    :hasTitle="true"
                    :title="'Mô tả'"
                    :notNull="true"
                    :msrequire="true"
                    :placeholder="'Nhập thông tin mô tả phòng'"
                    />
                </div>

                <div class="d-flex w-full m-b-20">
                    <div class="d-flex flex-column w-half m-r-20">
                        <div class="font-bold m-b-20">Menu <span style="color:red">*</span></div>

                        <table class="m-b-20">
                            <thead>
                                <tr>
                                    <th>Tên</th>
                                    <th>Giá</th>
                                    <th></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>
                                        <BaseInput
                                        :clas="'w-full'"
                                        :hasTitle="false"
                                        :msrequire="false"
                                        :notNull="false"
                                        :isNumber="false"
                                        />
                                    </td>
                                    <td>
                                        <BaseInput
                                        :clas="'w-full'"
                                        :hasTitle="false"
                                        :msrequire="false"
                                        :notNull="false"
                                        :isNumber="false"
                                        />
                                    </td>
                                    <td class="function">Xóa</td>
                                </tr>
                            </tbody>
                        </table>
                        <div class="btn" style="width:107px">Thêm mới</div>
                    </div>

                    <div class="d-flex flex-column w-half m-r-20">
                        <div class="font-bold m-b-20">Ảnh <span style="color:red">*</span></div>

                        <table class="m-b-20">
                            <tbody>
                                <tr>
                                    <td>
                                        <input type="file" accept="image/x-png,image/gif,image/jpeg">
                                    </td>
                                    
                                    <td class="function">Xóa</td>
                                </tr>
                            </tbody>
                        </table>
                        <div class="btn" style="width:107px">Thêm mới</div>
                    </div>
                </div>
                
                
            </div>
          </div>
          <div class="flex-1"></div>
          <div class="action d-flex">
              <div class="flex-1"></div>
              <div class="btn" @click="closeForm">Hủy</div>
              <div class="btn btn-save">Lưu</div>
          </div>
      </div>
  </div>
</template>

<script>
// import DatePicker from 'vue2-datepicker';
// import 'vue2-datepicker/index.css';
import BaseInput from '../base/BaseInput.vue';
import BaseTextArea from '../base/BaseTextArea.vue'
import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';
export default {
  components: { BaseInput, BaseTextArea, DatePicker },
  data(){
      return{
          startTime: null,
          endTime: null,
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