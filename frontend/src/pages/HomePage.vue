<script setup></script>
<template>
  <!-- Alerts -->
  <!-- {% include 'partials/_alerts.html' %} -->

  <!-- Showcase -->
  <section id="" class="py-5">
    <div class="container_main">
      <div class="item">
        <h1 class="title">Contains Reports & Some Idea.</h1>
        <p class="description">
          Welcome.<br />
          Record Whatever you Want.<br />
          Turning Idea into Reality.
        </p>
        <div>
          <router-link to="/listings" class="button btn text-white btn-lg"
            >Search Reports</router-link
          >
        </div>
      </div>
      <div class="item">
        <img src="/img/main.png" class="img" alt="main-image" />
      </div>
    </div>
  </section>

  <section id="info" class="py-5 text-white" style="background-color: #796fff">
    <div class="container">
      <div class="row text-center">
        <div class="col-md-4">
          <font-awesome-icon icon="fa-solid fa-arrow-circle-up" size="4x" />
          <hr />
          <h3>Upload Report</h3>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt,
            debitis nam! Repudiandae, provident iste consequatur hic dignissimos
            ratione ea quae.
          </p>
        </div>
        <div class="col-md-4">
          <font-awesome-icon icon="fa-solid fa-share-square" size="4x" />
          <hr />
          <h3>Share Together</h3>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt,
            debitis nam! Repudiandae, provident iste consequatur hic dignissimos
            ratione ea quae.
          </p>
        </div>
        <div class="col-md-4">
          <font-awesome-icon icon="fa-solid fa-address-book" size="4x" />
          <hr />
          <h3>Work Easy</h3>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Incidunt,
            debitis nam! Repudiandae, provident iste consequatur hic dignissimos
            ratione ea quae.
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.container_main {
  display: flex;
  align-items: center;
  width: 100%;
  padding-right: 15px;
  padding-left: 120px;
  padding-top: 10px;
  margin-right: auto;
  margin-left: auto;
  margin-top: 30px;
  margin-bottom: 60px;
  justify-content: space-between;
}

.title {
  font-size: 60px;
  background: linear-gradient(to bottom, #696be6, #bbb);
  background-clip: border-box;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.button {
  background-color: #796fff;
}
</style>
