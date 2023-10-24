import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useReportStore = defineStore("reports", () => {
  const data = ref({});

  return { data };
});
