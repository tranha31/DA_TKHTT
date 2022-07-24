<template>
  <div class="place-info-container">
    <img v-for="(v, index) in listImage" v-bind:key="index" class="image w-60 slide fade slideTour" :src="v">
    <div id="commonInfo" class="info w-full flex-column d-flex" style="line-height:30px;margin-top:30px">
        <div class="font-bold" style="font-size:20px">{{object.Name}}</div>
        <div class="">Tỉnh: <span style="">{{object.ProvinceName}}</span></div>
        <div class="">Huyện: <span style="">{{object.DistrictName}}</span></div>
        <div class="">Địa chỉ: <span style="">{{object.Place}}</span></div>
        <div class="d-flex flex-column">Giá vé:
            <div style="padding-left:10px">Người lớn: <span style="">{{object.Adult}}</span></div>
            <div style="padding-left:10px">Trẻ em: <span style="">{{object.Child}}</span></div>
            <div style="padding-left:10px">Em bé: <span style="">{{object.Baby}}</span></div>
        </div>
        <div>{{object.Described}}</div>
    </div>

    <BaseLoad :load="showLoad"/>
  </div>
</template>

<script>
import BaseLoad from '../../components/base/BaseLoad.vue'
import DestinationAPI from '../../js/api/destinationapi'
export default {
    components: {BaseLoad},
    props:{},
    data(){
        return{
            id: null,
            slideIndex : 0,
            object: {},
            listImage: [],
            showLoad: false,

        }
    },
    watch:{
        '$route'(to, from){
            this.id = to.params.id;
            from;
        }
    },
    async created() {
        this.id = this.$route.params.id;
        this.showLoad = true
        await DestinationAPI.getByID(this.id)
        .then(res=>{
            this.object = res.data.data[0]
            var ticket = this.object.TicketPrice
            ticket = JSON.parse(ticket)
            this.object.Adult = ticket.Adult.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ".") + " VNĐ"
            this.object.Child = ticket.Child.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ".") + " VNĐ"
            this.object.Baby = ticket.Baby.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ".") + " VNĐ"
            
            this.listImage = res.data.image
        })
        this.showLoad = false

        setTimeout(()=>{    
            this.showSlides();
        }, 100)
    },
    methods:{
        /**
         * Hiển thị ảnh tour theo thời gian
         */
        showSlides(){
            let i;
            let slides = document.getElementsByClassName("slideTour");
            for (i = 0; i < slides.length; i++) {
                slides[i].style.display = "none";  
            }
            this.slideIndex++;
            if (this.slideIndex > slides.length) {this.slideIndex = 1}   
            slides[this.slideIndex-1].style.display = "block";
            setTimeout(this.showSlides, 2500); 
        },
    }
}
</script>

<style>
.place-info-container{
    width: 70%;
    margin-left: auto;
    margin-right: auto;
}
#commonInfo div, span{
    font-size: 15px;
}

.place-info-container img{
    width: 100%;
    height: 650px;
}
</style>