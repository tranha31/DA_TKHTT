<template>
  <div class="form-container d-flex">
    <div class="form-background"></div>
    <div class="form-main d-flex flex-column form-cancel">
        <div class="header">{{title}}</div>
        <div class="icon-close" @click="closeForm">X</div>
        <div class="d-flex flex-column w-full content">
            <div class="reason d-flex flex-column m-b-20">
                <div style="font-weight:600; margin-bottom:4px">Lý do hủy <span style="color: red">*</span></div>
                <textarea :title="message" v-title :class="isNull ? 'error' : ''" 
                    @blur="()=>{
                        if(this.reason){
                            this.isNull = false
                            this.message = ''
                        }
                        else{
                            this.isNull = true
                            this.message = 'Dữ liệu không được để trống';
                        }
                    }">
                </textarea>
            </div>
            <div class="w-full">
                <table style="width: 100%;">
                    <thead>
                        <tr>
                            <th>
                                Tên người nhận
                            </th>
                            <th>
                                Email
                            </th>
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
                        </tr>
                        
                    </tbody>
                </table>
            </div>
            
            
        </div>
        <div class="flex-1"></div>
        <div class="action d-flex">
              <div class="flex-1"></div>
              <div class="btn btn-save">Gửi</div>
          </div>
    </div>
  </div>
</template>

<script>
import BaseInput from '../base/BaseInput.vue';
export default {
  components: { BaseInput },
    props:{
        title: String,
    },
    data(){
        return{
            reason: "",
            isNull: false,
            message : "",
        }
    },
    methods:{
        closeForm(){
            this.$emit("closeForm");
        }
    }
}
</script>

<style>
@import url(../../css/form/createform.css);
@import url(../../css/form/canceltour.css);
.form-container input{
    border-radius: 5px;
}
</style>