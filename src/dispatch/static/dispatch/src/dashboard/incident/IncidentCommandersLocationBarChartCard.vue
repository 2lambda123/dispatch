<template>
  <dashboard-card
    :loading="loading"
    type="bar"
    :options="chartOptions"
    :series="series"
    title="Incident Commanders Location"
  />
</template>

<script>
import { forEach } from "lodash"
import DashboardUtils from "@/dashboard/utils"
import DashboardCard from "@/dashboard/DashboardCard.vue"

export default {
  name: "IncidentCommandersLocationBarChartCard",

  props: {
    modelValue: {
      type: Object,
      default: function () {
        return {}
      },
    },
    loading: {
      type: [String, Boolean],
      default: function () {
        return false
      },
    },
  },

  components: {
    DashboardCard,
  },

  computed: {
    chartOptions() {
      return {
        chart: {
          type: "bar",
          height: 350,
          stacked: true,
          animations: {
            enabled: false,
          },
          events: {
            dataPointSelection: (event, chartContext, config) => {
              var data = config.w.config.series[config.seriesIndex].data[config.dataPointIndex]
              this.$emit("detailsSelected", data.items)
            },
          },
        },
        responsive: [
          {
            options: {
              legend: {
                position: "left",
              },
            },
          },
        ],
        xaxis: {
          categories: this.categoryData || [],
          title: {
            text: "Month",
          },
        },
        fill: {
          opacity: 1,
        },
        legend: {
          position: "right",
        },
      }
    },
    series() {
      let allLocations = []
      forEach(this.modelValue, function (value) {
        forEach(value, function (value) {
          allLocations.push(value.commanders_location)
        })
      })
      let series = DashboardUtils.createCountedSeriesData(this.modelValue, "commanders_location", [
        ...new Set(allLocations),
      ])
      return series
    },
    categoryData() {
      return Object.keys(this.modelValue)
    },
  },
}
</script>
