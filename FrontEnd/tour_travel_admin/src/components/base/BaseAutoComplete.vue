<template>
    <div :class="clas">
        <div v-if="hasTitle" class="title-input">{{title}}&nbsp;&nbsp;<span v-if="msrequire">*</span></div>
        <div class="main-autocomplete" :class="error? 'error' : ''" :title="message" v-title>
            <div v-if="hasImage" class="img" :class="classImage"></div>
            <input v-if="disable" disabled class="w-full" style="height:33px; border:unset; border-radius: 0;padding-left: 10px;" v-model="contents"/>
            <ejs-autocomplete v-else :dataSource='dataItem' :fields='dataFields' 
            v-model="contents"
            :placeholder="placeholder"
            @blur="blurCbb">
            </ejs-autocomplete>
        </div>
        
    </div>
</template>

<script>
import Vue from "vue";
import {AutoCompletePlugin} from "@syncfusion/ej2-vue-dropdowns";
import Error from '../../js/entity/error.js'
Vue.use(AutoCompletePlugin)
export default {
    props:{
        dataItem : Array,
        dataFields: Object,
        clas: String,
        placeholder: String,
        msrequire: Boolean,
        content: String,
        hasTitle: Boolean,
        title: String,
        isNumber: Boolean,
        notNull : Boolean,
        read : Boolean,
        hasImage: Boolean,
        classImage: String,
        disable: Boolean,
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
    },
    methods:{
        /**
         * Blur cbb check validate
         */
        blurCbb(){
            var e = new Error();
            if(this.notNull){
                if(!this.contents){
                    this.error = true;
                    this.message = e.NotNull;
                }
                else{
                    this.error = false;
                    this.message = "";
                    
                }
            }
            this.$emit("returnValue", this.contents);
        },
    }
}
</script>

<style>
@import url(https://cdn.syncfusion.com/ej2/material.css);

.main-autocomplete{
    position: relative;
}

.main-autocomplete .img{
    position: absolute;
    left: 5px;
    top: 25%;
}

.e-autocomplete::placeholder{
    color: #949494;
    font-family: notosans-italic;
}

.e-autocomplete{
    padding-left: 10px !important;
    height: 23px !important;
}
</style>