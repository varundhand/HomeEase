import { createApp } from 'vue';
import App from './App.vue';
import { createRouter, createWebHistory } from 'vue-router';
import Login from './components/Auth/Login.vue';
import AdminDashboard from './components/Admin/AdminDashboard.vue';
import CustomerDashboard from './components/Customer/CustomerDashboard.vue';
import ProfessionalDashboard from './components/Professional/ProfessionalDashboard.vue';
import ServiceRequest from './components/Customer/ServiceRequest.vue';

// Styles
import './assets/global.css'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle.js';



// Define routes
const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  { path: '/admin-dashboard', component: AdminDashboard },
  { path: '/customer-dashboard', component: CustomerDashboard },
  { path: '/professional-dashboard', component: ProfessionalDashboard },
  { path: '/request-service', component: ServiceRequest }
];

// Create router instance
const router = createRouter({
  history: createWebHistory(),
  routes
});

// Create Vue app instance and mount it
createApp(App)
  .use(router)
  .mount('#app');