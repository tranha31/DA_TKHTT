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
                    :title="'Tên phòng'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="false"
                    />

                    <BaseInput
                    :clas="'w-20 m-b-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Mã phòng'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="false"
                    />
                    <BaseInput
                    :clas="'w-20 m-b-20'"
                    :hasTitle="true"
                    :title="'Mã khách sạn'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="false"
                    :disabled="true"
                    />
                </div>
                
                <div class="d-flex">
                    <BaseTextArea
                    :clas="'w-half m-r-20 m-b-20'"
                    :hasTitle="true"
                    :title="'Mô tả'"
                    :notNull="true"
                    :msrequire="true"
                    :placeholder="'Nhập thông tin mô tả phòng'"
                    />

                    <BaseInput
                    :clas="'w-20 m-b-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Diện tích'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="true"
                    />
                    <BaseInput
                    :clas="'w-20 m-b-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Số lượng'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="true"
                    />
                </div>
                    
                <div class="block first-block d-flex">
                    <BaseInput
                    :clas="'w-20 m-b-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Số người lớn'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="false"
                    />
                    <BaseInput
                    :clas="'w-20 m-b-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Số trẻ em'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="false"
                    />
                    <BaseInput
                    :clas="'w-20 m-b-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Số em bé'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="true"
                    />
                </div>

                <div class="d-flex flex-column w-half m-b-20">
                    <div class="font-bold m-b-20" >Ảnh đại diện<span style="color:red">*</span></div>
                    <label for="avatar" id="avatarHotel"></label>
                    <input type="file" id="avatar" accept="image/x-png,image/gif,image/jpeg" class="d-none" @change="chooseAvatar"> 
                </div>

                <div class="block second-block d-flex flex-column" style="border-top:1px solid #babec5; padding-top:20px">
                    
                    <div class="font-bold m-b-20">Thông tin option1: Không ăn sáng</div>
                    <div class="d-flex w-full">
                        <BaseInput
                        :clas="'w-half m-b-20 m-r-20'"
                        :hasTitle="true"
                        :title="'Tên option'"
                        :msrequire="true"
                        :notNull="true"
                        :isNumber="false"
                        />

                        <BaseInput
                        :clas="'w-20 m-b-20 m-r-20'"
                        :hasTitle="true"
                        :title="'Giá phòng'"
                        :msrequire="true"
                        :notNull="true"
                        :isNumber="true"
                        />
                    </div>
                    
                    <BaseTextArea
                    :clas="'w-half m-r-20'"
                    :hasTitle="true"
                    :title="'Chi tiết gói'"
                    :notNull="true"
                    :msrequire="true"
                    :placeholder="'Chi tiết gói'"
                    />

                    <BaseTextArea
                    :clas="'w-half m-r-20 m-b-20'"
                    :hasTitle="true"
                    :title="'Chính sách hoàn hủy'"
                    :notNull="true"
                    :msrequire="true"
                    :placeholder="'Chính sách hoàn hủy'"
                    />

                   
                </div>

                <div class="block second-block d-flex flex-column" style="border-top:1px solid #babec5; padding-top:20px">
                    
                    <div class="font-bold m-b-20">Thông tin option2: Ăn sáng</div>
                    <div class="d-flex w-full">
                        <BaseInput
                        :clas="'w-half m-b-20 m-r-20'"
                        :hasTitle="true"
                        :title="'Tên option'"
                        :msrequire="true"
                        :notNull="true"
                        :isNumber="false"
                        />

                        <BaseInput
                        :clas="'w-20 m-b-20 m-r-20'"
                        :hasTitle="true"
                        :title="'Giá phòng'"
                        :msrequire="true"
                        :notNull="true"
                        :isNumber="true"
                        />
                    </div>
                    
                    <BaseTextArea
                    :clas="'w-half m-r-20'"
                    :hasTitle="true"
                    :title="'Chi tiết gói'"
                    :notNull="true"
                    :msrequire="true"
                    :placeholder="'Chi tiết gói'"
                    />

                    <BaseTextArea
                    :clas="'w-half m-r-20 m-b-20'"
                    :hasTitle="true"
                    :title="'Chính sách hoàn hủy'"
                    :notNull="true"
                    :msrequire="true"
                    :placeholder="'Chính sách hoàn hủy'"
                    />

                   
                </div>

                
            </div>
            
            
          </div>

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
export default {
  components: { BaseInput, BaseTextArea },
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