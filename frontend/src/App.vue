<script setup>
// import { RouterLink, RouterView } from "vue-router";
import NavBar from "./components/NavBar.vue";
import Footer from "./components/Footer.vue";
</script>

<template>
  <header>
    <NavBar />
  </header>

  <RouterView />
  <Footer />
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
</style>
