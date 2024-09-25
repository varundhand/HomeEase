<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6">
        <div class="card admin-card">
          <div class="card-body">
            <h5 class="card-title">Manage Services</h5>
            <p class="card-text">Create, edit, or delete services offered.</p>
            <router-link to="/create-service" class="btn btn-primary">Go</router-link>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="card admin-card">
          <div class="card-body">
            <h5 class="card-title">Manage Professionals</h5>
            <p class="card-text">Manage service professionals and their details.</p>
            <router-link to="/manage-professionals" class="btn btn-success">Go</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdminDashboard',
};
</script>

<style scoped>
.admin-card {
  margin-bottom: 20px;
  transition: transform 0.3s;
}

.admin-card:hover {
  transform: translateY(-5px);
}
</style>
