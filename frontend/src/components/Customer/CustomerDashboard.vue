<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6">
        <div class="card customer-card">
          <div class="card-body">
            <h5 class="card-title">Available Services</h5>
            <p class="card-text">Browse and select from available services.</p>
            <router-link to="/services" class="btn btn-info">View Services</router-link>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="card customer-card">
          <div class="card-body">
            <h5 class="card-title">Request a Service</h5>
            <p class="card-text">Submit a request for a specific service.</p>
            <router-link to="/request-service" class="btn btn-primary">Request Now</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CustomerDashboard',
};
</script>

<style scoped>
.customer-card {
  margin-bottom: 20px;
  transition: transform 0.3s;
}

.customer-card:hover {
  transform: translateY(-5px);
}
</style>
