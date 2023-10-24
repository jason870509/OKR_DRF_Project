<script setup></script>
<template>
  <nav class="navbar navbar-expand-lg navbar-dark sticky-top">
    <a href="/"><img src="/img/logo.png" class="logo" alt="" /></a>

    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item mr-3">
          <router-link to="/" class="nav-link">Home</router-link>
        </li>
        <li class="nav-item mr-3">
          <router-link to="/about" class="nav-link">ABOUT</router-link>
        </li>
        <li class="nav-item mr-3">
          <router-link to="/listings" class="nav-link">LISTINGS</router-link>
        </li>
        <li class="nav-item mr-3">
          <router-link to="/reports" class="nav-link">REPORTS</router-link>
        </li>
      </ul>
      <ul class="navbar-nav ml-auto">
        <li class="nav-item mr-3">
          <router-link to="/dashboard" class="nav-link"
            ><font-awesome-icon icon="fa-solid fa-user-plus" /> Welcome Jason
            Dashboard</router-link
          >
        </li>
        <li class="nav-item mr-3">
          <router-link to="/" class="nav-link"
            ><font-awesome-icon icon="fa-solid fa-sign-out-alt" />
            Logout</router-link
          >
        </li>
        <li class="nav-item mr-3">
          <router-link to="/register" class="nav-link"
            ><font-awesome-icon icon="fa-solid fa-user-plus" />
            Register</router-link
          >
        </li>
        <li class="nav-item mr-3">
          <router-link to="/login" class="nav-link"
            ><font-awesome-icon icon="fa-solid fa-sign-in-alt" />
            Login</router-link
          >
        </li>
      </ul>
      <div class="toggle_container" onClick="toggle()">
        <div class="toggle_icon">🌙</div>
        <div class="toggle_icon">🔆</div>
        <div class="ball"></div>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.router-link-exact-active {
  position: relative;
  font-weight: bold;
}

nav {
  background-color: rgb(55, 46, 182);
  text-transform: uppercase;
  box-shadow: 0 0 8px black;
}

.toggle_container {
  width: 42px;
  height: 24px;
  border: 3px solid #d0f0e070;
  border-radius: 30px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 2px;
  position: relative;
  cursor: pointer;
}

.toggle_icon {
  font-size: 12px;
}

.ball {
  width: 15px;
  height: 15px;
  background: #9374e6;
  border-radius: 50%;
  position: absolute;
}
</style>
