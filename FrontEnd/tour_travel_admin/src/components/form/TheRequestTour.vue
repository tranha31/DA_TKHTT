<template>
  <div class="form-container d-flex" id="tourTemplate">
    <div class="form-background"></div>
    <div class="form-main d-flex flex-column">
      <div class="header">{{TitleTour}}</div>
      <div class="icon-close" @click="closeForm">X</div>
      <div class="form-title d-flex">
        <div class="title">{{ oTourDetail.Name }}</div>
        <div class="flex-1"></div>
        <div class="price">{{ oTourDetail.TotalAmount }}đ</div>
      </div>
      <div class="d-flex flex-column content">
        <div class="common-infor d-flex flex-column" id="tourTemplateGeneral">
          <BaseInput
            :clas="'w-half m-b-20'"
            :stylE="'width:52%'"
            :hasTitle="true"
            :title="'Tên tour'"
            :msrequire="true"
            :notNull="true"
            :isNumber="false"
            :disabled="true"
            :content="oTourDetail.Name"
            v-on:changeData="
              (value) => {
                this.oTourDetail.Name = value;
              }
            "
          />
          <div class="block first-block d-flex mb-20">
            <BaseAutoComplete
              :clas="'w-30 m-r-20'"
              :hasTitle="true"
              :title="'Nơi xuất phát'"
              :notNull="true"
              :msrequire="true"
              :placeholder="'Nhập tên tỉnh'"
              :disable="true"
              :dataItem="lstProvince"
              :dataFields="dataProvinceField"
              :content="oTourDetail.StartPoint"
              v-on:returnValue="chooseStartPoint"
            />
            <div class="m-r-20">
              <div class="title-input">
                Thời gian xuất phát&nbsp;&nbsp;<span>*</span>
              </div>
              <date-picker
                v-model="oTourDetail.StartTime"
                type="date"
                placeholder="Chọn thời gian bắt đầu"
                :editable="false"
                :disabled="true"
                @change="chooseStartTime"
                id="startTime"
              ></date-picker>
            </div>
            <div class="m-r-20">
              <div class="title-input">
                Thời gian kết thúc&nbsp;&nbsp;<span>*</span>
              </div>
              <date-picker
                v-model="oTourDetail.EndTime"
                type="date"
                placeholder="Chọn thời gian kết thúc"
                :editable="false"
                :disabled="true"
                @change="chooseEndTime"
                id="endTime"
              ></date-picker>
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
              :disable="true"
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
              :disabled="true"
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
              :disabled="true"
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
              :disabled="true"
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
              :disabled="true"
              :content="oTourDetail.PickUpPoint"
              v-on:changeData="
                (value) => {
                  this.oTourDetail.PickUpPoint = value;
                }
              "
            />

            <div class="m-r-20">
              <div class="title-input">
                Thời gian đón khách&nbsp;&nbsp;<span>*</span>
              </div>
              <date-picker
                v-model="oTourDetail.PickUpTime"
                type="datetime"
                placeholder="Chọn thời gian đón khách"
                :editable="false"
                :disabled="true"
                :disabled-date="disabledBeforeStartTimeAndAfterEndTime"
              ></date-picker>
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
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="(v, index) in lstSelectDestination"
                  v-bind:key="index"
                >
                  <td>
                    <BaseAutoComplete
                      :notNull="true"
                      :msrequire="true"
                      :placeholder="'Nhập tên điểm tham quan'"
                      :dataItem="lstDestination"
                      :dataFields="dataFieldDestination"
                      :content="v.Name"
                      :index="index"
                      :disable="true"
                      v-on:returnValue="chooseTourDestination"
                    />
                  </td>
                  <td class="adult-price" style="text-align: right">
                    {{ v.AdultPrice }}
                  </td>
                  <td class="child-price" style="text-align: right">
                    {{ v.ChildPrice }}
                  </td>
                  <td class="baby-price" style="text-align: right">
                    {{ v.BabyPrice }}
                  </td>
                </tr>
              </tbody>
            </table>
            <!-- <div class="add-new d-flex" @click="addNewDestination">
              <div>+</div>
              <div>Thêm điểm tham quan</div>
            </div> -->
          </div>
        </div>

        <div class="time-line d-flex flex-column">
          <div class="title mb-20">Lịch trình</div>
          <div
            v-for="(day, index) in listTimeLine"
            v-bind:key="index"
            class="block-time-line morning mb-20"
          >
            <div class="title mb-12">Ngày {{ index + 1 }}</div>
            <div class="title mb-12" style="padding-left: 5px">Buổi sáng</div>
            <table style="width: 100%">
              <thead>
                <tr>
                  <th class="location">Địa điểm</th>
                  <th style="width: 20%">Thời gian</th>
                  <th>Hoạt động</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(v, i) in day.Morning" v-bind:key="i">
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
                      :disable="true"
                      v-on:returnValue="chooseTourDesMorning"
                    />
                  </td>
                  <td>
                    <date-picker
                      v-model="v.Time"
                      type="datetime"
                      placeholder="Chọn thời gian bắt đầu"
                      :editable="false"
                      :disabled="true"
                      :disabled-date="disabledBeforeStartTimeAndAfterEndTime"
                    ></date-picker>
                  </td>
                  <td>
                    <BaseTextArea
                      :hasTitle="false"
                      :msrequire="true"
                      :notNull="true"
                      :isNumber="false"
                      :content="v.Action"
                      :index="index"
                      :index2="i"
                      :disabled="true"
                      v-on:changeData="changeContentActionMorning"
                    />
                  </td>
                </tr>
              </tbody>
            </table>

            <div class="title mb-12" style="padding-left: 5px">Buổi chiều</div>
            <table style="width: 100%">
              <thead>
                <tr>
                  <th class="location">Địa điểm</th>
                  <th style="width: 20%">Thời gian</th>
                  <th>Hoạt động</th>
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
                      :disable="true"
                      v-on:returnValue="chooseTourDesAfternoon"
                    />
                  </td>
                  <td>
                    <date-picker
                      v-model="v.Time"
                      type="datetime"
                      placeholder="Chọn thời gian bắt đầu"
                      :editable="false"
                      :disabled="true"
                      :disabled-date="disabledBeforeStartTimeAndAfterEndTime"
                    ></date-picker>
                  </td>
                  <td>
                    <BaseTextArea
                      :hasTitle="false"
                      :msrequire="true"
                      :notNull="true"
                      :isNumber="false"
                      :content="v.Action"
                      :index="index"
                      :index2="i"
                      :disabled="true"
                      v-on:changeData="changeContentActionAfternoon"
                    />
                  </td>
                </tr>
              </tbody>
            </table>

            <div class="title mb-12" style="padding-left: 5px">Buổi tối</div>
            <table style="width: 100%">
              <thead>
                <tr>
                  <th class="location">Địa điểm</th>
                  <th style="width: 20%">Thời gian</th>
                  <th>Hoạt động</th>
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
                      :disable="true"
                      v-on:returnValue="chooseTourDesEvening"
                    />
                  </td>
                  <td>
                    <date-picker
                      v-model="v.Time"
                      type="datetime"
                      placeholder="Chọn thời gian bắt đầu"
                      :editable="false"
                      :disable="true"
                      :disabled-date="disabledBeforeStartTimeAndAfterEndTime"
                    ></date-picker>
                  </td>
                  <td>
                    <BaseTextArea
                      :hasTitle="false"
                      :msrequire="true"
                      :notNull="true"
                      :isNumber="false"
                      :content="v.Action"
                      :index="index"
                      :index2="i"
                      :disable="true"
                      v-on:changeData="changeContentActionEvening"
                    />
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
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
                      :index="index"
                      v-on:changeData="changeAttachPrice"
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
                  <td class="function" @click="deleteAttachPrice(index)">
                    Xóa
                  </td>
                </tr>
              </tbody>
            </table>
            <div class="add-new d-flex" @click="addNewAttachPrice">
              <div>+</div>
              <div>Thêm mới chi phí</div>
            </div>
          </div>
        </div>
        <div class="other-infor d-flex" style="width: 100%">
          <div class="other-infor-item policy w-full">
            <div class="title mb-20">Chính sách hoàn hủy</div>
            <table style="width: 100%">
              <thead>
                <tr>
                  <th>Nội dung</th>
                  <th style="width: 50px"></th>
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
                      :index="index"
                      v-on:changeData="changePolicy"
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
          <div class="title mb-20">Trách nhiệm của hai bên</div>
            <table style="width: 100%">
              <thead>
                <tr>
                  <th>Nội dung</th>
                  <th style="width: 50px"></th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(v, index) in listTutorial" v-bind:key="index">
                  <td>
                    <BaseTextArea
                      :clas="'w-full m-r-20'"
                      :hasTitle="false"
                      :msrequire="false"
                      :notNull="false"
                      :isNumber="false"
                      :content="v.Content"
                      :index="index"
                      v-on:changeData="changeTutorial"
                    />
                  </td>
                  <td class="function" @click="deleteTutorial(index)">Xóa</td>
                </tr>
              </tbody>
            </table>
            <div class="add-new d-flex" @click="addNewTutorial">
              <div>+</div>
              <div>Thêm mới nội dung</div>
            </div>
        </div>
      </div>

      <div class="action d-flex">
        <div class="flex-1"></div>
        <div class="btn" @click="closeForm">Hủy</div>
        <div v-if="oTourDetail.Status != 1" class="btn btn-save" @click="saveData">Cập nhật</div>
        <div v-if="oTourDetail.Status != 1" class="btn btn-save" @click="confirmTour">Xác nhận tour</div>
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
      v-on:confirmAction3="
        () => {
          this.showPopUp = false;
        }
      "
    />

    <div id="toast"></div>
    <BaseLoad :load="showLoad"/>
  </div>
