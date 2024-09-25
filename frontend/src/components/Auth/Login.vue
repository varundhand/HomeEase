<template>
  <div class="login-container d-flex justify-content-center align-items-center">
    <div class="card login-card">
      <div class="card-body">
        <div class="text-center mb-4">
          <img src="@/assets/logo/HomeEase-logo.png" alt="HomeEase Logo" class="logo">
        </div>
        <h3 class="card-title text-center mb-4">Welcome to HomeEase</h3>
        <form @submit.prevent="login">
          <div class="form-group">
            <input v-model="username" type="text" class="form-control login-input" placeholder="Username" required>
          </div>
          <div class="form-group">
            <input v-model="password" type="password" class="form-control login-input" placeholder="Password" required>
          </div>
          <div class="text-center">
            <button type="submit" class="btn btn-primary login-btn">Login</button>
          </div>
        </form>
        <div class="text-center mt-3">
          <a href="#" class="forgot-password">Forgot Password?</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    login() {
      // API call for authentication
    }
  }
};
</script>

<style scoped>
/* Container styling */
.login-container {
  height: 100vh;
  /* background: linear-gradient(135deg, #6dd5fa, #2980b9); */
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Card styling */
.login-card {
  width: 100%;
  max-width: 400px;
  border-radius: 12px;
  padding: 30px;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  background-color: #fff;
  animation: fadeIn 0.6s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(-20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Logo styling */
.logo {
  width: 180px;
  height: auto;
}

/* Input styling */
.login-input {
  border: 2px solid #ddd;
  border-radius: 8px;
  padding: 12px;
  margin-bottom: 15px;
  font-size: 16px;
  transition: all 0.3s ease-in-out;
}

.login-input:focus {
  border-color: #2980b9;
  box-shadow: 0 0 5px rgba(41, 128, 185, 0.5);
}

/* Button styling */
.login-btn {
  background-color: #2980b9;
  border: none;
  padding: 12px 40px;
  border-radius: 8px;
  font-size: 18px;
  font-weight: bold;
  transition: background-color 0.3s ease-in-out;
  display: inline-block;
}

.login-btn:hover {
  background-color: #2572a5;
}

/* Forgot password link */
.forgot-password {
  color: #2980b9;
  text-decoration: none;
  font-size: 14px;
}

.forgot-password:hover {
  text-decoration: underline;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .login-card {
    padding: 20px;
  }

  .logo {
    width: 140px;
  }
}
</style>
