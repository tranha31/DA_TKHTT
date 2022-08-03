<template>
  <div class="place-container d-flex flex-column" style="height:93vh">
    <div class="place-list" style="height:100%; padding:20px 100px">
        <div class="content-place d-flex" style="flex-wrap:wrap">
            <div v-for="(v, index) in listDestination" v-bind:key="index" class="v-place place d-flex flex-column">
                <img :src="v.imageUrl"/>
                <div class="d-flex flex-column" style="padding:20px">
                    <router-link class="font-bold mb-20 title-place" :to="{ name: 'place-infor', params: { id: v.id }}" >{{v.name}}</router-link>
                    <div>{{v.place}}</div>
                </div>
            </div>
        </div>
        <BaseNavigationPage
        :totalPage="totalPage"
        :totalrecord="totalRecord"
        :currentPage="currentPage"
        :listNumberPage="numberPage"
        />
    </div>
    
    
    <div id="toast"></div>
    <BaseLoad :load="showLoad"/>
    <TheFooter/>
  </div>
</template>

<script>
import BaseNavigationPage from '../../components/base/BaseNavigationPage.vue'
import TheFooter from '../../components/layout/TheFooter.vue'
import BaseLoad from '../../components/base/BaseLoad.vue'
import DestinationAPI from '../../js/api/destinationapi'
export default {
    components: { BaseNavigationPage, TheFooter, BaseLoad},
    data(){
        return{
            showLoad : false,
            totalRecord : 5,
            totalPage: 1,
            currentPage: 1,
            pageSize : 20,
            numberPage: [
                {value: 1, class: "active"},
                {value: 2, class: ""},
                {value: 3, class: ""},
                {value: 5, class: ""},
            ],

            listDestination : [],
        }
    },
    async created() {
        await this.loadData(20, 0)
    },
    methods:{
        async loadData(size, page){
            this.showLoad = true
            await DestinationAPI.getAll("", size, page)
            .then(res=>{
                this.listDestination = []
                var data = res.data.data
                var listImage = res.data.image
                this.totalRecord = res.data.totalRecord
                this.totalPage = res.data.totalPage
                for(var i=0; i<data.length; i++){
                    var item = data[i]
                    var image = listImage[i]
                    var randIndex = Math.floor(Math.random() * image.Image.length)
                    image = image.Image[randIndex]
                    this.listDestination.push({
                        id: item.RefID,
                        imageUrl: image,
                        name: item.Name,
                        place: item.Place,
                    })
                }

                this.numberPage = [];
                var me = this;
                if(me.totalPage > 4){
                    me.numberPage = [
                        {value: 1, class: "active"},
                        {value: 2, class: ""},
                        {value: 3, class: ""},
                        {value: this.totalPage, class: ""},
                    ];
                }
                else{
                    for(i=1; i<= me.totalPage; i++){
                    if(i == 1){
                        me.numberPage.push({
                            value: 1,
                            class: "active"
                        });
                    }
                    else{
                        me.numberPage.push({value:i, class: ""});
                    }
                    
                    }
                }
            })
            .catch(()=>{
                this.toast({
                    title: "Có lỗi xảy ra. Vui lòng thử lại",
                    type: "error",
                    duration: 3000,
                });
            })

            this.showLoad = false
        },
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

<style scoped>
.place-list{
    overflow: auto;
}

.content-place .v-place{
    height: 600px;
    width: 500px;
    border: 1px solid #babec5;
    border-radius: 5px;
    margin: 25px;
}
.content-place .v-place img{
    height: 400px;
    width: 100%;
}

.content-place .v-place .title-place{
    font-size: 20px;
    color: #000;
    margin-left: 0px !important;
}
</style>