</template>

<script>
import BaseAutoComplete from "../base/BaseAutoComplete.vue";
import DatePicker from "vue2-datepicker";
import "vue2-datepicker/index.css";
import BaseInput from "../base/BaseInput.vue";
import BasePopUp from "../base/BasePopUp.vue";
import BaseLoad from "../base/BaseLoad.vue";
import ProvinceAPI from "../../js/api/province";
import DestinationAPI from "../../js/api/destinationapi";
import BaseTextArea from "../base/BaseTextArea.vue";
import TourAPI from "../../js/api/tourapi";
// import UserAPI from "../../js/api/tourapi";
export default {
  components: {
    BaseAutoComplete,
    DatePicker,
    BaseInput,
    BasePopUp,
    BaseTextArea,
    BaseLoad,
  },
  props: {
    oTour: Object,
    mode : Number,
    oData : Object,
    TitleTour: String
  },
  data() {
    return {
      oTourDetail: this.oTour,
      lstProvince: [],
      dataProvinceField: { value: "ProvinceName" },
      lstDestination: [],
      dataFieldDestination: { value: "Name" },
      lstSelectDestination: [],

      showPopUp: false,
      type: "error",
      message: null,
      titleP: null,
      action1: "Hủy",
      action2: "Đóng",
      action3: "Lưu",
      optionPopUp: [false, false],

      listTimeLine: [],
      listAttachPrice: [],
      listPolicy: [],
      listTutorial: [],

      showLoad: false,
    };
  },
  watch: {
    oTour: function () {
      this.oTourDetail = this.oTour;
    },
  },
  async created() {
    await ProvinceAPI.getAll().then((res) => {
      this.lstProvince = res.data;
    });

    if(this.mode == 2){
      this.bindingData(this.oData)
    }
  },
  methods: {
    closeForm() {
      this.$emit("closeForm");
    },

    async bindingData(data){
      this.showLoad = true
      await this.chooseDestination(data.Master.ProvinceDestinationName)

      data.Destination.forEach(e=>{
        this.lstSelectDestination.push({
          RefID: e.RefID,
          Name: e.Name,
          Address: e.Address,
          AdultPrice: e.TicketPrice.Adult.toString()
          .replace(/\D/g, "")
          .replace(/\B(?=(\d{3})+(?!\d))/g, "."),
          ChildPrice: e.TicketPrice.Child.toString()
          .replace(/\D/g, "")
          .replace(/\B(?=(\d{3})+(?!\d))/g, "."),
          BabyPrice: e.TicketPrice.Baby.toString()
          .replace(/\D/g, "")
          .replace(/\B(?=(\d{3})+(?!\d))/g, "."),
        });
      })

      this.listTimeLine = [];
      this.listAttachPrice = [];
      this.listPolicy = [];
      this.listTutorial = [];

      this.listTimeLine = data.Schedule
      this.listAttachPrice = data.AttachOption
      this.listPolicy = data.RefundPolicy
      this.listTutorial = data.Tutorial
      
      this.calculateTotalAmount()
      this.showLoad = false
    },

    disabledBeforeStartTimeAndAfterEndTime(date){
      var startDate = new Date(this.oTourDetail.StartTime)
      var endDate = new Date(this.oTourDetail.EndTime);
      endDate.setHours(23, 59, 59, 0);
      return date < startDate || date > endDate;
    },

    chooseStartPoint(value) {
      var startPoint = this.lstProvince.filter((x) => x.ProvinceName == value);
      if (startPoint.length == 1) {
        this.oTourDetail.StartPoint = startPoint[0].ProvinceName;
        this.oTourDetail.StartPointID = startPoint[0].ProvinceID;
      }
    },

    async chooseDestination(value) {
      this.lstDestination = [];
      this.lstSelectDestination = [];
      this.listTimeLine.forEach((e) => {
        e.Morning = [];
        e.Afternoon = [];
        e.Evening = [];
      });
      var departure = this.lstProvince.filter((x) => x.ProvinceName == value);
      if (departure.length == 1) {
        this.oTourDetail.Departure = departure[0].ProvinceName;
        this.oTourDetail.DepartureID = departure[0].ProvinceID;
        await DestinationAPI.getDesInProvince(
          this.oTourDetail.DepartureID
        ).then((res) => {
          this.lstDestination = res.data;
        });
      }
      this.calculateTotalAmount();
    },

    addNewDestination() {
      if (this.lstSelectDestination.length < this.lstDestination.length) {
        var lstSel = this.lstSelectDestination;
        this.lstSelectDestination = [];
        lstSel.push({
          RefID: "",
          Name: "",
          Address: "",
          AdultPrice: 0,
          ChildPrice: 0,
          BabyPrice: 0,
        });
        this.lstSelectDestination = lstSel;
      }
    },

    changeNumberAdult(value) {
      this.oTourDetail.NumberAdult = value.toString().replaceAll(".", "");
      this.calculateTotalAmount();
    },

    changeNumberChild(value) {
      this.oTourDetail.NumberChild = value.toString().replaceAll(".", "");
      this.calculateTotalAmount();
    },

    changeNumberBaby(value) {
      this.oTourDetail.NumberBaby = value.toString().replaceAll(".", "");
      this.calculateTotalAmount();
    },

    chooseTourDestination(value, index) {
      var des = this.lstDestination.filter((x) => x.Name == value);
      if (des.length > 0) {
        var tikcet = des[0].TicketPrice;
        tikcet = JSON.parse(tikcet);
        this.lstSelectDestination[index].RefID = des[0].RefID;
        this.lstSelectDestination[index].Name = des[0].Name;
        this.lstSelectDestination[index].AdultPrice = tikcet.Adult.toString()
          .replace(/\D/g, "")
          .replace(/\B(?=(\d{3})+(?!\d))/g, ".");
        this.lstSelectDestination[index].ChildPrice = tikcet.Child.toString()
          .replace(/\D/g, "")
          .replace(/\B(?=(\d{3})+(?!\d))/g, ".");
        this.lstSelectDestination[index].BabyPrice = tikcet.Baby.toString()
          .replace(/\D/g, "")
          .replace(/\B(?=(\d{3})+(?!\d))/g, ".");

        this.lstSelectDestination[index].Address = des[0].Place;
        this.calculateTotalAmount();
      }
    },

    calculateTotalAmount() {
      var ticketAdult = 0;
      var ticketChild = 0;
      var ticketBaby = 0;

      for (var i = 0; i < this.lstSelectDestination.length; i++) {
        var item = this.lstSelectDestination[i];
        ticketAdult =
          ticketAdult + Number.parseInt(item.AdultPrice.replaceAll(".", ""));
        ticketChild =
          ticketChild + Number.parseInt(item.ChildPrice.replaceAll(".", ""));
        ticketBaby =
          ticketBaby + Number.parseInt(item.BabyPrice.replaceAll(".", ""));
      }

      var totalAttachPrice = 0;
      for (var j = 0; j < this.listAttachPrice.length; j++) {
        totalAttachPrice =
          totalAttachPrice + Number.parseInt(this.listAttachPrice[j].Price.toString().replaceAll(".", ""));
      }

      var totalAmount =
        ticketAdult * Number.parseInt(this.oTourDetail.NumberAdult.toString().replaceAll(".", "")) +
        ticketChild * Number.parseInt(this.oTourDetail.NumberChild.toString().replaceAll(".", "")) +
        ticketBaby * Number.parseInt(this.oTourDetail.NumberBaby.toString().replaceAll(".", "")) +
        totalAttachPrice;

      this.oTourDetail.TotalAmount = totalAmount
        .toString()
        .replace(/\D/g, "")
        .replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    },

    removeTourDestination(index) {
      var refID = this.lstSelectDestination[index].RefID;
      var use = false;
      for (var i = 0; i < this.listTimeLine.length; i++) {
        var item = this.listTimeLine[i];
        for (var k = 0; k < item.Morning.length; k++) {
          if (item.Morning[k].RefID == refID) {
            use = true;
          }
        }

        for (k = 0; k < item.Afternoon.length; k++) {
          if (item.Afternoon[k].RefID == refID) {
            use = true;
          }
        }

        for (k = 0; k < item.Evening.length; k++) {
          if (item.Evening[k].RefID == refID) {
            use = true;
          }
        }
      }

      if (use) {
        this.titleP = "Cảnh báo";
        this.message = "Địa điểm đã phát sinh quan hệ. Không thể xóa";
        this.showPopUp = true;
      } else {
        this.titleP = "";
        this.message = "";
        this.lstSelectDestination.splice(index, 1);
        this.calculateTotalAmount();
      }
    },

    chooseStartTime() {
      var input = document.getElementById("startTime").querySelector("input");
      var inputT = document.getElementById("endTime").querySelector("input");
      if (this.oTourDetail.StartTime > this.oTourDetail.EndTime) {
        this.message = "Ngày bắt đầu phải nhỏ hơn ngày kết thúc";
        this.titleP = "Thời gian không hợp lệ";
        input.classList.add("error");
        this.showPopUp = true;
      } else {
        this.message = "";
        this.titleP = "";
        input.classList.remove("error");
        inputT.classList.remove("error");
        if (this.oTourDetail.StartTime && this.oTourDetail.EndTime) {
          var difference =
            this.oTourDetail.EndTime.getTime() -
            this.oTourDetail.StartTime.getTime();
          var days = Math.ceil(difference / (1000 * 3600 * 24));
          this.oTourDetail.TotalDay = days;
          this.initListTimeLine();
        } else if (!this.oTourDetail.StartTime && !this.oTourDetail.EndTime) {
          this.listTimeLine = [];
        }
      }
    },

    chooseEndTime() {
      var input = document.getElementById("endTime").querySelector("input");
      var inputT = document.getElementById("startTime").querySelector("input");
      if (this.oTourDetail.StartTime > this.oTourDetail.EndTime) {
        this.message = "Ngày bắt đầu phải nhỏ hơn ngày kết thúc";
        this.titleP = "Thời gian không hợp lệ";
        input.classList.add("error");
        this.showPopUp = true;
      } else {
        this.message = "";
        this.titleP = "";
        input.classList.remove("error");
        inputT.classList.remove("error");

        if (this.oTourDetail.StartTime && this.oTourDetail.EndTime) {
          var difference =
            this.oTourDetail.EndTime.getTime() -
            this.oTourDetail.StartTime.getTime();
          var days = Math.ceil(difference / (1000 * 3600 * 24));
          this.oTourDetail.TotalDay = days;
          this.initListTimeLine();
        } else if (!this.oTourDetail.StartTime && !this.oTourDetail.EndTime) {
          this.listTimeLine = [];
        }
      }
    },

    initListTimeLine() {
      var nDay = this.oTourDetail.TotalDay;
      if (nDay > this.listTimeLine.length) {
        while (this.listTimeLine.length != nDay) {
          this.listTimeLine.push({
            Morning: [],
            Afternoon: [],
            Evening: [],
          });
        }
      } else {
        while (this.listTimeLine.length != nDay) {
          this.listTimeLine.splice(this.listTimeLine.length - 1, 1);
        }
      }
    },

    addNewActionMorning(index) {
      this.listTimeLine[index].Morning.push({
        Name: "",
        RefID: "",
        Time: null,
        Action: "",
      });
    },

    deleteActionMorning(index, i) {
      this.listTimeLine[index].Morning.splice(i, 1);
    },

    addNewActionAfternoon(index) {
      this.listTimeLine[index].Afternoon.push({
        Name: "",
        RefID: "",
        Time: null,
        Action: "",
      });
    },

    deleteActionAfternoon(index, i) {
      this.listTimeLine[index].Afternoon.splice(i, 1);
    },

    addNewActionEvening(index) {
      this.listTimeLine[index].Evening.push({
        Name: "",
        RefID: "",
        Time: null,
        Action: "",
      });
    },

    deleteActionEvening(index, i) {
      this.listTimeLine[index].Evening.splice(i, 1);
    },

    chooseTourDesMorning(value, index, i) {
      var des = this.lstSelectDestination.filter((x) => x.Name == value);
      if (des.length == 1) {
        this.listTimeLine[index].Morning[i].Name = value;
        this.listTimeLine[index].Morning[i].RefID = des[0].RefID;
      }
    },

    chooseTourDesAfternoon(value, index, i) {
      var des = this.lstSelectDestination.filter((x) => x.Name == value);
      if (des.length == 1) {
        this.listTimeLine[index].Afternoon[i].Name = value;
        this.listTimeLine[index].Afternoon[i].RefID = des[0].RefID;
      }
    },

    chooseTourDesEvening(value, index, i) {
      var des = this.lstSelectDestination.filter((x) => x.Name == value);
      if (des.length == 1) {
        this.listTimeLine[index].Evening[i].Name = value;
        this.listTimeLine[index].Evening[i].RefID = des[0].RefID;
      }
    },

    changeContentActionMorning(value, index, i) {
      this.listTimeLine[index].Morning[i].Action = value;
    },

    changeContentActionAfternoon(value, index, i) {
      this.listTimeLine[index].Afternoon[i].Action = value;
    },

    changeContentActionEvening(value, index, i) {
      this.listTimeLine[index].Evening[i].Action = value;
    },

    addNewAttachPrice() {
      this.listAttachPrice.push({
        Name: "",
        Price: 0,
      });
    },

    deleteAttachPrice(index) {
      this.listAttachPrice.splice(index, 1);
      this.calculateTotalAmount();
    },

    changePriceAttach(value, index) {
      this.listAttachPrice[index].Price = value;
      this.calculateTotalAmount();
    },
    changeAttachPrice(value, index){
      this.listAttachPrice[index].Name = value;
    },

    addNewPolicy() {
      this.listPolicy.push({ Content: "" });
    },

    deletePolicy(indnex) {
      this.listPolicy.splice(indnex, 1);
    },

    changePolicy(value, index){
      this.listPolicy[index].Content = value;
    },

    addNewTutorial() {
      this.listTutorial.push({ Content: "" });
    },

    deleteTutorial(indnex) {
      this.listTutorial.splice(indnex, 1);
    },

    changeTutorial(value, index){
      this.listTutorial[index].Content = value;
    },

    async saveData() {
        if(this.validataBeforeSave()){
          var data = {
            "Master": {},
            "Contract": {},
            "Destination" : [],
            "Schedule" : [],
            "CustomerRequest" : [],
            "AttachOption" : [],
            "RefundPolicy" : [],
            "Tutorial" : [],
            "Info": {
              "UserID" : null,
              "Sample" : this.oTourDetail.Sample,
              "Status" : this.oTourDetail.Status,
              "IsPayment" : this.oTourDetail.IsPayment,
              "RefID": this.oTourDetail.TourID,
              "Mode": this.mode
            },
          }

          data.Master = await this.bindingDataMaster(data.Master);
          data.Contract = this.bindingDataContract(data.Contract);
          data.Destination = this.bindingDataDestination(data.Destination);
          data.Schedule = this.bindingDataSchedule(data.Schedule);
          data.AttachOption = this.bindingDataAttachOption(data.AttachOption);
          data.RefundPolicy = this.bindingDataRefundPolicy(data.RefundPolicy);
          data.Tutorial = this.bindingDataTutorial(data.Tutorial);
          data = JSON.stringify(data);
          this.showLoad = true
          await TourAPI.update(data)
          .then(res=>{
            if(res.data.error == "DupliacteName"){
                this.toast({
                    title: "Tên tour đã tồn tại",
                    type: "error",
                    duration: 3000,
                });
            }
            else{
                this.closeForm();
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
        }
        else{
            this.showPopUp = true;
            this.titleP = "Cảnh báo";
        }
    },

    async bindingDataMaster(data){
      if(this.mode == 1){
        await TourAPI.getNewCode()
        .then(res=>{
          data.ContractCode = res.data;
          data.CreatedTime = new Date();
          data.CreatedTime = new Date(data.CreatedTime.setTime(data.CreatedTime.getTime() + (7*60*60*1000)))
        })
      }
      else{
        data.ContractCode = this.oTourDetail.ContractCode;
        data.CreatedTime = this.oTourDetail.CreatedTime;
      }

      // await UserAPI.getUserInfo()
      // .then(res=>{
      //   data.CustomerName = res.data.Name;
      //   data.CustomerIdentity = res.data.IdentityNumber;
      //   data.CustomerPhone = res.data.PhoneNumber;
      //   data.CustomerAddress = res.data.Address;
      // })

      data.CustomerName = "";
      data.CustomerIdentity = "";
      data.CustomerPhone = "";
      data.CustomerAddress = "";

      data.TotalCost = this.oTourDetail.TotalAmount.replaceAll(".", "");
      data.TourName = this.oTourDetail.Name;
      data.ProvinceStartName = this.oTourDetail.StartPoint;
      data.ProvinceDestinationName = this.oTourDetail.Departure;
      data.ProvinceStartID = this.lstProvince.filter(e=>e.ProvinceName == this.oTourDetail.StartPoint)[0].ProvinceID;
      data.ProvinceDestinationID = this.lstProvince.filter(e=>e.ProvinceName == this.oTourDetail.Departure)[0].ProvinceID;
      data.PickupAdress = this.oTourDetail.PickUpPoint;
      var pickupTime = this.oTourDetail.PickUpTime.setTime(this.oTourDetail.PickUpTime.getTime() + (7*60*60*1000))
      data.PickupTime = new Date(pickupTime);
      
      await TourAPI.sayMoney(data.TotalCost)
      .then(res=>{
        data.TotalCostInWord = res.data;
      })

      return data;
    },

    bindingDataContract(data){
      data.NumberAdult = this.oTourDetail.NumberAdult;
      data.NumberChild = this.oTourDetail.NumberChild;
      data.NumberBaby = this.oTourDetail.NumberBaby;
      data.StartTime = new Date(this.oTourDetail.StartTime.setTime(this.oTourDetail.StartTime.getTime() + (7*60*60*1000)))
      data.EndTime = new Date(this.oTourDetail.EndTime.setTime(this.oTourDetail.EndTime.getTime() + (7*60*60*1000)))
      var diff =(data.EndTime.getTime() - data.StartTime.getTime()) / 1000;
      diff /= (60 * 60);
      data.TotalHour = Math.abs(Math.round(diff));
      
      return data;
    },

    bindingDataDestination(data){
      this.lstSelectDestination.forEach(e=>{
        data.push({
          "Name" : e.Name,
          "Address" : e.Address,
          "TicketPrice" : {
            "Adult" : e.AdultPrice.replaceAll(".", ""),
            "Child" : e.ChildPrice.replaceAll(".", ""),
            "Baby" : e.BabyPrice.replaceAll(".", ""),
          },
          "DestinationID" : e.RefID
        })
      })

      return data;
    },

    bindingDataSchedule(data){
      for(var i=0; i<this.listTimeLine.length; i++){
        data.push({
          "Morning" : [],
          "Afternoon" : [],
          "Evening" : [],
        })
        this.listTimeLine[i].Morning.forEach(e=>{
          var time = new Date(e.Time.setTime(e.Time.getTime() + (7*60*60*1000)));
          data[i].Morning.push({
            "DestinationID" : e.RefID,
            "Destination" : e.Name,
            "StartTime" : time,
            "Action" : e.Action
          })
        })

        this.listTimeLine[i].Afternoon.forEach(e=>{
          data[i].Afternoon.push({
            "DestinationID" : e.RefID,
            "Destination" : e.Name,
            "StartTime" : new Date(e.Time.setTime(e.Time.getTime() + (7*60*60*1000))),
            "Action" : e.Action
          })
        })

        this.listTimeLine[i].Evening.forEach(e=>{
          data[i].Evening.push({
            "DestinationID" : e.RefID,
            "Destination" : e.Name,
            "StartTime" : new Date(e.Time.setTime(e.Time.getTime() + (7*60*60*1000))),
            "Action" : e.Action
          })
        })
      }

      return data;
    },

    bindingDataAttachOption(data){
      this.listAttachPrice.forEach(e=>{
        data.push({
          "Content" : e.Name,
          "Cost" : e.Price
        })
      })

      return data;
    },

    bindingDataRefundPolicy(data){
      this.listPolicy.forEach(e=>{
        data.push({
          "Content" : e.Content
        })
      })
      return data
    },

    bindingDataTutorial(data){
      this.listTutorial.forEach(e=>{
        data.push({
          "Content" : e.Content
        })
      })
      return data
    },

    validataBeforeSave() {
      var input = document
        .getElementById("tourTemplateGeneral")
        .querySelectorAll("input");

      input.forEach((e) => {
        if (e.getAttribute("notNull")) {
          if (!e.value) {
            this.message = "Tồn tại trường bắt buộc nhập đang bỏ trống trên phần thông tin chung";
            return false;
          }
        }
        if (e.classList.contains("error")) {
          this.message = "Tồn tại trường nhập liệu có giá trị không hợp lệ trên phần thông tin chung";
          return false;
        }
      });

      var autocomplete = document.querySelectorAll(
        "#tourTemplateGeneral .main-autocomplete"
      );
      autocomplete.forEach((e) => {
        if (e.classList.contains("error")) {
          this.message = "Tồn tại trường nhập liệu có giá trị không hợp lệ trên phần thông tin chung";
          return false;
        }
        if (e.getAttribute("notNull")) {
          if (!e.querySelector("input").value) {
            this.message = "Tồn tại trường bắt buộc nhập đang bỏ trống trên phần thông tin chung";
            return false;
          }
        }
      });

      if (
        !this.oTourDetail.PickUpTime ||
        !this.oTourDetail.StartTime ||
        !this.oTourDetail.EndTime
      ) {
        this.message = "Thời gian bắt buộc nhập đang bỏ trống";
        return false;
      }

      if (this.lstSelectDestination.length == 0) {
        this.message = "Bạn chưa chọn điểm tham quan";
        return false;
      }

      for (var i = 0; i < this.listTimeLine.length; i++) {
        var item = this.listTimeLine[i];
        item.Morning.forEach((x) => {
          if (!x.Time) {
            this.message =
              "Thời gian bắt đầu sự kiện trong lịch trình đang bỏ trống";
            return false;
          }
          if (!x.Name) {
            this.message =
              "Địa điểm tổ chức sự kiện trong lịch trình đang bỏ trống";
            return false;
          }
          if (!x.Action) {
            this.message =
              "Hoạt động trong sự kiện trong lịch trình đang bỏ trống";
            return false;
          }
        });
      }

      for (i = 0; i < this.listAttachPrice.length; i++) {
        if (!this.listAttachPrice[i].Name) {
          this.message = "Tồn tại chi phí đi kèm chưa có nội dung";
          return false;
        }
        if (!this.listAttachPrice[i].Price) {
          this.message = "Tồn tại chi phí đi kèm chưa có chi phí";
          return false;
        }
      }

      for (i = 0; i < this.listPolicy.length; i++) {
        if (!this.listPolicy[i].Content) {
          this.message = "Tồn tại chính sách hoàn hủy chưa có nội dung";
          return false;
        }
      }

      for (i = 0; i < this.listTutorial.length; i++) {
        if (!this.listTutorial[i].Content) {
          this.message = "Tồn tại thông tin trách nhiệm hai bên chưa có nội dung";
          return false;
        }
      }

      return true;
    },

    async confirmTour(){
        var id = this.oTourDetail.TourID
        this.showLoad = true
        await TourAPI.confirmTour(id)
        .then(res=>{
            if(res.data.error == "TourNotExist"){
                this.toast({
                    title: "Tour không tồn tại",
                    type: "error",
                    duration: 3000,
                });
            }
            else{
                this.closeForm()
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
     * Khởi tạo toast
     */
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
  },
};
</script>

<style>
@import url(../../css/form/createform.css);
.form-container input {
  border-radius: 5px;
}
</style>