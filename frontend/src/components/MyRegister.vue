<!-- <template>
    <div class="register-container">
      <h1>Register</h1>
      <form @submit.prevent="register">
        <div>
          <label for="username">Username:</label>
          <input id="username" type="text" v-model="username" required>
        </div>
        <div>
          <label for="password">Password:</label>
          <input id="password" type="password" v-model="password" required>
        </div>
        <button type="submit">Register</button>
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
      register() {
        this.$store.dispatch('register', {
          username: this.username,
          password: this.password
        }).then(() => {
          this.$router.push('/'); // Redirect to home page after successful registration
        }).catch(error => {
          alert('Registration Failed: ' + error.response.data.error);
        });
      }
    }
  }
  </script>
  
  <style>
  .register-container {
    width: 300px;
    margin: auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  </style>
   -->

   <template>
    <div class="register-container">
      <h1>Register</h1>
      <form @submit.prevent="register">
        <div>
          <label for="username">Username:</label>
          <input id="username" type="text" v-model="username" required>
        </div>
        <div>
          <label for="password">Password:</label>
          <input id="password" type="password" v-model="password" required>
        </div>
        <button type="submit">Register</button>
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
      register() {
        this.$store.dispatch('register', {
          username: this.username,
          password: this.password
        }).then(() => {
          this.$router.push('/login'); // Redirect to login page after successful registration
          alert('Registration successful. Please login.');
        }).catch(error => {
          alert('Registration Failed: ' + error.response.data.error);
        });
      }
    }
  }
  </script>
  
  <style>
  .register-container {
    width: 300px;
    margin: auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  </style>
  