<!-- <template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script> -->

<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <div class="auth-options">
      <button v-if="!isAuthenticated" @click="goToLogin">登录/注册</button>
      <button v-if="isAuthenticated" @click="logout">退出</button>
    </div>
  </div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  },
  computed: {
    ...mapGetters([
      'isAuthenticated'
    ])
  },
  methods: {
    goToLogin() {
      this.$router.push('/login');
    },
    logout() {
      this.$store.dispatch('logout').then(() => {
        this.$router.push('/login');
      });
    }
  }
}
</script>

<style>
.auth-options button {
  margin: 10px;
  padding: 5px 20px;
}
</style>
