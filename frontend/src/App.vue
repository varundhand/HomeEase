<template>
  <div id="app">
    <div class="gradient"></div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">Household Services</a>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link class="nav-link" to="/login">Login</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/admin-dashboard">Admin</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/customer-dashboard">Customer</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/professional-dashboard">Professional</router-link>
          </li>
        </ul>
      </div>
    </nav>
    <div class="main"></div>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
body {
  font-family: "Roboto", sans-serif;
  /* background-color: red; */
}

.navbar {
  /* margin-bottom: 20px; */
}
</style>