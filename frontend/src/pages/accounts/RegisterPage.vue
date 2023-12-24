<script setup>
import useAxios from "../../composables/useAxios";
import { useRouter } from "vue-router";

const router = useRouter();
const axios = useAxios();

const handleRegister = async () => {
  const registerForm = document.getElementById("register-form");
  let formData = new FormData(registerForm);
  let data = Object.fromEntries(formData);

  try {
    await axios.post("/api/user/create/", data);

    alert("Sign up seccessful.");
    router.push("/login");
  } catch (err) {
    console.log(err);
  }
};
</script>
<template>
  <section id="register" class="py-5">
    <div class="container">
      <div class="row">
        <div class="col-md-6 mx-auto">
          <div class="card">
            <div class="card-header bg-primary text-white">
              <h4>
                <font-awesome-icon icon="fa-solid fa-user-plus" /> Register
              </h4>
            </div>
            <div class="card-body">
              <form id="register-form" @submit.prevent="handleRegister">
                <div class="form-group">
                  <label for="first_name">First Name</label>
                  <input
                    type="text"
                    name="first_name"
                    class="form-control"
                    required
                  />
                </div>
                <div class="form-group">
                  <label for="last_name">Last Name</label>
                  <input
                    type="text"
                    name="last_name"
                    class="form-control"
                    required
                  />
                </div>
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
                  <label for="email">Email</label>
                  <input
                    type="email"
                    name="email"
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
                <div class="form-group">
                  <label for="password">Confirm Password</label>
                  <input
                    type="password"
                    name="password2"
                    class="form-control"
                    required
                  />
                </div>
                <input
                  type="submit"
                  value="Register"
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
