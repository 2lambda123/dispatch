<template>
  <dashboard-card
    :loading="loading"
    type="line"
    :options="chartOptions"
    :series="series"
    title="New to Closed Average Time (Hours)"
  />
</template>

<script>
import { forEach, sumBy } from "lodash"
import differenceInHours from "date-fns/differenceInHours"
import parseISO from "date-fns/parseISO"

import DashboardCard from "@/dashboard/DashboardCard.vue"

export default {
  name: "CaseNewClosedAverageTimeCard",

  props: {
    modelValue: {
      type: Object,
      default: function () {
        return {}
      },
    },
    interval: {
      type: String,
      default: function () {
        return "Month"
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

  data() {
    return {}
  },

  computed: {
    series() {
      let series = { name: "New to Closed Average Time (Hours)", data: [] }
      forEach(this.modelValue, function (value) {
        series.data.push(
          Math.round(
            sumBy(value, function (item) {
              let endTime = new Date().toISOString()
              if (item.closed_at) {
                endTime = item.closed_at
              }
              return differenceInHours(parseISO(endTime), parseISO(item.reported_at))
            }) / value.length
          )
        )
      })

      return [series]
    },
    chartOptions() {
      return {
        chart: {
          height: 350,
          type: "line",
          animations: {
            enabled: false,
          },
        },
        xaxis: {
          categories: Object.keys(this.modelValue) || [],
          title: {
            text: this.interval,
          },
        },
        dataLabels: {
          enabled: true,
        },
        stroke: {
          curve: "smooth",
        },
        markers: {
          size: 1,
        },
        yaxis: {
          title: {
            text: "Hours",
          },
        },
        legend: {
          position: "top",
        },
      }
    },
  },
}
</script>
