document.addEventListener("DOMContentLoaded", () => {
    new Chart(document.querySelector("#barChart"), {
      type: "bar",
      data: {
        labels: [
          "Malur",
          "Trichy"
        ],
        datasets: [
        {
          label: 'Rough Handling',
          data: {{factViolation[0]}}
          // borderColor: Utils.CHART_COLORS.red,
          // backgroundColor: Utils.transparentize(Utils.CHART_COLORS.red, 0.5),
        },
        {
          label: 'No Gloves',
          data: {{factViolation[1]}}
          // borderColor: Utils.CHART_COLORS.blue,
          // backgroundColor: Utils.transparentize(Utils.CHART_COLORS.blue, 0.5),
        },
        {
          label: 'Bag Stepping',
          data: {{factViolation[2]}}
          // borderColor: Utils.CHART_COLORS.blue,
          // backgroundColor: Utils.transparentize(Utils.CHART_COLORS.blue, 0.5),
        }
        ]
      },
      options: {
        aspectRatio: 1.45,
        scales: {
          y: {
            beginAtZero: true,
          }
        }
      }
    });
  });