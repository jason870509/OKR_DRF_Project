import "bootstrap/dist/css/bootstrap.css";

// import "./assets/all.css";
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
  faUserPlus,
  faSignOutAlt,
  faSignInAlt,
  faPhone,
  faEnvelopeOpen,
  faClock,
} from "@fortawesome/free-solid-svg-icons";

import {
  faFacebook,
  faXTwitter,
  faLinkedin,
  faInstagram,
  faPinterest,
  faLeanpub,
} from "@fortawesome/free-brands-svg-icons";

import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";

const app = createApp(App);

/* add icons to the library */
library.add(
  faArrowCircleUp,
  faShareSquare,
  faAddressBook,
  faHouseChimney,
  faUserPlus,
  faSignOutAlt,
  faSignInAlt,
  faPhone,
  faEnvelopeOpen,
  faFacebook,
  faXTwitter,
  faLinkedin,
  faInstagram,
  faPinterest,
  faLeanpub,
  faClock
);

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);

app.use(pinia);
app.use(router);
app.component("font-awesome-icon", FontAwesomeIcon);
app.mount("#app");

import "bootstrap/dist/js/bootstrap.js";
