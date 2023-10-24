import { createRouter, createWebHistory } from "vue-router";
// import Vue from "vue";
const HomePage = () => import("../pages/HomePage.vue");
const AboutPage = () => import("../pages/AboutPage.vue");
const ListingsPage = () => import("../pages/ListingsPage.vue");
const ReportsPage = () => import("../pages/ReportsPage.vue");
const DashboardPage = () => import("../pages/accounts/DashboardPage.vue");
const RegisterPage = () => import("../pages/accounts/RegisterPage.vue");
const LoginPage = () => import("../pages/accounts/LoginPage.vue");
const SearchPage = () => import("../pages/SearchPage.vue");

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomePage,
      meta: {
        title: "Home",
      },
    },
    {
      path: "/about",
      name: "about",
      component: AboutPage,
      meta: {
        title: "About",
      },
    },
    {
      path: "/listings",
      name: "listings",
      component: ListingsPage,
      meta: {
        title: "Listings",
      },
    },
    {
      path: "/reports",
      name: "reports",
      component: ReportsPage,
      meta: {
        title: "Reports",
      },
    },
    {
      path: "/dashboard",
      name: "dashboard",
      component: DashboardPage,
      meta: {
        title: "Dashboard",
      },
    },
    {
      path: "/register",
      name: "register",
      component: RegisterPage,
      meta: {
        title: "Register",
      },
    },
    {
      path: "/login",
      name: "login",
      component: LoginPage,
      meta: {
        title: "Login",
      },
    },
    {
      path: "/search",
      name: "search",
      component: SearchPage,
      meta: {
        title: "Search",
      },
    },
  ],
});

router.beforeEach((to, from) => {
  console.log(to);
  // Use next tick to handle router history correctly
  // see: https://github.com/vuejs/vue-router/issues/914#issuecomment-384477609
  // Vue.nextTick(() => {
  //   document.title = to.meta.title;
  // });
  document.title = to.meta.title;
});

export default router;
