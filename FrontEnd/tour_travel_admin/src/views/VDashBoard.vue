<template>
  <div class="dashboard d-flex flex-column">
    <div class="total d-flex font-bold w-30">
      <div class="d-flex flex-column w-half item">
        <div class="p-b-20">Tổng số</div>
        <div>20</div>
      </div>
      <div class="d-flex flex-column w-half item">
        <div class="p-b-20">Tổng phòng Khách sạn</div>
        <div>1.700</div>
      </div>
    </div>
    <div class="d-flex w-full">
      <div class="chart" id="chart">
      </div>
      <div class="flex-1"></div>
      <div class="tour-rank d-flex flex-column">
        <div class="font-bold">Tour được quan tâm</div>
        <div class="rank d-flex flex-column">
          <div class="item">AAAa</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  components: { },
  data(){
    return{
      chartData:{
        labels:["Jan", "Feb", "Mar", "Apr"],
        datasets:{
          data:[100, 50, 150, 200],
        }
      },
      chartOption:{
        maintainAspectRadio: false,
        responsive: true
      }
    }
  },
  // mounted() {
  //   const plugin = document.createElement("script");
  //   plugin.setAttribute(
  //     "src",
  //     "https://cdn.jsdelivr.net/npm/chart.js"
  //   );
  //   plugin.async = true;
  //   document.head.appendChild(plugin);

  //   const plugin2 = document.createElement("script");
  //   plugin2.setAttribute(
  //     "src",
  //     "../js/chart.js"
  //   );
  //   plugin2.async = true;
  //   document.head.appendChild(plugin2);
  // }
}
</script>

<style>
.dashboard{
  width: 100%;
  height: 100%;
  padding: 50px;
}

.dashboard div{
  font-size: 18px;
}
.dashboard .total{
  height: 100px;
  background-color: #babec5;
}
.dashboard .total .item{
  height: 100%;
  align-items: center;
  justify-content: center;
}
.dashboard .tour-rank{
  width: 300px;
  justify-content: center;
  align-items: center;
}
.dashboard .tour-rank .rank{
  width: 100%;
  height: 300px;
  overflow-y: auto;
  margin-top: 20px;
  background-color: #babec5;
  padding: 10px;
}
.dashboard .tour-rank .rank .item{
  padding: 10px 20px;
}
.dashboard .tour-rank .rank .item:hover{
  background-color: #fff;
  cursor: pointer;
}
</style>