import { ref, computed } from "vue";
import { defineStore } from "pinia";

export const useUserStore = defineStore(
  "user",
  () => {
    const username = ref("");
    const login = ref(false);

    return { username, login };
  },
  {
    persist: {
      key: "user",
    },
  }
);
