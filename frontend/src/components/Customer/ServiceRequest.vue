<template>
  <div class="container">
    <div class="card service-request-card">
      <div class="card-body">
        <h4 class="card-title">Request a Service</h4>
        <form @submit.prevent="requestService">
          <div class="form-group">
            <label for="service">Service</label>
            <select v-model="selectedService" class="form-control" required>
              <option v-for="service in services" :key="service.id" :value="service.id">{{ service.name }}</option>
            </select>
          </div>
          <div class="form-group">
            <label for="date">Preferred Date</label>
            <input type="date" v-model="preferredDate" class="form-control" required>
          </div>
          <button type="submit" class="btn btn-success btn-block">Submit Request</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      services: [], // Fetch services from API
      selectedService: '',
      preferredDate: '',
    };
  },
  methods: {
    requestService() {
      // Make API call to submit request
    }
  },
  created() {
    // Fetch services from API on component load
  }
};
</script>

<style scoped>
.service-request-card {
  margin: 20px auto;
  max-width: 600px;
  padding: 20px;
}
</style>
