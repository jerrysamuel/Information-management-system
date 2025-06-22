document.addEventListener("DOMContentLoaded", function () {
    // PIE CHART 1
    const categories = JSON.parse("{{ categories|escapejs }}");
    const worthPercentages = JSON.parse("{{ worth_percentages|escapejs }}");
    new ApexCharts(document.getElementById("pie-chart"), {
      series: worthPercentages,
      labels: categories,
      chart: { type: "pie", height: 420, width: "100%" },
      stroke: { colors: ["white"] },
      plotOptions: {
        pie: {
          size: "100%",
          dataLabels: {
            offset: -25,
            formatter: (_, { dataPointIndex }) =>
              worthPercentages[dataPointIndex] + "%",
          },
        },
      },
      legend: { position: "bottom", fontFamily: "Inter, sans-serif" },
      dataLabels: { enabled: true, style: { fontFamily: "Inter, sans-serif" } },
      colors: ["#1C64F2", "#16BDCA", "#9061F9", "#FDBA8C", "#FF5C5C", "#2DCE89", "#FFA500", "#FF5733", "#006400", "#800080"],
    }).render();

    // GENDER DONUT CHART
    const genderLabels = JSON.parse("{{ genders|escapejs }}");
    const genderPercentages = JSON.parse("{{ percentages|escapejs }}");
    if (document.getElementById("gender-chart")) {
      new ApexCharts(document.getElementById("gender-chart"), {
        series: genderPercentages,
        labels: genderLabels,
        chart: { type: "donut", height: 320 },
        plotOptions: { pie: { donut: { size: "70%" } } },
        legend: { position: "bottom" },
      }).render();
    }

    // STAFF PIE CHART
    const labels = JSON.parse("{{ labels|escapejs }}");
    const counts = JSON.parse("{{ counts|escapejs }}");
    if (document.getElementById("staff-chart")) {
      new ApexCharts(document.getElementById("staff-chart"), {
        series: counts,
        labels: labels,
        chart: { type: "pie", height: 320 },
        plotOptions: { pie: { size: "70%" } },
        legend: { position: "bottom" },
      }).render();
    }

    // SALES LINE CHART
    const salesDates = JSON.parse("{{ dates|escapejs }}");
    const unitsSold = JSON.parse("{{ units_sold|escapejs }}");
    if (document.querySelector("#daily-sales-chart")) {
      new ApexCharts(document.querySelector("#daily-sales-chart"), {
        chart: { type: "line", height: 350 },
        series: [{ name: "Units Sold", data: unitsSold }],
        xaxis: { categories: salesDates },
      }).render();
    }

    // LOW RESOURCE AJAX CHECK
    if (window.jQuery) {
      function checkResources() {
        $.get("{% url 'check_resources' %}", function (data) {
          if (data.length > 0) {
            $('#warning-message').html('<p class="font-bold mb-2">You\'re running low on the following resources:</p>');
            const list = $('<ul>').addClass('list-none flex');
            data.forEach((res, i) => list.append(`<li class="inline-block mr-2 font-bold">${i > 0 ? ', ' : ''}${res.name}</li>`));
            $('#warning-message').append(list).show();
          } else {
            $('#warning-message').hide();
          }
        });
      }
      checkResources();
      setInterval(checkResources, 5000);
    }
  });

