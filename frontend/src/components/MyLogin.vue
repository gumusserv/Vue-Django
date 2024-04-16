<!-- <template>
    <div class="login-container">
      <h1>Login</h1>
      <form @submit.prevent="login">
        <div>
          <label for="username">Username:</label>
          <input id="username" type="text" v-model="username" required>
        </div>
        <div>
          <label for="password">Password:</label>
          <input id="password" type="password" v-model="password" required>
        </div>
        <button type="submit">Login</button>
      </form>
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
        this.$store.dispatch('login', {
          username: this.username,
          password: this.password
        }).then(() => {
          this.$router.push('/'); // Redirect to home page after successful login
        }).catch(error => {
          alert('Login Failed: ' + error.response.data.error);
        });
      }
    }
  }
  </script>
  
  <style>
  .login-container {
    width: 300px;
    margin: auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  </style>
   -->

   <template>
    <div class="login-container">
      <h1>Login</h1>
      <form @submit.prevent="login">
        <div>
          <label for="username">Username:</label>
          <input id="username" type="text" v-model="username" required>
        </div>
        <div>
          <label for="password">Password:</label>
          <input id="password" type="password" v-model="password" required>
        </div>
        <button type="submit">Login</button>
      </form>
      <!-- 添加一个链接或按钮用于跳转到注册页面 -->
      <div class="register-link">
        <p>Don't have an account? <a href="#" @click="goToRegister">Register here</a></p>
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
        this.$store.dispatch('login', {
          username: this.username,
          password: this.password
        }).then(() => {
          this.$router.push('/'); // Redirect to home page after successful login
        }).catch(error => {
          alert('Login Failed: ' + error.response.data.error);
        });
      },
      goToRegister() {
        this.$router.push('/register'); // 导航到注册页面
      }
    }
  }
  </script>
  
  <style>
  .login-container {
    width: 300px;
    margin: auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  .register-link {
    margin-top: 20px;
    text-align: center;
  }
  </style>
  