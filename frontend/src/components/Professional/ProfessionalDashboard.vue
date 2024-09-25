<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6" v-for="task in tasks" :key="task.id">
        <div class="card professional-card">
          <div class="card-body">
            <h5 class="card-title">{{ task.serviceName }}</h5>
            <p class="card-text">Date: {{ task.date }}</p>
            <p class="card-text">Customer: {{ task.customerName }}</p>
            <button class="btn btn-info btn-block">View Details</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tasks: [
        { id: 1, serviceName: 'Plumbing', date: '2023-09-25', customerName: 'John Doe' },
        { id: 2, serviceName: 'Electrical', date: '2023-09-26', customerName: 'Jane Doe' },
        // Fetch tasks dynamically
      ]
    };
  }
};
</script>

<style scoped>
.professional-card {
  margin-bottom: 20px;
  transition: transform 0.3s;
}

.professional-card:hover {
  transform: translateY(-5px);
}
</style>
