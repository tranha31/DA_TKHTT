<template>
  <div class="main-input" :class="clas" >
        <div v-if="hasTitle" class="title-input">{{title}}&nbsp;&nbsp;<span v-if="msrequire">*</span></div>
        <div v-if="hasImage" class="img" :class="classImage"></div>
        <textarea type="text"
            class="base-input"
            :class="[isNumber? 'input-right':'', error? 'error' : '', read? 'read' : '']"
            :placeholder="placeholder"
            :readonly="read"
            :title="message" v-title
            :disabled="disabled"
            autocomplete="off"
            v-model="contents"
            @keypress="input($event)"
            @input="sendContent"
            @blur="checkValidate"
            @change="sendData"
            ref="Input"
        ></textarea>
    </div>
</template>

<script>
import Error from '../../js/entity/error.js'
import Vue from"vue"
export default {
    props:{
        clas: String,
        placeholder: String,
        msrequire: Boolean,
        content: {type:[String, Number]},
        hasTitle: Boolean,
        title: String,
        isNumber: Boolean,
        notNull : Boolean,
        read : Boolean,
        hasImage: Boolean,
        classImage: String,
        disabled : Boolean,
    },
    data(){
        return{
            contents : this.content,
            error : false,
            message : "",
        }
    },
    watch:{
        content: function(){
            this.contents = this.content;
        },
        contents: function(newValue){
            if(this.isNumber){
                const result = newValue
                .replace(/\D/g, "")
                .replace(/\B(?=(\d{3})+(?!\d))/g, ".");
                Vue.nextTick(() => (this.contents = result));
            }
            
        }
    },
    methods:{
        /**
         * Focus ô input
         */
        focusInput(){
            this.$refs.Input.focus();
        },
        /**
         * Chỉ cho nhập số
         */
        input(evt){
            if(this.isNumber){
                evt = evt ? evt : window.event;
                var charCode = evt.which ? evt.which : evt.keyCode;
                if (
                    charCode > 31 &&
                    (charCode < 48 || charCode > 57) &&
                    charCode !== 46
                ) {
                    evt.preventDefault();
                } 
                else {
                    return true;
                }
            }
        },
        /**
         * Gửi nội dung cho component cha
         */
        sendContent(){
            this.$emit("contentInput", this.contents);
        },
        /**
         * Kiểm tra nội dung nhập có hợp lệ
         */
        checkValidate(){
            var e = new Error();
            if(this.notNull){
                if(this.contents == "" || this.contents == null){
                    this.error = true;
                    this.message = e.NotNull;
                }
                else{
                    this.error = false;
                    this.message = "";
                }
            }
        },
        /**
         * Đặt nội dung lỗi
         */
        setErrorMessage(mess){
            this.error = true;
            this.message = mess;
        },

        unsetErrorMessage(){
            this.error = false;
            this.message = "";
        },

        sendData(){
            if(this.isNumber){
                this.$emit("changeData", this.contents.replaceAll(".", ""));
            }
            else{
                this.$emit("changeData", this.contents);
            }
        }
    }
}
</script>

<style>
    .main-input{
        position: relative;
    }

    .main-input textarea{
        resize: none;
    }

    .main-input .img{
        position: absolute;
        left: 5px;
        top: 25%;
        z-index: 1;
    }

    .title-input{
        font-weight: 600;
        font-size: 12px;
        margin-bottom: 4px;
    }
    .title-input span{
        color: #ff0000;
    }
    .base-input{
        border: 1px solid #babec5;
        width: 100%;
        height: 34px;
        font-size: 13px;
        color: inherit;
        position: relative;
        border-radius: 2px;
        box-sizing: border-box;
        padding: 6px 10px;
    }
    .base-input::placeholder{
        color: #949494;
        font-family: notosans-italic;
    }
    .base-input:focus{
        border-color: #e89327 !important;
    }
    .base-input.error{
        border-color: #f77 !important;
    }
    .base-input.read{
        background-color: #f3f3f3 !important;
    }
    .input-right{
        text-align: right;
    }
</style>