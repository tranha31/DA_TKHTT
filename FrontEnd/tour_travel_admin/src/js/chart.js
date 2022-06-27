var chart = document.getElementById("chart");
var config = {
    type: "bar",
    data: {
        labels: ["Jan", "Feb", "Tue", "Apr"],
        datasets: [{
            label: "Số lượng đặt tour",
            data: [200, 150, 250, 300]
        }]
    },
};

console.log("aaaa")

var cookieChart = new Chart(chart, config)