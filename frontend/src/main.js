import "bootstrap/dist/css/bootstrap.css";

import "./assets/all.css";
import "./assets/bootstrap.css";
import "./assets/style.css";
import "./assets/lightbox.min.css";
import "./assets/main.css";

/* import the fontawesome core */
import { library } from "@fortawesome/fontawesome-svg-core";

/* import font awesome icon component */
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

/* import specific icons */
import {
  faArrowCircleUp,
  faShareSquare,
  faAddressBook,
  faHouseChimney,
} from "@fortawesome/free-solid-svg-icons";

import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

const app = createApp(App);

/* add icons to the library */
library.add(faArrowCircleUp, faShareSquare, faAddressBook, faHouseChimney);

app.use(createPinia());
app.use(router);
app.component("font-awesome-icon", FontAwesomeIcon);
app.mount("#app");

import "bootstrap/dist/js/bootstrap.js";
