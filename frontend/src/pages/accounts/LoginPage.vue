<script setup></script>

<template>
  <section id="login" class="bg-light py-5">
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
              <form action="/" method="POST">
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
