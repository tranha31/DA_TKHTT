<template>
  <div class="form-container d-flex">
      <div class="form-background"></div>
      <div class="form-main d-flex flex-column">
          <div class="header">Thêm mới</div>
          <div class="icon-close" @click="closeForm">X</div>
          <div class="form-title d-flex">
              <div class="title">{{oTourDetail.Name}}</div>
              <div class="flex-1"></div>
              <div class="price">{{oTourDetail.TotalAmount}}đ</div>
          </div>
          <div class="d-flex flex-column content">
            <div class="common-infor d-flex flex-column">
                <BaseInput
                    :clas="'w-half m-b-20'"
                    :stylE="'width:52%'"
                    :hasTitle="true"
                    :title="'Tên tour'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="false"
                    :content="oTourDetail.Name"
                    v-on:changeData="(value)=>{this.oTourDetail.Name = value}"
                    />
                <div class="block first-block d-flex mb-20">
                    <BaseAutoComplete
                    :clas="'w-30 m-r-20'"
                    :hasTitle="true"
                    :title="'Nơi xuất phát'"
                    :notNull="true"
                    :msrequire="true"
                    :placeholder="'Nhập tên tỉnh'"
                    :dataItem="lstProvince"
                    :dataFields="dataProvinceField"
                    :content="oTourDetail.StartPoint"
                    v-on:returnValue="chooseStartPoint"
                    />
                    <div class="m-r-20">
                        <div class="title-input">Thời gian xuất phát&nbsp;&nbsp;<span>*</span></div>
                        <date-picker v-model="oTourDetail.StartTime" type="date" placeholder="Chọn thời gian bắt đầu" 
                        @change="chooseStartTime" id="startTime" ></date-picker>
                    </div>
                    <div class="m-r-20">
                        <div class="title-input">Thời gian kết thúc&nbsp;&nbsp;<span>*</span></div>
                        <date-picker v-model="oTourDetail.EndTime" type="date" placeholder="Chọn thời gian kết thúc" 
                        @change="chooseEndTime" id="endTime"></date-picker>
                    </div>
                </div>
                <div class="block second-block d-flex mb-20">
                    <BaseAutoComplete
                    :clas="'w-30 m-r-20'"
                    :hasTitle="true"
                    :title="'Nơi tham quan'"
                    :notNull="true"
                    :msrequire="true"
                    :placeholder="'Nhập tên tỉnh'"
                    :dataItem="lstProvince"
                    :dataFields="dataProvinceField"
                    :content="oTourDetail.Departure"
                    v-on:returnValue="chooseDestination"
                    />

                    <BaseInput
                    :clas="'w-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Số người lớn'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="true"
                    :content="oTourDetail.NumberAdult"
                    v-on:changeData="changeNumberAdult"
                    />

                    <BaseInput
                    :clas="'w-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Số trẻ em'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="true"
                    :content="oTourDetail.NumberChild"
                    v-on:changeData="changeNumberChild"
                    />

                    <BaseInput
                    :clas="'w-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Số em bé'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="true"
                    :content="oTourDetail.NumberBaby"
                    v-on:changeData="changeNumberBaby"
                    />
                </div>
                <div class="d-flex">
                    <BaseInput
                    :clas="'w-half m-b-20 m-r-20'"
                    :stylE="'width:52%'"
                    :hasTitle="true"
                    :title="'Nơi đón khách'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="false"
                    :content="oTourDetail.PickUpPoint"
                    v-on:changeData="(value)=>{this.oTourDetail.PickUpPoint = value}"
                    />

                    <div class="m-r-20">
                        <div class="title-input">Thời gian đón khách&nbsp;&nbsp;<span>*</span></div>
                        <date-picker v-model="oTourDetail.PickUpTime" type="datetime" placeholder="Chọn thời gian đón khách"></date-picker>
                    </div>
                </div>
            </div>
            <div class="destination d-flex flex-column">
                <div class="title mb-20">Điểm tham quan</div>
                <div class="block-time-line morning mb-20">
                    <table>
                        <thead>
                            <tr>
                                <th rowspan="2" class="location">Địa điểm</th>
                                <th colspan="4">Giá vé (VND)</th>
                            </tr>
                            <tr>
                                <th>Người lớn</th>
                                <th>Trẻ em</th>
                                <th>Em bé</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(v, index) in lstSelectDestination" v-bind:key="index">
                                <td>
                                    <BaseAutoComplete
                                    :notNull="true"
                                    :msrequire="true"
                                    :placeholder="'Nhập tên điểm tham quan'"
                                    :dataItem="lstDestination"
                                    :dataFields="dataFieldDestination"
                                    :content="v.Name"
                                    :index="index"
                                    v-on:returnValue="chooseTourDestination"
                                    />
                                </td>
                                <td class="adult-price" style="text-align:right;">{{v.AdultPrice}}</td>
                                <td class="child-price" style="text-align:right;">{{v.ChildPrice}}</td>
                                <td class="baby-price" style="text-align:right;">{{v.BabyPrice}}</td>
                                <td class="function" @click="removeTourDestination(index)">Xóa</td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="add-new d-flex" @click="addNewDestination">
                        <div>+</div>
                        <div>Thêm điểm tham quan</div>
                    </div>
                </div>
            </div>

            <div class="time-line d-flex flex-column">
                <div class="title mb-20">Lịch trình</div>
                <div v-for="(day, index) in listTimeLine" v-bind:key="index" class="block-time-line morning mb-20">
                    <div class="title mb-12">Ngày {{index+1}}</div>
                    <div class="title mb-12" style="padding-left:5px">Buổi sáng</div>
                    <table style="width:100%">
                        <thead>
                            <tr>
                                <th class="location">Địa điểm</th>
                                <th style="width:20%">Thời gian</th>
                                <th >Hoạt động</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(v, i) in day.Moring" v-bind:key="i">
                                <td>
                                    <BaseAutoComplete
                                    :notNull="true"
                                    :msrequire="true"
                                    :placeholder="'Nhập tên điểm tham quan'"
                                    :dataItem="lstSelectDestination"
                                    :dataFields="dataFieldDestination"
                                    :content="v.Name"
                                    :index="index"
                                    :index2="i"
                                    v-on:returnValue="chooseTourDesMorning"
                                    />
                                </td>
                                <td>
                                    <date-picker v-model="v.Time" type="datetime" placeholder="Chọn thời gian bắt đầu"></date-picker>
                                </td>
                                <td>
                                    <BaseTextArea
                                    :hasTitle="false"
                                    :msrequire="true"
                                    :notNull="true"
                                    :isNumber="false"
                                    :content="day.Moring.Action"
                                    :index="index"
                                    :index2="i"
                                    v-on:changeData="changeContentActionMorning"
                                    />
                                </td>
                                <td class="function" @click="deleteActionMoring(index, i)">Xóa</td>
                            </tr>
                        </tbody>
                    </table>

                    <div class="add-new d-flex m-b-20" @click="addNewActionMoring(index)">
                        <div>+</div>
                        <div>Thêm hoạt động</div>
                    </div>

                    <div class="title mb-12" style="padding-left:5px">Buổi chiều</div>
                    <table style="width:100%">
                        <thead>
                            <tr>
                                <th class="location">Địa điểm</th>
                                <th style="width:20%">Thời gian</th>
                                <th >Hoạt động</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(v, i) in day.Afternoon" v-bind:key="i">
                                <td>
                                    <BaseAutoComplete
                                    :notNull="true"
                                    :msrequire="true"
                                    :placeholder="'Nhập tên điểm tham quan'"
                                    :dataItem="lstSelectDestination"
                                    :dataFields="dataFieldDestination"
                                    :content="v.Name"
                                    :index="index"
                                    :index2="i"
                                    v-on:returnValue="chooseTourDesAfternoon"
                                    />
                                </td>
                                <td>
                                    <date-picker v-model="v.Time" type="datetime" placeholder="Chọn thời gian bắt đầu"></date-picker>
                                </td>
                                <td>
                                    <BaseTextArea
                                    :hasTitle="false"
                                    :msrequire="true"
                                    :notNull="true"
                                    :isNumber="false"
                                    :content="day.Afternoon.Action"
                                    :index="index"
                                    :index2="i"
                                    v-on:changeData="changeContentActionAfternoon"
                                    />
                                </td>
                                <td class="function" @click="deleteActionAfternoon(index, i)">Xóa</td>
                            </tr>
                        </tbody>
                    </table>

                    <div class="add-new d-flex m-b-20" @click="addNewActionAfternoon(index)">
                        <div>+</div>
                        <div>Thêm hoạt động</div>
                    </div>

                    <div class="title mb-12" style="padding-left:5px">Buổi tối</div>
                    <table style="width:100%">
                        <thead>
                            <tr>
                                <th class="location">Địa điểm</th>
                                <th style="width:20%">Thời gian</th>
                                <th >Hoạt động</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(v, i) in day.Evening" v-bind:key="i">
                                <td>
                                    <BaseAutoComplete
                                    :notNull="true"
                                    :msrequire="true"
                                    :placeholder="'Nhập tên điểm tham quan'"
                                    :dataItem="lstSelectDestination"
                                    :dataFields="dataFieldDestination"
                                    :content="v.Name"
                                    :index="index"
                                    :index2="i"
                                    v-on:returnValue="chooseTourDesEvening"
                                    />
                                </td>
                                <td>
                                    <date-picker v-model="v.Time" type="datetime" placeholder="Chọn thời gian bắt đầu"></date-picker>
                                </td>
                                <td>
                                    <BaseTextArea
                                    :hasTitle="false"
                                    :msrequire="true"
                                    :notNull="true"
                                    :isNumber="false"
                                    :content="day.Evening.Action"
                                    :index="index"
                                    :index2="i"
                                    v-on:changeData="changeContentActionEvening"
                                    />
                                </td>
                                <td class="function" @click="deleteActionEvening(index, i)">Xóa</td>
                            </tr>
                        </tbody>
                    </table>

                    <div class="add-new d-flex m-b-20" @click="addNewActionEvening(index)">
                        <div>+</div>
                        <div>Thêm hoạt động</div>
                    </div>
                </div>
                
            </div>
            <!-- <div class="request-customer">
                <div class="title mb-20">Yêu cầu của bên mua</div>
                <table>
                    <tbody>
                        <tr>
                            <td>
                                <BaseAutoComplete/>
                            </td>
                            <td class="function">Xóa</td>
                        </tr>
                    </tbody>
                </table>
                <div class="add-new d-flex">
                        <div>+</div>
                        <div>Thêm mới yêu cầu</div>
                    </div>
            </div> -->
            <div class="other-infor d-flex">
                <div class="other-infor-item cost">
                    <div class="title mb-20">Chi phí đi kèm</div>
                    <table>
                        <thead>
                            <tr>
                                <th style="width: 60%">Loại chi phí</th>
                                <th>Chi phí (VND)</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(v, index) in listAttachPrice" v-bind:key="index">
                                <td>
                                    <BaseInput
                                    :clas="'w-full m-r-20'"
                                    :hasTitle="false"
                                    :msrequire="false"
                                    :notNull="false"
                                    :isNumber="false"
                                    :content="v.Name"
                                    v-on:changeData="(value)=>{this.listAttachPrice[index].Name = value}"
                                    />
                                </td>
                                <td>
                                    <BaseInput
                                    :clas="'w-full m-r-20'"
                                    :hasTitle="false"
                                    :msrequire="false"
                                    :notNull="true"
                                    :isNumber="true"
                                    :content="v.Price"
                                    :index="index"
                                    v-on:changeData="changePriceAttach"
                                    />
                                </td>
                                <td class="function" @click="deleteAttachPrice(index)">Xóa</td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="add-new d-flex" @click="addNewAttachPrice">
                        <div>+</div>
                        <div>Thêm mới chi phí</div>
                    </div>
                </div>
                
            </div>
            <div class="other-infor d-flex" style="width:100%">
                <div class="other-infor-item policy w-full">
                    <div class="title mb-20">Chính sách hoàn hủy</div>
                    <table style="width:100%">
                        <thead>
                            <tr>
                                <th>Nội dung</th>
                                <th style="width:50px"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(v, index) in listPolicy" v-bind:key="index">
                                <td>
                                    <BaseTextArea
                                    :clas="'w-full m-r-20'"
                                    :hasTitle="false"
                                    :msrequire="false"
                                    :notNull="false"
                                    :isNumber="false"
                                    :content="v.Content"
                                    v-on:changeData="(value)=>{this.listPolicy[index].Content = value}"
                                    />
                                </td>
                                <td class="function" @click="deletePolicy(index)">Xóa</td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="add-new d-flex" @click="addNewPolicy">
                        <div>+</div>
                        <div>Thêm mới chính sách</div>
                    </div>
                </div>

            </div>
        
            <div class="note d-flex flex-column w-full">
                <div class="title mb-20">Hướng dẫn</div>
                <textarea></textarea>
            </div>
          </div>
          
          <div class="action d-flex">
              <div class="flex-1"></div>
              <div class="btn" @click="closeForm">Hủy</div>
              <div class="btn btn-save">Xác nhận</div>
          </div>
      </div>

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
  </div>
