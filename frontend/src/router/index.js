import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import MyLogin from '../components/MyLogin.vue';
import MyRegister from '../components/MyRegister.vue';

const routes = [
  { path: '/', name: 'Home', component: HomeView },
  { path: '/login', name: 'Login', component: MyLogin },
  { path: '/register', name: 'Register', component: MyRegister }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
