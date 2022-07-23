<template>
    <div class="page-navigation">
        <div v-if="totalrecord > 0" class="page-navigation-bar">
            <div class="total-record">
                Tổng số: <b>{{ totalrecord }}</b> bản ghi
            </div>

            <BaseDropDown
            :value="value"
            :listOption="listOption"
            id="amount"
            :tabindex="tabindex"
            v-on:chooseOption="chooseOption"
            v-on:confirmOption="confirmOption"
            />
            
            <div v-if="totalPage < 5" class="number-page">
                <div v-if="currentPage > 1" class="first" style="cursor:pointer" @click="choosePrePage">Trước</div>
                <div v-else class="first" style="color:#e4e4e4">Trước</div>
                <div v-for="(p, index) in listNumberPage" v-bind:key="index" class="page-number number" :class="p.class" @click="choosePage(p.value)">{{p.value}}</div>
                <div v-if="currentPage < totalPage" class="last" style="cursor:pointer" @click="chooseNextPage">Sau</div>
                <div v-else class="last" style="color: #e4e4e4">Sau</div>
            </div>
            <div v-else class="number-page">
                <div v-if="currentPage > 1" class="first" style="cursor:pointer" @click="choosePrePage">Trước</div>
                <div v-else class="first" style="color:#e4e4e4">Trước</div>
                <div class="page-number number" :class="listNumberPage[0].class" @click="chooseFirstPage">1</div>
                <div v-if="currentPage > 2" class="page-number">...</div>
                <div class="page-number number" :class="listNumberPage[1].class" @click="choosePage(listNumberPage[1].value)">{{ listNumberPage[1].value }}</div>
                <div class="page-number number" :class="listNumberPage[2].class" @click="choosePage(listNumberPage[2].value)">{{ listNumberPage[2].value }}</div>
                <div v-if="currentPage < totalPage-1" class="page-number">...</div>
                <div class="page-number number" :class="listNumberPage[3].class" @click="chooseLastPage">{{ listNumberPage[3].value }}</div>
                <div v-if="currentPage < totalPage" class="last" style="cursor:pointer" @click="chooseNextPage">Sau</div>
                <div v-else class="last" style="color: #e4e4e4">Sau</div>
            </div>
        </div>
        <div v-else class="empty-value">
            <div class="notification">
                <img src="https://actappg1.misacdn.net/img/bg_report_nodata.76e50bd8.svg">
                <div style="margin-top: 30px">Không có dữ liệu</div>
            </div>
        </div>
    </div>
</template>

<script>
import BaseDropDown from './BaseDropDown.vue';
export default {
    name: "PageNavigation",
    components: {BaseDropDown  },
    props:{
        totalrecord: Number,
        currentPage: Number,
        totalPage: Number,
        listNumberPage: Array,
    },
    data(){
        return{
            value: "20 bản ghi trên một trang",
            listOption: ["10 bản ghi trên một trang", 
                        "20 bản ghi trên một trang",
                        "30 bản ghi trên một trang",
                        "50 bản ghi trên một trang",
                        "100 bản ghi trên một trang"],
            listValueOption: [10, 20, 30, 50, 100],
            tabindex : 20,
        }
    },
    methods:{
        /**
         * Chọn option
         * @param {String} value: Giá trị số lượng bản ghi được chọn
         * create by: TQHA (19/8/2021)
         */
        chooseOption(value){
            this.value = value;
        },
        /**
         * Chọn đối tượng
         * @param {Number} index: vị trí của giá trị được chọn
         * create by: TQHA (19/8/2021)
         */
        confirmOption(index){
            this.$emit("changePageSize", this.listValueOption[index])
            
        },

        /**
         * Chọn trang đầu tiên
         * create by: TQHA(19/8/2021)
         */
        chooseFirstPage(){
            if(this.totalPage > 4){
                var num = [
                    {value: 1, class: "active"},
                    {value: 2, class: ""},
                    {value: 3, class: ""},
                    {value: this.totalPage, class: ""},
                ];

                this.$emit("choosePage", 1, num);
            }
            else{
                num = [];
                for(var i=1; i<=this.totalPage; i++){
                    num.push(
                        {value: i, class: (i==1)? "active": ""}
                    );
                }

                this.$emit("choosePage", 1, num);
            }
        },
        /**
         * Chọn page
         * @param {Number} page : trang
         * create by: TQHA (19/8/2021)
         */
        choosePage(page){
            if(this.totalPage > 4){
                if(page < 3){
                    var num = [
                        {value: 1, class: (page == 1)? "active" : ""},
                        {value: 2, class: (page == 2)? "active" : ""},
                        {value: 3, class: (page == 3)? "active" : ""},
                        {value: this.totalPage, class: ""},
                    ];

                    this.$emit("choosePage", page, num);
                }
                else if(page > this.totalPage-3){
                    num = [
                        {value: 1, class: ""},
                        {value: this.totalPage-2, class: (page == this.totalPage-2)? "active" : "" },
                        {value: this.totalPage-1, class: (page == this.totalPage-1)? "active" : ""},
                        {value: this.totalPage, class: (page == this.totalPage)? "active" : ""},
                    ];
                    this.$emit("choosePage", page, num);
                }
                else{
                    num = [
                        {value: 1, class: ""},
                        {value: page, class: "active"},
                        {value: page+1, class: ""},
                        {value: this.totalPage, class: ""},
                    ];
                    this.$emit("choosePage", page, num);
                }
            }
            else{
                num = [];
                for(var i=1; i<=this.totalPage; i++){
                    num.push(
                        {value: i, class: (i==page)? "active": ""}
                    );
                }
                
                this.$emit("choosePage", page, num);
            }
        },
        /**
         * Chọn trang cuối cùng
         * create by: TQHA (19/8/2021)
         */
        chooseLastPage(){
            if(this.totalPage > 4){
                var num = [
                    {value: 1, class: ""},
                    {value: this.totalPage-2, class: ""},
                    {value: this.totalPage-1, class: ""},
                    {value: this.totalPage, class: "active"},
                ];

                this.$emit("choosePage", this.totalPage, num);
            }
            else{
                num = [];
                for(var i=1; i<=this.totalPage; i++){
                    num.push(
                        {value: i, class: (i==this.totalPage)? "active": ""}
                    );
                }

                this.$emit("choosePage", this.totalPage, num);
            }
        },
        /**
         * Chọn trang tiếp theo
         * create by: TQHA (19/8/2021)
         */
        chooseNextPage(){
            this.choosePage(this.currentPage+1);
        },
        /**
         * Chọn trang trước đó
         * create by: TQHA (19/8/2021)
         */
        choosePrePage(){
            this.choosePage(this.currentPage - 1);
        }
    },
}
</script>

<style scoped>
    @import url(../../css/common/nav.css);
    
</style>