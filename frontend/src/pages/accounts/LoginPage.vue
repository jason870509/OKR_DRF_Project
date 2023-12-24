<script setup>
import useAxios from "../../composables/useAxios";
import { useRouter } from "vue-router";
import { useUserStore } from "../../stores/user";

const router = useRouter();
const axios = useAxios();
const userStore = useUserStore();

const handleLogin = async () => {
  const loginForm = document.getElementById("login-form");
  let formData = new FormData(loginForm);
  let data = Object.fromEntries(formData);

  console.log(data);

  try {
    const response = await axios.post("/api/api/token/", data);

    localStorage.setItem("access", response.data["access"]);
    localStorage.setItem("refresh", response.data["refresh"]);
    userStore.username = data["username"];
    userStore.login = true;
    router.push("/dashboard");
    console.log(userStore.username);
  } catch (err) {}
};
</script>

<template>
  <section id="login" class="py-5">
    <div class="container">
      <div class="row">
        <div class="col-md-6 mx-auto">
          <div class="card">
            <div class="card-header bg-primary text-white">
              <h4>
                <font-awesome-icon icon="fa-solid fa-sign-in-alt" /> Login
              </h4>
            </div>
            <div class="card-body">
              <form id="login-form" @submit.prevent="handleLogin">
                <div class="form-group">
                  <label for="username">Username</label>
                  <input
                    type="text"
                    name="username"
                    class="form-control"
                    required
                  />
                </div>

                <div class="form-group">
                  <label for="password2">Password</label>
                  <input
                    type="password"
                    name="password"
                    class="form-control"
                    required
                  />
                </div>

                <input
                  type="submit"
                  value="Login"
                  class="submit-button btn btn-primary btn-block"
                />
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.submit-button {
  background-color: #796fff;
}
</style>
