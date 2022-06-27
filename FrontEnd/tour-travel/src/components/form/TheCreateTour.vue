<template>
  <div class="form-container d-flex">
      <div class="form-background"></div>
      <div class="form-main d-flex flex-column">
          <div class="header">Chỉnh sửa tour theo nhu cầu của bạn</div>
          <div class="icon-close" @click="closeForm">X</div>
          <div class="form-title d-flex">
              <div class="title">Tour du lich Ha Noi - Ninh Binh, 3N2D</div>
              <div class="flex-1"></div>
              <div class="price">8.000.000đ</div>
          </div>
          <div class="d-flex flex-column" style="overflow: auto">
            <div class="common-infor d-flex flex-column">
              <div class="block first-block d-flex mb-20">
                  <BaseAutoComplete
                  :clas="'w-30 m-r-20'"
                  :hasTitle="true"
                  :title="'Điểm khởi hành'"
                  :notNull="true"
                  :msrequire="true"
                  :placeholder="'Nhập tên tỉnh'"
                  />
                  <div class="m-r-20">
                      <div class="title-input">Thời gian xuất phát&nbsp;&nbsp;<span>*</span></div>
                      <date-picker v-model="startTime" type="date" placeholder="Chọn thời gian bắt đầu" format='DD-MM-YYYY'></date-picker>
                  </div>
                  <div class="m-r-20">
                      <div class="title-input">Thời gian kết thúc&nbsp;&nbsp;<span>*</span></div>
                      <date-picker v-model="endTime" type="date" placeholder="Chọn thời gian kết thúc" format='DD-MM-YYYY'></date-picker>
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
                  />

                  <BaseInput
                  :clas="'w-10 m-r-20'"
                  :hasTitle="true"
                  :title="'Số người lớn'"
                  :msrequire="true"
                  :notNull="true"
                  :isNumber="true"
                  />

                  <BaseInput
                  :clas="'w-10 m-r-20'"
                  :hasTitle="true"
                  :title="'Số trẻ em'"
                  :msrequire="true"
                  :notNull="true"
                  :isNumber="true"
                  />

                  <BaseInput
                  :clas="'w-10 m-r-20'"
                  :hasTitle="true"
                  :title="'Số em bé'"
                  :msrequire="true"
                  :notNull="true"
                  :isNumber="true"
                  />
              </div>
          </div>
          <div class="time-line d-flex flex-column">
              <div class="title mb-20">Lịch trình</div>
              <div class="block-time-line morning mb-20">
                  <div class="title mb-12">Buổi sáng</div>
                  <table>
                      <thead>
                          <tr>
                              <th rowspan="2" class="location">Địa điểm</th>
                              <th colspan="4">Giá vé</th>
                          </tr>
                          <tr>
                              <th>Người lớn</th>
                              <th>Trẻ em</th>
                              <th>Em bé</th>
                              <th></th>
                          </tr>
                      </thead>
                      <tbody>
                          <tr>
                              <td>
                                  <BaseAutoComplete/>
                              </td>
                              <td></td>
                              <td></td>
                              <td></td>
                              <td class="function">Xóa</td>
                          </tr>
                      </tbody>
                  </table>

                  <div class="add-new d-flex">
                      <div>+</div>
                      <div>Thêm điểm tham quan</div>
                  </div>
              </div>
              <div class="block-time-line afternoon mb-20">
                  <div class="title mb-12">Buổi chiều</div>
                  <table>
                      <thead>
                          <tr>
                              <th rowspan="2" class="location">Địa điểm</th>
                              <th colspan="4">Giá vé</th>
                          </tr>
                          <tr>
                              <th>Người lớn</th>
                              <th>Trẻ em</th>
                              <th>Em bé</th>
                              <th></th>
                          </tr>
                      </thead>
                      <tbody>
                          <tr>
                              <td>
                                  <BaseAutoComplete/>
                              </td>
                              <td></td>
                              <td></td>
                              <td></td>
                              <td class="function">Xóa</td>
                          </tr>
                      </tbody>
                  </table>

                  <div class="add-new d-flex">
                      <div>+</div>
                      <div>Thêm điểm tham quan</div>
                  </div>
              </div>
              <div class="block-time-line evening mb-20">
                  <div class="title mb-12">Buổi tối</div>
                  <table>
                      <thead>
                          <tr>
                              <th rowspan="2" class="location">Địa điểm</th>
                              <th colspan="4">Giá vé</th>
                          </tr>
                          <tr>
                              <th>Người lớn</th>
                              <th>Trẻ em</th>
                              <th>Em bé</th>
                              <th></th>
                          </tr>
                      </thead>
                      <tbody>
                          <tr>
                              <td>
                                  <BaseAutoComplete/>
                              </td>
                              <td></td>
                              <td></td>
                              <td></td>
                              <td class="function">Xóa</td>
                          </tr>
                      </tbody>
                  </table>

                  <div class="add-new d-flex">
                      <div>+</div>
                      <div>Thêm điểm tham quan</div>
                  </div>
              </div>
          </div>
          <div class="request-customer">
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
                              <td>Di chuyển</td>
                              <td>500.000đ</td>
                          </tr>
                          <tr>
                              <td>Hướng dẫn viên</td>
                              <td>1.500.000đ</td>
                          </tr>
                      </tbody>
                  </table>
                  <div><span style="color:red">*</span>Liên hệ với admin qua kênh chat để điều chỉnh</div>
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
                          
                      </tbody>
                  </table>
                  <div><span style="color:red">*</span>Liên hệ với admin qua kênh chat để điều chỉnh</div>
              </div>
          </div>
          </div>
          
          <div class="action d-flex">
              <div class="flex-1"></div>
              <div class="btn" @click="closeForm">Hủy</div>
              <div class="btn btn-save">Gửi yêu cầu</div>
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
</style>