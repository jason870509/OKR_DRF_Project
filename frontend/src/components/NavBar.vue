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
          <a class="nav-link" href="/">
            <i class="fas fa-user-plus"></i> Welcome Jason Dashboard</a
          >
        </li>
        <li class="nav-item mr-3">
          <a
            href="javascript:{document.getElementById('logout').submit()}"
            class="nav-link"
          >
            <i class="fas fa-sign-out-alt"></i> Logout
          </a>
          <form action="#" method="POST" id="logout">
            <input type="hidden" />
          </form>
        </li>
        <li class="nav-item mr-3">
          <a class="nav-link" href="/">
            <i class="fas fa-user-plus"></i> Register</a
          >
        </li>
        <li class="nav-item mr-3">
          <a class="nav-link" href="/">
            <i class="fas fa-sign-in-alt"></i>
            Login</a
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
}
</style>
