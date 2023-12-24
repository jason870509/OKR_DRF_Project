<script setup>
import { onMounted } from "vue";
import { useUserStore } from "./stores/user";
import { useVerify } from "./composables/useVerify";
import useAxios from "./composables/useAxios";
import NavBar from "./components/NavBar.vue";
import Footer from "./components/Footer.vue";

const { verifyAPI } = useVerify();

onMounted(async () => {});
</script>

<template>
  <div class="wrapper">
    <header>
      <NavBar />
    </header>

    <RouterView />
  </div>
  <div>
    <Footer />
  </div>
</template>

<style>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

/* width */
::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  box-shadow: inset 0 0 5px grey;
  border-radius: 10px;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: rgba(181, 119, 248, 0.5);
  border-radius: 10px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #ff53f1;
} /*# sourceMappingURL=style.css.map */

.wrapper {
  flex-grow: 1; /*可佔滿垂直剩餘的空間*/
}
</style>
