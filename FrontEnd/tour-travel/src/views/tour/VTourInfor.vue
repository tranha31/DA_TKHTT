<template>
  <div>
      <div class="tour-contain">
        <div class="search">
            <div class="search-main">
                <div class="search-title">
                  <router-link to="/tour" class="link active">Tour &amp; Trải nghiệm</router-link>
                  <router-link to="/test" class="link">Khách sạn</router-link>
                </div>
                <div class="search-content">
                    <BaseInput
                    :clas="'w-half m-r-20'"
                    :placeholder="'Nhập hoạt động'"
                    :hasImage="true"
                    :classImage="'mi-14 icon-search'"
                    :content="search"
                    v-on:changeData="(value)=>{this.search = value}"
                    />

                    <BaseAutoComplete
                    :clas="'w-30'"
                    :placeholder="'Chọn tỉnh muốn du lịch'"
                    :hasImage="true"
                    :classImage="'mi-14 icon-location'"
                    :dataFields="dataProvinceField"
                    :dataItem="lstProvince"
                    v-on:returnValue="chooseDestinationPoint"
                    />
                    <div class="flex-1"></div>
                    <div class="btn btn-save m-l-10" style="min-width: 100px" @click="searchTour">Tìm kiếm</div>
                </div>
            </div>
        </div>
        <div class="grid-content d-flex flex-column">
          <div class="overview mb-30">
              <div class="title">{{object.title}}</div>
              <div class="d-flex">
                  <img v-for="(v, index) in object.imageUrl" v-bind:key="index" class="image w-60 slide fade slideTour" :src="v">
                  <div class="d-flex flex-column w-40" style="padding-left: 20px">
                    <div class="d-flex p-b-20">
                      <div>Mã tour: {{object.code}}</div>
                      <div class="flex-1"></div>
                    </div>
                    <div class="price p-b-30">{{object.price}}</div>
                    <div class="d-flex p-b-30">
                        <div class="btn btn-save" @click="showFormCreateTour(object.id)">Đặt tour ngay</div>
                        <div class="flex-1"></div>
                        <div class="mi mi-32 icon-cart" @click="addToCart"></div>
                    </div>
                    <div class="w-full d-flex">
                        <div class="mi mi-14 icon-tick m-r-10"></div>
                        <span>Gá tốt nhất</span>
                    </div>
                    <div class="w-full d-flex">
                        <div class="mi mi-14 icon-tick m-r-10"></div>
                        <span>Thanh toán tức thì</span>
                    </div>
                    <div class="w-full d-flex">
                        <div class="mi mi-14 icon-tick m-r-10"></div>
                        <span>Trải nghiệm hoàn hảo</span>
                    </div>
                  </div>
                  
              </div>
          </div>
          
          <div class="tour-infor mb-30">
            <div class="d-flex option mb-20">
                <div class="option-item active" @click="changeInfo(0)">Thông tin tour</div>
                <div class="option-item" @click="changeInfo(1)">Lịch trình</div>
                <div class="option-item" @click="changeInfo(2)">Chính sách hoàn hủy</div>
                <div class="option-item" @click="changeInfo(3)">Hướng dẫn</div>
            </div>
            <div class="content">
                <div id="commonInfo" class="info w-full flex-column d-flex" style="line-height:30px">
                    <div class="">Điểm xuất phát: <span style="">{{masterInfo.FromName}}</span></div>
                    <div class="">Điểm tới: <span style="">{{masterInfo.ToName}}</span></div>
                    <div class="">Điểm đón khách: <span style="">{{masterInfo.PickupName}}</span></div>
                    <div class="d-flex flex-column ">Danh sách điểm du lịch:
                        <div class="d-flex flex-column" style="padding:10px 0 10px 20px" v-for="(v, index) in masterInfo.Destination" v-bind:key="index">
                            <div>Địa danh: <span style="">{{v.Name}}</span></div>
                            <div class="d-flex flex-column">Giá vé:
                                <div style="padding-left:10px">Người lớn: <span style="">{{v.Adult}} đ</span></div>
                                <div style="padding-left:10px">Trẻ em: <span style="">{{v.Child}} đ</span></div>
                                <div style="padding-left:10px">Em bé: <span style="">{{v.Baby}} đ</span></div>
                            </div>
                        </div>
                    </div>
                    <div class="">Bao gồm: <span style="">{{masterInfo.NumberAdult}}</span> người lớn, <span style="">{{masterInfo.NumberChild}}</span> trẻ em, <span style="">{{masterInfo.NumberBaby}}</span> em bé</div>
                    <div class="">Thời gian tour: {{masterInfo.TourTime}}</div>
                    <div class="d-flex flex-column">Chi phí đi kèm:
                        <div class="d-flex flex-column" style="padding:10px 0 10px 20px" v-for="(v, index) in masterInfo.AttachCost" v-bind:key="index">
                            <div>Nội dung: <span style="">{{v.Name}}</span></div>
                            <div class="">Chi phí: <span style="">{{v.Cost}} đ</span></div>
                        </div>
                    </div>
                </div>

                <div id="schedule" class="info flex-column d-none">
                    <div class="d-flex flex-column" v-for="(v, index) in tourSchedule" v-bind:key="index">
                        <div class="d-flex flex-column">
                            <div class="font-bold">Ngày {{index+1}}:</div>
                            <div style="padding-left:10px; padding-top:10px">Buổi sáng:</div>
                            <div v-for="(value, i) in v.Morning" v-bind:key="i" class="d-flex flex-column" style="padding:10px 0 10px 20px">
                                <div>Địa điểm: {{value.Name}}</div>
                                <div>Thời gian: {{value.Time}}</div>
                                <div>Hoạt động: {{value.Action}}</div>
                            </div>
                            <div style="padding-left:10px">Buổi chiều:</div>
                            <div v-for="(value, i) in v.Afternoon" v-bind:key="i" class="d-flex flex-column" style="padding:10px 0 10px 20px">
                                <div>Địa điểm: {{value.Name}}</div>
                                <div>Thời gian: {{value.Time}}</div>
                                <div>Hoạt động: {{value.Action}}</div>
                            </div>
                            <div style="padding-left:10px">Buổi tối:</div>
                            <div v-for="(value, i) in v.Evening" v-bind:key="i" class="d-flex flex-column" style="padding:10px 0 10px 20px">
                                <div>Địa điểm: {{value.Name}}</div>
                                <div>Thời gian: {{value.Time}}</div>
                                <div>Hoạt động: {{value.Action}}</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div id="policy" class="info flex-column d-none">
                    <div v-for="(v, index) in policy" v-bind:key="index" class="d-flex" style="padding:10px">
                        <span>{{index+1}}.&nbsp;</span>
                        <span>{{v.Content}}</span>
                    </div>
                </div>
                <div id="tutorial" class="info flex-column d-none">
                    <div v-for="(v, index) in tutorial" v-bind:key="index" class="d-flex" style="padding:10px">
                        <span>{{index+1}}.&nbsp;</span>
                        <span>{{v.Content}}</span>
                    </div>
                </div>
            </div>
          </div>

          <div class="suggest-tour">
              <div class="title mb-30">Tour tương tự</div>
              <div class="suggest-container d-flex">
                  <div class="prev" @click="showPrevSuggest()"></div>
                  <div class="next" @click="showNextSuggest()"></div>
                  <div v-for="(v, index) in suggestItem" v-bind:key="index" class="suggest-item d-flex flex-column w-33 fade">
                      <img class="image" :src="v.imageUrl">
                      <a class="title" :title="v.title" :href="v.id">{{v.title}}</a>
                      <div class="flex-1"></div>
                      <div class="d-flex other-info">
                        <div class="flex-1"></div>
                        <div class="price">{{v.price}}</div>
                      </div>
                  </div>
              </div>
          </div>
        </div>
    </div>

    <TheCreateTour v-if="showForm"
    :oTour="oTour"
    :mode="1"
    :oData="oData"
    :TitleTour="'Khởi tạo tour'"
    v-on:closeForm="closeForm"
    />

    <div id="toast"></div>
    <BaseLoad :load="showLoad"/>

    <BasePopUp
    :isShow="showPopUp"
    :type="type"
    :message="message"
    :title="titleP"
    :action1="action1"
    :action2="action2"
    :action3="action3"
    :show="optionPopUp"
    v-on:confirmAction3="()=>{this.showPopUp = false;}"
    />

    <ThePageInfo/>
  </div>
