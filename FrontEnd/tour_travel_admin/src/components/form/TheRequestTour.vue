<template>
  <div class="form-container d-flex">
      <div class="form-background"></div>
      <div class="form-main d-flex flex-column request-form">
          <div class="header">Xác nhận yêu cầu</div>
          <div class="icon-close" @click="closeForm">X</div>
          <div class="form-title d-flex">
              <div class="title">Tour du lich Ha Noi - Ninh Binh, 3N2D</div>
              <div class="flex-1"></div>
              <div class="price">8.000.000đ</div>
          </div>
          <div class="d-flex flex-column content">
            <div class="common-infor d-flex flex-column">
               
                <div class="block first-block d-flex mb-20">
                    <BaseAutoComplete
                    :clas="'w-30 m-r-20'"
                    :hasTitle="true"
                    :title="'Điểm khởi hành'"
                    :notNull="true"
                    :msrequire="true"
                    :placeholder="'Nhập tên tỉnh'"
                    :disable="true"
                    />
                    <div class="m-r-20">
                        <div class="title-input">Thời gian xuất phát&nbsp;&nbsp;<span>*</span></div>
                        <date-picker v-model="startTime" type="date" placeholder="Chọn thời gian bắt đầu" format='DD-MM-YYYY' :disabled="true"></date-picker>
                    </div>
                    <div class="m-r-20">
                        <div class="title-input">Thời gian kết thúc&nbsp;&nbsp;<span>*</span></div>
                        <date-picker v-model="endTime" type="date" placeholder="Chọn thời gian kết thúc" format='DD-MM-YYYY' :disabled="true"></date-picker>
                    </div>
                </div>
                <div class="block second-block d-flex mb-20">
                    <BaseAutoComplete
                    :clas="'w-30 m-r-20'"
                    :hasTitle="true"
                    :title="'Điểm tham quan'"
                    :notNull="true"
                    :msrequire="true"
                    :placeholder="'Nhập tên tỉnh'"
                    :disable="true"
                    />

                    <BaseInput
                    :clas="'w-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Số người lớn'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="true"
                    :disabled="true"
                    />

                    <BaseInput
                    :clas="'w-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Số trẻ em'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="true"
                    :disabled="true"
                    />

                    <BaseInput
                    :clas="'w-20 m-r-20'"
                    :hasTitle="true"
                    :title="'Số em bé'"
                    :msrequire="true"
                    :notNull="true"
                    :isNumber="true"
                    :disabled="true"
                    />
                </div>
            </div>
            <div class="time-line d-flex flex-column">
                <div class="title mb-20">Lịch trình</div>
                <div class="block-time-line morning mb-20">
                    <div class="title mb-12">Buổi sáng</div>
                    <table class="disable">
                        <thead>
                            <tr>
                                <th rowspan="2" class="location">Địa điểm</th>
                                <th colspan="4">Giá vé</th>
                            </tr>
                            <tr>
                                <th>Người lớn</th>
                                <th>Trẻ em</th>
                                <th>Em bé</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <BaseAutoComplete
                                    :disable="true"/>
                                </td>
                                <td></td>
                                <td></td>
                                <td></td>
                            </tr>
                        </tbody>
                    </table>

                </div>
                <div class="block-time-line afternoon mb-20">
                    <div class="title mb-12">Buổi chiều</div>
                    <table class="disable">
                        <thead>
                            <tr>
                                <th rowspan="2" class="location">Địa điểm</th>
                                <th colspan="4">Giá vé</th>
                            </tr>
                            <tr>
                                <th>Người lớn</th>
                                <th>Trẻ em</th>
                                <th>Em bé</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <BaseAutoComplete
                                    :disable="true"/>
                                </td>
                                <td></td>
                                <td></td>
                                <td></td>
                            </tr>
                        </tbody>
                    </table>

                </div>
                <div class="block-time-line evening mb-20">
                    <div class="title mb-12">Buổi tối</div>
                    <table class="disable">
                        <thead>
                            <tr>
                                <th rowspan="2" class="location">Địa điểm</th>
                                <th colspan="4">Giá vé</th>
                            </tr>
                            <tr>
                                <th>Người lớn</th>
                                <th>Trẻ em</th>
                                <th>Em bé</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <BaseAutoComplete
                                    :disable="true"/>
                                </td>
                                <td></td>
                                <td></td>
                                <td></td>
                            </tr>
                        </tbody>
                    </table>

                </div>
            </div>
            <div class="request-customer">
                <div class="title mb-20">Yêu cầu của bên mua</div>
                <table class="disable">
                    <tbody>
                        <tr>
                            <td>
                                <BaseInput
                                :clas="'w-full'"
                                :hasTitle="false"
                                :title="'Số em bé'"
                                :msrequire="false"
                                :notNull="false"
                                :isNumber="false"
                                :disabled="true"
                                />
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="other-infor d-flex">
                <div class="other-infor-item cost">
                    <div class="title mb-20">Chi phí đi kèm</div>
                    <table>
                        <thead>
                            <tr>
                                <th>Loại chi phí</th>
                                <th>Chi phí</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <BaseInput
                                    :clas="'w-full m-r-20'"
                                    :hasTitle="false"
                                    :msrequire="false"
                                    :notNull="false"
                                    :isNumber="false"
                                    />
                                </td>
                                <td>
                                    <BaseInput
                                    :clas="'w-full m-r-20'"
                                    :hasTitle="false"
                                    :msrequire="false"
                                    :notNull="false"
                                    :isNumber="false"
                                    />
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <BaseInput
                                    :clas="'w-full m-r-20'"
                                    :hasTitle="false"
                                    :msrequire="false"
                                    :notNull="false"
                                    :isNumber="false"
                                    />
                                </td>
                                <td>
                                    <BaseInput
                                    :clas="'w-full m-r-20'"
                                    :hasTitle="false"
                                    :msrequire="false"
                                    :notNull="false"
                                    :isNumber="false"
                                    />
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="add-new d-flex">
                        <div>+</div>
                        <div>Thêm mới chi phí</div>
                    </div>
                </div>
                <div class="flex-1"></div>
                <div class="other-infor-item policy">
                    <div class="title mb-20">Chính sách hoàn hủy</div>
                    <table>
                        <thead>
                            <tr>
                                <th>Điều kiện áp dụng</th>
                                <th>Bồi thường</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>
                                    <BaseInput
                                    :clas="'w-full m-r-20'"
                                    :hasTitle="false"
                                    :msrequire="false"
                                    :notNull="false"
                                    :isNumber="false"
                                    />
                                </td>
                                <td>
                                    <BaseInput
                                    :clas="'w-full m-r-20'"
                                    :hasTitle="false"
                                    :msrequire="false"
                                    :notNull="false"
                                    :isNumber="false"
                                    />
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="add-new d-flex">
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
              <div class="btn btn-save" title="Trao đổi với Khách hàng" v-title>Trao đổi với KH</div>
              <div class="btn btn-save">Lưu</div>
              <div class="btn btn-save">Xác nhận</div>
          </div>
      </div>
  </div>
</template>

<script>
import BaseAutoComplete from '../base/BaseAutoComplete.vue'
import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';
import BaseInput from '../base/BaseInput.vue';
export default {
  components: { BaseAutoComplete, DatePicker, BaseInput },
  data(){
      return{
          startTime: null,
          endTime: null,
      }
  },
  methods:{
      closeForm(){
          this.$emit("closeForm");
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