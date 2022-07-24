<template>
<div class="container" style="position:relative" >
    <div class="dropdown-container" :class="clas">
        <input type="text" name="date" :class="read?'read-only':''" class="dropdown-content" readonly :value="value" :id="id" v-on:keyup.38="selectItem" v-on:keyup.40="selectItemDown" v-on:keyup.13="enterChoose" :tabindex="tabindex">
        <div class="button" @click="showOption" v-click-outside="hiddenOption">
            <div class="mi mi-16 dropdown-button" :class="[isShow? 'choose' : '']"></div>
        </div>
        
    </div>
    <div :class="[clas, isShow? 'option-container' : 'hidden-option', isNormal?'option-container-normal':'']">
        <div v-for="(o, index) in listOption" v-bind:key="index" :title="o">
            <input type="radio" :value="o" :id="'option-dropdown'+index" name="amount" class="option-radio" style="display: none" :checked="(o == value) ? 'checked' : ''" >
            <label :for="'option-dropdown'+index"  class="option-dropdown" @click="chooseOption(o, index)">{{o}}</label>
        </div>
    </div>
    <div :tabindex="tabindex+1" @focus="hiddenShowOption"></div>
</div>

</template>

<script>
export default {
    name: "DropDown",
    props:{
        value : String,
        listOption: Array,
        id: String,
        tabindex: Number,
        isNormal: Boolean,
        clas: String,
        read: Boolean,
    },
    data(){
        return{
            isShow: false,
            indexOption : 0,
        }
    },
    computed:{
        
    },
    methods:{
        /**
         * Hiển thị nội dung option
         */
        showOption(){
            if(!this.read){
                this.isShow = !this.isShow;
                if(this.isShow){
                    document.getElementById(this.id).focus();
                }
            }
            
        },
        /**
         * Click ra ngoài thì đóng option
         */
        hiddenOption(event){
            var div = document.getElementById(this.id);
            (event.target ==  div)? this.isShow = true : this.isShow = false;
        },
        /**
         * Chọn option
         * @param {String} value : Nội dung số lượng được chọn 
         * @param {Number} index : Vị trí số lượng được chọn
         */
        chooseOption(value, index){
            if(!this.read){
                this.$emit("chooseOption", value);
                this.indexOption = index;
                this.$emit("confirmOption", index);
            }
            
        },
        /**
         * Chọn option bằng cách nhấn phím đi lên
         */
        selectItem(){
            if(!this.read){
                var option = document.querySelectorAll(".option-radio");
                var index;
                for(var i=0; i<option.length; i++){
                    if(option[i].checked){
                        var idO = option[i].id;
                        idO = idO.substring(6);
                        index = idO;
                        break;
                    }
                }
                if(index != 0){
                    var value = option[index-1].value;
                    this.$emit("chooseOption", value);
                    this.indexOption = index-1;
                }
            }
            
        },
        /**
         * Chọn option bằng cách nhấn phím đi xuống
         */
        selectItemDown(){
            if(!this.read){
                var option = document.querySelectorAll(".option-radio");
                var index;
                for(var i=0; i<option.length; i++){
                    if(option[i].checked){
                        var idO = option[i].id;
                        idO = idO.substring(6);
                        index = idO;
                        break;
                    }
                }
                index = Number(index);
                if(index != option.length-1){
                    var value = option[index+1].value;
                    this.$emit("chooseOption", value);
                    this.indexOption = index+1;
                }
            }
            
        },
        /**
         * Nhấn enter để lọc
         */
        enterChoose(){
            if(!this.read){
                this.isShow = false;
                document.getElementById(this.id).blur();
                this.$emit("confirmOption", this.indexOption);
            }
            
            
        },
        /**
         * Đóng option khi nhấn tab
         */
        hiddenShowOption(){
            this.isShow = false;
        }
    },
}
</script>

<style>
    .dropdown-container{
        width: 200px;
        height: 32px;
        
        display: flex;
    }
    .dropdown-container .dropdown-content{
        border: 1px solid #babec5;
        outline: none;
        padding-left: 10px;
        flex: 1;
        cursor: pointer;
    }
    .dropdown-container .dropdown-content:focus{
        border-color: #e89327 !important;
    }
    .dropdown-container .button{
        width: 30px;
        height: 31px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        position: absolute;
        right: 0;
        border: none;
    }
    .dropdown-container .button.read{
        background-color: #f3f3f3 !important;
    }
    .dropdown-container .button:hover{
        background-color: #e0e0e0;
    }
    .dropdown-container .button .dropdown-button{
        background-position: -560px -359px;
    }

    .option-container{
        width: 200px;
        height: auto;
        position: absolute;
        bottom: 34px;
        background-color: #ffffff;
        display: flex;
        flex-direction: column;
        border: 1px solid #babec5;
    }
    .option-container-normal{
        bottom: unset !important;
        top: 34px;
    }
    .option-container .option-dropdown{
        height: 32px;
        width: 100%;
        padding-left: 10px;
        display: flex;
        align-items: center;
        background-color: #ffffff;
        cursor: pointer;
    }
    .option-container .option-dropdown:hover{
        background-color: #ebedf0;
        color: #6cba63;
    }
    .option-radio:checked + label{
        background-color: #e89327 !important;
        color: #ffffff !important;
    }
    .hidden-option{
        display: none;
    }
    .choose{
        transform: rotate(180deg);
    }
    .container.read{
        background-color: #f3f3f3 !important;
    }
    label{
        font-size: 13px !important;
        margin-left: 0px !important;
    }
</style>