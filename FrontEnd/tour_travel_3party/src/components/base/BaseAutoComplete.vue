<template>
    <div :class="clas">
        <div v-if="hasTitle" class="title-input">{{title}}&nbsp;&nbsp;<span v-if="msrequire">*</span></div>
        <div class="main-autocomplete" :class="error? 'error' : ''" :title="message" v-title>
            <ejs-autocomplete :dataSource='dataItem' :fields='dataFields' 
            v-model="contents"
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
            if(this.msrequire){
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
</style>