</template>

<script>
import BaseAutoComplete from '../base/BaseAutoComplete.vue'
import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';
import BaseInput from '../base/BaseInput.vue';
import BasePopUp from '../base/BasePopUp.vue';
import ProvinceAPI from '../../js/api/province'
import DestinationAPI from '../../js/api/destinationapi'
import BaseTextArea from '../base/BaseTextArea.vue';
export default {
  components: { BaseAutoComplete, DatePicker, BaseInput, BasePopUp, BaseTextArea },
  props:{
    oTour : Object,
  },
  data(){
      return{
            oTourDetail : this.oTour,
            lstProvince : [],
            dataProvinceField : {value: "ProvinceName"},
            lstDestination : [],
            dataFieldDestination : {value: "Name"},
            lstSelectDestination : [],

            showPopUp : false,
            type: "error",
            message: null,
            titleP: null,
            action1: "Hủy",
            action2 : "Đóng",
            action3 : "Lưu",
            optionPopUp : [false, false],

            listTimeLine: [],
            listAttachPrice : [],
            listPolicy : [],

      }
  },
  watch:{
    oTour : function(){
        this.oTourDetail = this.oTour
    },

  },
  async created(){
    await ProvinceAPI.getAll()
    .then(res=>{
        this.lstProvince = res.data;
    })
  },
  methods:{
      closeForm(){
          this.$emit("closeForm");
      },

      chooseStartPoint(value){
        var startPoint = this.lstProvince.filter(x=>x.ProvinceName == value);
        if(startPoint.length == 1){
            this.oTourDetail.StartPoint = startPoint[0].ProvinceName;
            this.oTourDetail.StartPointID = startPoint[0].ProvinceID;
        }
      },

      async chooseDestination(value){
        this.lstDestination = [];
        this.lstSelectDestination = [];
        this.listTimeLine.forEach(e=>{
            e.Moring = [];
            e.Afternoon = [];
            e.Evening = [];
        })
        var departure = this.lstProvince.filter(x=>x.ProvinceName == value);
        if(departure.length == 1){
            this.oTourDetail.Departure = departure[0].ProvinceName;
            this.oTourDetail.DepartureID = departure[0].ProvinceID;
            await DestinationAPI.getDesInProvince(this.oTourDetail.DepartureID)
            .then(res=>{
                this.lstDestination = res.data;
                
            })
        }
        this.calculateTotalAmount();
      },

      addNewDestination(){
        if(this.lstSelectDestination.length < this.lstDestination.length){
            var lstSel = this.lstSelectDestination;
            this.lstSelectDestination = [];
            lstSel.push({
                "RefID" : "",
                "Name" : "",
                "AdultPrice" : 0,
                "ChildPrice" : 0,
                "BabyPrice" : 0
            });
            this.lstSelectDestination = lstSel;
        }
      },

      changeNumberAdult(value){
        this.oTourDetail.NumberAdult = value.toString().replaceAll(".", "")
        this.calculateTotalAmount();
      },

      changeNumberChild(value){
        this.oTourDetail.NumberChild = value.toString().replaceAll(".", "")
        this.calculateTotalAmount();
      },

      changeNumberBaby(value){
        this.oTourDetail.NumberBaby = value.toString().replaceAll(".", "")
        this.calculateTotalAmount();
      },

      chooseTourDestination(value, index){
        var des = this.lstDestination.filter(x=>x.Name == value)
        if(des.length > 0){
            var tikcet = des[0].TicketPrice
            tikcet = JSON.parse(tikcet)
            this.lstSelectDestination[index].RefID = des[0].RefID;
            this.lstSelectDestination[index].Name = des[0].Name;
            this.lstSelectDestination[index].AdultPrice = tikcet.Adult.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ".");
            this.lstSelectDestination[index].ChildPrice = tikcet.Child.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ".");
            this.lstSelectDestination[index].BabyPrice = tikcet.Baby.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ".");
            this.calculateTotalAmount();
        }
      },

      calculateTotalAmount(){
        var ticketAdult = 0;
        var ticketChild = 0;
        var ticketBaby = 0;

        for(var i=0; i<this.lstSelectDestination.length; i++){
            var item = this.lstSelectDestination[i];
            ticketAdult = ticketAdult + Number.parseInt(item.AdultPrice.replaceAll(".", ""));
            ticketChild = ticketChild + Number.parseInt(item.ChildPrice.replaceAll(".", ""));
            ticketBaby = ticketBaby + Number.parseInt(item.BabyPrice.replaceAll(".", ""));
        }

        var totalAttachPrice = 0;
        for(var j=0; j<this.listAttachPrice.length; j++){
            totalAttachPrice = totalAttachPrice + Number.parseInt(this.listAttachPrice[j].Price)
        }

        var totalAmount = ticketAdult * Number.parseInt(this.oTourDetail.NumberAdult)
                    + ticketChild * Number.parseInt(this.oTourDetail.NumberChild)
                    + ticketBaby * Number.parseInt(this.oTourDetail.NumberBaby)
                    + totalAttachPrice;
        
        this.oTourDetail.TotalAmount = totalAmount.toString().replace(/\D/g, "").replace(/\B(?=(\d{3})+(?!\d))/g, ".");
      },

      removeTourDestination(index){
        var refID = this.lstSelectDestination[index].RefID;
        var use = false;
        for(var i=0; i<this.listTimeLine.length; i++){
            var item = this.listTimeLine[i];
            for(var k=0; k<item.Moring.length; k++){
                if(item.Moring[k].RefID == refID){
                    use = true;
                }
            }

            for(k=0; k<item.Afternoon.length; k++){
                if(item.Afternoon[k].RefID == refID){
                    use = true;
                }
            }

            for(k=0; k<item.Evening.length; k++){
                if(item.Evening[k].RefID == refID){
                    use = true;
                }
            }
        }

        if(use){
            this.titleP = "Cảnh báo";
            this.message = "Địa điểm đã phát sinh quan hệ. Không thể xóa";
            this.showPopUp = true;
        }
        else{
            this.titleP = "";
            this.message = "";
            this.lstSelectDestination.splice(index, 1);
            this.calculateTotalAmount()
        }
      },

      chooseStartTime(){
        var input = document.getElementById("startTime").querySelector("input");
        var inputT = document.getElementById("endTime").querySelector("input");
        if(this.oTourDetail.StartTime > this.oTourDetail.EndTime){
            this.message = "Ngày bắt đầu phải nhỏ hơn ngày kết thúc";
            this.titleP = "Thời gian không hợp lệ"
            input.classList.add("error")
            this.showPopUp = true;
        }
        else{
            this.message = "";
            this.titleP = ""
            input.classList.remove("error")
            inputT.classList.remove("error")
            if(this.oTourDetail.StartTime && this.oTourDetail.EndTime){
                var difference = this.oTourDetail.EndTime.getTime() - this.oTourDetail.StartTime.getTime();
                var days = Math.ceil(difference / (1000 * 3600 * 24));
                this.oTourDetail.TotalDay = days;
                this.initListTimeLine();
            }
            else if(!this.oTourDetail.StartTime && !this.oTourDetail.EndTime){
                this.listTimeLine = []
            }
            
        }
      },

      chooseEndTime(){
        var input = document.getElementById("endTime").querySelector("input");
        var inputT = document.getElementById("startTime").querySelector("input");
        if(this.oTourDetail.StartTime > this.oTourDetail.EndTime){
            this.message = "Ngày bắt đầu phải nhỏ hơn ngày kết thúc";
            this.titleP = "Thời gian không hợp lệ"
            input.classList.add("error")
            this.showPopUp = true;
        }
        else{
            this.message = "";
            this.titleP = ""
            input.classList.remove("error")
            inputT.classList.remove("error")

            if(this.oTourDetail.StartTime && this.oTourDetail.EndTime){
                var difference = this.oTourDetail.EndTime.getTime() - this.oTourDetail.StartTime.getTime();
                var days = Math.ceil(difference / (1000 * 3600 * 24));
                this.oTourDetail.TotalDay = days;
                this.initListTimeLine();
            }
            else if(!this.oTourDetail.StartTime && !this.oTourDetail.EndTime){
                this.listTimeLine = []
            }
        }
      },

      initListTimeLine(){
        var nDay = this.oTourDetail.TotalDay;
        if(nDay > this.listTimeLine.length){
            while(this.listTimeLine.length != nDay){
                this.listTimeLine.push({
                    "Moring": [],
                    "Afternoon": [],
                    "Evening": []
                })
            }
        }
        else{
            while(this.listTimeLine.length != nDay){
                this.listTimeLine.splice(this.listTimeLine.length-1, 1); 
            }
        }
      },

      addNewActionMoring(index){
        this.listTimeLine[index].Moring.push({
            "Name" : "",
            "RefID" : "",
            "Time": null,
            "Action": ""
        })
      },

      deleteActionMoring(index, i){
        this.listTimeLine[index].Moring.splice(i, 1)
      },

      addNewActionAfternoon(index){
        this.listTimeLine[index].Afternoon.push({
            "Name" : "",
            "RefID" : "",
            "Time": null,
            "Action": ""
        })
      },

      deleteActionAfternoon(index, i){
        this.listTimeLine[index].Afternoon.splice(i, 1)
      },

      addNewActionEvening(index){
        this.listTimeLine[index].Evening.push({
            "Name" : "",
            "RefID" : "",
            "Time": null,
            "Action": ""
        })
      },

      deleteActionEvening(index, i){
        this.listTimeLine[index].Evening.splice(i, 1)
      },

      chooseTourDesMorning(value, index, i){
        var des = this.lstSelectDestination.filter(x=>x.Name == value)
        if(des.length == 1){
            this.listTimeLine[index].Moring[i].Name = value;
            this.listTimeLine[index].Moring[i].RefID = des[0].RefID;
        }
      },

      chooseTourDesAfternoon(value, index, i){
        var des = this.lstSelectDestination.filter(x=>x.Name == value)
        if(des.length == 1){
            this.listTimeLine[index].Afternoon[i].Name = value;
            this.listTimeLine[index].Afternoon[i].RefID = des[0].RefID;
        }
      },

      chooseTourDesEvening(value, index, i){
        var des = this.lstSelectDestination.filter(x=>x.Name == value)
        if(des.length == 1){
            this.listTimeLine[index].Evening[i].Name = value;
            this.listTimeLine[index].Evening[i].RefID = des[0].RefID;
        }
      },

      changeContentActionMorning(value, index, i){
        this.listTimeLine[index].Moring[i].Action = value;
      },

      changeContentActionAfternoon(value, index, i){
        this.listTimeLine[index].Moring[i].Action = value;
      },

      changeContentActionEvening(value, index, i){
        this.listTimeLine[index].Moring[i].Action = value;
      },

      addNewAttachPrice(){
        this.listAttachPrice.push({
            "Name" : "",
            "Price" : 0
        })
      },

      deleteAttachPrice(index){
        this.listAttachPrice.splice(index, 1);
        this.calculateTotalAmount()
      },
      
      changePriceAttach(value, index){
        this.listAttachPrice[index].Price = value
        this.calculateTotalAmount()
      },
      
      addNewPolicy(){
        this.listPolicy.push({"Content" : ""})
      },

      deletePolicy(indnex){
        this.listPolicy.splice(indnex, 1);
        
      }
  }
}
</script>

<style>
@import url(../../css/form/createform.css);
.form-container input{
    border-radius: 5px;
}
</style>