</template>

<script>
import BaseAutoComplete from '../../components/base/BaseAutoComplete.vue'
import BaseInput from '../../components/base/BaseInput.vue'
import BaseLoad from '../../components/base/BaseLoad.vue'
import BasePopUp from '../../components/base/BasePopUp.vue'
import TheCreateTour from '../../components/form/TheCreateTour.vue'
import ThePageInfo from '../../components/layout/ThePageInfo.vue'
import TourAPI from "../../js/api/tourapi"
import Tour from '../../js/entity/tour'
import ProvinceAPI from "../../js/api/province"
export default {
    components: { ThePageInfo, BaseInput, BaseAutoComplete, TheCreateTour, BaseLoad, BasePopUp},
    data(){
        return{
            id: null,
            slideIndex : 0,
            suggestIndex: 0,
            showForm: false,
            showLoad: false,
            showPopUp : false,
            type: "error",
            message: null,
            titleP: null,
            action1: "Hủy",
            action2 : "Đóng",
            action3 : "Xóa",
            optionPopUp : [false, false],
            object: {},

            suggestItem:[],

            masterInfo: {},
            tourSchedule : [],
            policy: [],
            tutorial: [],
            
            contentInfor: "<div>kjkjkj</div>",
            lstProvince : [],
            dataProvinceField : {value: "ProvinceName"},
            search : "",
            toID : "",

            oTour : new Tour(),
            oData: null,

        }
    },
    watch:{
        '$route'(to, from){
            this.id = to.params.id;
            from;
        }
    },
    async created(){
        this.id = this.$route.params.id;
        this.showLoad = true

        await ProvinceAPI.getAll()
        .then(res=>{
            this.lstProvince = res.data;
        })

        var toID = ""
        await TourAPI.getByID(this.id)
        .then(res=>{
            var data = res.data
            this.object = {
                id: this.id,
                imageUrl: data.Image,
                title: data.Master.TourName,
                code: data.Master.ContractCode,
                price: data.Master.TotalCost.replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ".") + " VNĐ",
            };
            toID = data.Master.ProvinceDestinationID
            this.bindingMasterData(data)
            this.bindingDataSchedule(data)
            this.bindingPolicyData(data)
            this.bindingDataTutorial(data)
        })
        .catch(()=>{
          this.toast({
              title: "Có lỗi xảy ra. Vui lòng thử lại",
              type: "error",
              duration: 3000,
          });
        })

        await TourAPI.getListTourSuggest(this.id, toID)
        .then(res=>{
            var data = res.data.data
            var image = res.data.listImage
            for(var i=0; i<data.length; i++){
                var item = data[i]
                var img = image[i].Image
                var randIndex = Math.floor(Math.random() * img.length)
                var object = {
                    id: item.TourID,
                    imageUrl: img[randIndex],
                    title: item.TourName,
                    code: item.TourCode,
                    price: item.Price.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ".") + " VNĐ",
                };
                this.suggestItem.push(object)
            }
            
        })

        setTimeout(()=>{    
            this.showSlides();
            this.setUpShowSuggest();
        }, 100)

        this.showLoad = false
    },
    mounted(){

    },
    methods:{
        searchTour(){
            if(!this.search){
                this.search = undefined
            }
            if(!this.toID){
                this.toID = undefined
            }
            this.$router.push({ path: '/tours/'+this.search+"/"+this.toID})
        },

        bindingMasterData(data){
            this.masterInfo = {}
            this.masterInfo.FromName = data.Master.ProvinceStartName
            this.masterInfo.ToName = data.Master.ProvinceDestinationName
            this.masterInfo.PickupName = data.Master.PickupAdress
            
            var destination = data.Destination
            this.masterInfo.Destination = []
            destination.forEach(e => {
                this.masterInfo.Destination.push({
                    "Name" : e.Name,
                    "Adult": e.TicketPrice.Adult.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, "."),
                    "Child" : e.TicketPrice.Child.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, "."),
                    "Baby" : e.TicketPrice.Baby.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ".")
                })
            });

            this.masterInfo.NumberAdult = data.Contract.NumberAdult
            this.masterInfo.NumberChild = data.Contract.NumberChild
            this.masterInfo.NumberBaby = data.Contract.NumberBaby
            this.masterInfo.TourTime = data.Contract.TotalHour + " giờ"
            this.masterInfo.AttachCost = []

            var lstAttach = data.AttachOption
            lstAttach.forEach(e=>{
                this.masterInfo.AttachCost.push({
                    "Name" : e.Name,
                    "Cost": e.Price
                })
            })

        },

        bindingDataSchedule(data){
            var schedule = data.Schedule
            this.tourSchedule = []
            var me = this
            schedule.forEach(e=>{
                e.Morning.forEach(k=>{
                    var time = new Date(k.Time)
                    k.Time = new Date(time.setTime(time.getTime() - (7*60*60*1000)))
                    k.Time = k.Time.getHours() + ':' + me.padTo2Digits(k.Time.getMinutes())
                })

                e.Afternoon.forEach(k=>{
                    var time = new Date(k.Time)
                    k.Time = new Date(time.setTime(time.getTime() - (7*60*60*1000)))
                    k.Time = k.Time.getHours() + ':' + me.padTo2Digits(k.Time.getMinutes())
                })

                e.Evening.forEach(k=>{
                    var time = new Date(k.Time)
                    k.Time = new Date(time.setTime(time.getTime() - (7*60*60*1000)))
                    k.Time = k.Time.getHours() + ':' + me.padTo2Digits(k.Time.getMinutes())
                }) 
                
                this.tourSchedule.push(e)
            })
        },

        bindingPolicyData(data){
            var cancel = data.RefundPolicy
            this.policy = []
            cancel.forEach(e=>{
                this.policy.push({
                    "Content" : e.Content
                })
            })
        },

        bindingDataTutorial(data){
            var tuto = data.Tutorial
            this.tutorial = []
            tuto.forEach(e=>{
                this.tutorial.push({
                    "Content" : e.Content
                })
            })
        },

        padTo2Digits(num) {
            return String(num).padStart(2, '0');
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

        chooseDestinationPoint(pName){
            var me = this;
            var province = this.lstProvince.filter(x=>x.ProvinceName == pName);
            if(province.length == 1){
                me.toID = province[0].ProvinceID
            }
        },

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

        /**
         * Thay đổi thông tin hiển thị 
         */
        changeInfo(index){
            var infos =  document.getElementsByClassName("option-item");
            for (var i = 0; i < infos.length; i++) {
                infos[i].classList.remove("active");  
            }
            infos[index].classList.add("active");

            var divInfo = document.querySelectorAll(".info")
            divInfo.forEach(e=>{
                e.classList.remove("d-flex")
                e.classList.add("d-none")
            })
            switch(index){
                case 0:
                    var common = document.getElementById("commonInfo")
                    common.classList.remove("d-none")
                    common.classList.add("d-flex")
                    break
                case 1:
                    var sche = document.getElementById("schedule")
                    sche.classList.remove("d-none")
                    sche.classList.add("d-flex")
                    break
                case 2:
                    var poli = document.getElementById("policy")
                    poli.classList.remove("d-none")
                    poli.classList.add("d-flex")
                    break
                case 3:
                    var tuto = document.getElementById("tutorial")
                    tuto.classList.remove("d-none")
                    tuto.classList.add("d-flex")
                    break
            }
            

        },

        setUpShowSuggest(){
            let i;
            let items = document.getElementsByClassName("suggest-item");
            for (i = 0; i < items.length; i++) {
                if(i < 3){
                    items[i].style.display = "flex";
                    items[i].style.left = i*33.733333333 + "%";
                }
                else{
                    items[i].style.display = "none";
                }
            }
            
        },

        /**
         * Dịch toàn bộ sang bên phải
         */
        showPrevSuggest(){
            let i;
            let items = document.getElementsByClassName("suggest-item");
            let len = items.length;
            for (i = 0; i < items.length; i++) {
                items[i].style.display = "none";
            }
            if(this.suggestIndex == 0){
                items[len-1].style.display = "flex";
                items[len-1].style.left =  "0";

                items[0].style.display = "flex";
                items[0].style.left =  "33.733333333%";

                items[1].style.display = "flex";
                items[1].style.left =  33.733333333*2 + "%";

                this.suggestIndex = len - 1;
                
            }
            else if(this.suggestIndex == len-1){
                items[len-2].style.display = "flex";
                items[len-2].style.left =  "0";

                items[len-1].style.display = "flex";
                items[len-1].style.left =  "33.733333333%";

                items[0].style.display = "flex";
                items[0].style.left =  33.733333333*2 + "%";

                this.suggestIndex = this.suggestIndex - 1;
                if(this.suggestIndex < 0) {
                    this.suggestIndex = 0;
                }
            }
            else if(this.suggestIndex == 1){
                items[0].style.display = "flex";
                items[0].style.left =  "0";

                items[1].style.display = "flex";
                items[1].style.left =  "33.733333333%";

                items[2].style.display = "flex";
                items[2].style.left =  33.733333333*2 + "%";

                this.suggestIndex = 0;
            }
            else{
                var index = this.suggestIndex;
                items[index-1].style.display = "flex";
                items[index-1].style.left =  "0";

                items[index].style.display = "flex";
                items[index].style.left =  "33.733333333%";

                items[index+1].style.display = "flex";
                items[index+1].style.left =  33.733333333*2 + "%";

                this.suggestIndex = this.suggestIndex - 1;
                if(this.suggestIndex < 0) {
                    this.suggestIndex = 0;
                }
            }
        },

        /**
         * Dịch toàn bộ qua trái
         */
        showNextSuggest(){
            let i;
            let items = document.getElementsByClassName("suggest-item");
            let len = items.length;
            for (i = 0; i < items.length; i++) {
                items[i].style.display = "none";
            }
            if(this.suggestIndex == 0){
                items[1].style.display = "flex";
                items[1].style.left =  "0";

                items[2].style.display = "flex";
                items[2].style.left = "33.733333333%";

                let index = this.suggestIndex + 3 == len ? len-1 : this.suggestIndex + 3;
                items[index].style.display = "flex";
                items[index].style.left =  33.733333333*2 + "%";

                this.suggestIndex = 1;
                
            }
            else if(this.suggestIndex == len-1){
                items[0].style.display = "flex";
                items[0].style.left =  "0";

                items[1].style.display = "flex";
                items[1].style.left =  "33.733333333%";

                items[2].style.display = "flex";
                items[2].style.left =  33.733333333*2 + "%";

                this.suggestIndex = 0;
            }
            else if(this.suggestIndex == len-2){
                items[len-1].style.display = "flex";
                items[len-1].style.left =  "0";

                items[0].style.display = "flex";
                items[0].style.left =  "33.733333333%";

                items[1].style.display = "flex";
                items[1].style.left =  33.733333333*2 + "%";

                this.suggestIndex = len-1;
            }
            else{
                items[this.suggestIndex+1].style.display = "flex";
                items[this.suggestIndex+1].style.left =  "0";

                items[this.suggestIndex+2].style.display = "flex";
                items[this.suggestIndex+2].style.left =  "33.733333333%";

                let inDex = this.suggestIndex+3 == len ? 0 : this.suggestIndex+3;
                items[inDex].style.display = "flex";
                items[inDex].style.left =  33.733333333*2 + "%";

                this.suggestIndex = this.suggestIndex + 1;
                if(this.suggestIndex == len) {
                    this.suggestIndex = 0;
                }
            }
        },

        async addToCart(){
            if (!this.$store.state.account.currentUser || (this.$store.state.account.currentUser && !this.$store.state.account.currentUser.UserID)) {
                this.$notify({
                    group: 'default',
                    title: 'Error',
                    text: 'Please completed login first!',
                    type: 'error',
                    position: 'bottom right'
                })
                this.$router.push({ path: '/login'})
                return
            }
            var data = {
                "TourID" : this.object.id,
                "UserID" : this.$store.state.account.currentUser.UserID
            }

            data = JSON.stringify(data)
            this.showLoad = true
            await TourAPI.addToCart(data)
            .then(res=>{
                if(res.data.error == "ExistInCart"){
                    this.toast({
                        title: "Tour đã tồn tại trong vào giỏ hàng",
                        type: "warning",
                        duration: 3000,
                    });
                }
                else{
                    this.toast({
                        title: "Thêm vào giỏ hàng thành công",
                        type: "success",
                        duration: 3000,
                    });
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

        /**
         * Show form tạo tour
         */
        async showFormCreateTour(id){
            this.showLoad = true
            await TourAPI.getByID(id)
            .then(res=>{
                var data = res.data
                var tour = new Tour();
                this.oTour = tour;
                this.oTour.Name = data.Master.TourName
                this.oTour.TourCode = data.Master.ContractCode
                this.oTour.CreatedTime = data.Master.CreatedTime
                this.oTour.TotalAmount = Number.parseInt(data.Master.TotalCost)
                this.oTour.Departure = data.Master.ProvinceDestinationName
                this.oTour.DepartureID = data.Master.ProvinceDestinationID
                this.oTour.StartPoint = data.Master.ProvinceStartName
                this.oTour.StartPointID = data.Master.ProvinceStartID
                this.oTour.PickUpPoint = data.Master.PickupAdress
                this.oTour.NumberAdult = Number.parseInt(data.Contract.NumberAdult)
                this.oTour.NumberChild = Number.parseInt(data.Contract.NumberChild)
                this.oTour.NumberBaby = Number.parseInt(data.Contract.NumberBaby)
                this.oTour.TotalDay = Number.parseInt(data.Contract.TotalHour)

                var pickupTime = new Date(data.Master.PickupTime)
                var startTime = new Date(data.Contract.StartTime)
                var endTime = new Date(data.Contract.EndTime)
                this.oTour.PickUpTime = new Date(pickupTime.setTime(pickupTime.getTime() - (7*60*60*1000)))
                this.oTour.StartTime = new Date(startTime.setTime(startTime.getTime() - (7*60*60*1000)))
                this.oTour.EndTime = new Date(endTime.setTime(endTime.getTime() - (7*60*60*1000)))
                
                this.oTour.Sample = data.Info.Sample
                this.oTour.Status = 0
                this.oTour.IsPayment = data.Info.IsPayment
                this.oTour.TourID = "0000"
                
                data.Schedule.forEach(e=>{
                    e.Morning.forEach(k=>{
                        var time = new Date(k.Time)
                        k.Time = new Date(time.setTime(time.getTime() - (7*60*60*1000)))
                    })

                    e.Afternoon.forEach(k=>{
                        var time = new Date(k.Time)
                        k.Time = new Date(time.setTime(time.getTime() - (7*60*60*1000)))
                    })

                    e.Evening.forEach(k=>{
                        var time = new Date(k.Time)
                        k.Time = new Date(time.setTime(time.getTime() - (7*60*60*1000)))
                    })
                })

                data.AttachOption.forEach(e=>{
                    e.Price = e.Price.toString()
                                    .replace(/\D/g, "")
                                    .replace(/\B(?=(\d{3})+(?!\d))/g, ".")
                })

                this.oData = data
                this.showForm = true;

                this.showLoad = false
            })
            .catch(()=>{
                this.showLoad = false
                this.toast({
                    title: "Có lỗi xảy ra. Vui lòng thử lại",
                    type: "error",
                    duration: 3000,
                });
            })
        },

        closeForm(){
            this.showForm = false;
        },
    }
}
</script>

<style>
@import url(../../css/content/tour.css);
@import url(../../css/content/tourinfor.css);

.tour-contain .e-autocomplete{
  padding-left: 25px !important;
}

</style>