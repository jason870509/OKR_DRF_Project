<script setup></script>
<template>
  <!-- Breadcrumb -->
  <section id="bc" class="mt-3">
    <div class="container">
      <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
          <li class="breadcrumb-item">
            <router-link to="/"
              ><font-awesome-icon icon="fa-solid fa-house-chimney" size="xs" />
              Home</router-link
            >
          </li>
          <li class="breadcrumb-item active">About</li>
        </ol>
      </nav>
    </div>
  </section>

  <section class="container">
    <div class="img-container">
      <img src="/img/about.jpg" alt="about-image" class="img-about" />
      <div class="img-text">
        <h1>Where there's a will, there's a way</h1>
        <h2>Let's do this together! Many hands make light work.</h2>
      </div>
    </div>

    <div class="text-container">
      <div class="text-what-for">
        <h1 class="">What's the Website For?</h1>
        <p class="about-desc">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus quae
          dolor, optio voluptatibus magnam iure esse tempora beatae. A suscipit
          eos. Animi quibusdam cum omnis officiis voluptatum quo ea eveniet?
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus quae
          dolor, optio voluptatibus magnam iure esse tempora beatae, a suscipit
          eos. Animi quibusdam cum omnis officiis
        </p>
        <p class="about-desc">
          voluptatum quo ea eveniet? Lorem ipsum dolor sit amet consectetur
          adipisicing elit. Ducimus quae dolor, optio voluptatibus magnam iure
          esse tempora beatae, a suscipit eos. Animi quibusdam cum omnis
          officiis voluptatum quo ea eveniet?
        </p>
      </div>
      <div class="text-use-this">
        <h1 class="">Who can Use This?</h1>
        <p class="about-desc">
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Ducimus quae
          dolor, optio voluptatibus magnam iure esse tempora beatae, a suscipit
          eos. Animi quibusdam cum omnis officiis voluptatum quo ea eveniet?
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
        </p>
        <p class="about-desc">- Creative Illustrations</p>
        <p class="about-desc">- Dynamic Websites</p>
        <p class="about-desc">- Fast and Handy</p>
        <p class="about-desc">- Mobile Apps</p>

        <div>
          <router-link to="/" class="button btn text-white btn-lg"
            >Dashborad</router-link
          >
        </div>
      </div>
    </div>
  </section>

  <!-- Work -->
  <section id="work" class="bg-dark text-white text-center">
    <h2 class="display-4">Check all of the Report</h2>
    <h4>Everyone can upload and share the report.</h4>
    <hr />
    <router-link to="/listings" class="button btn text-white btn-lg"
      >View Our Reported Listings</router-link
    >
  </section>
</template>

<style scoped>
.img-container {
  position: relative;
  width: 100%;
  height: 300px;
}

.img-about {
  width: 100%;
  height: 300px;
  object-fit: cover;
  filter: grayscale(100%);
}
.img-text {
  position: absolute;
  bottom: 20px;
  left: 20px;
  background-color: rgba(166, 160, 252, 0.8);
  padding: 5px;
  color: white;
}

.text-container {
  display: flex;
  margin-top: 50px;
  justify-content: space-between;
  gap: 100px;
}

.text-what-for {
  display: flex;
  flex-direction: column;
  flex: 1 1 300px;
  gap: 30px;
}

.text-use-this {
  display: flex;
  flex-direction: column;
  flex: 1 1 300px;
  gap: 30px;
}

.about-desc {
  font-size: 18px;
  font-weight: 300;
  text-align: justify;
}

.button {
  background-color: #796fff;
  margin-bottom: 20px;
}

#work {
  padding: 6rem 0;
}
</style>
