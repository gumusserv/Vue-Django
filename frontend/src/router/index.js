import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import MyLogin from '../components/MyLogin.vue';
import MyRegister from '../components/MyRegister.vue';

const routes = [
  { path: '/', name: 'Home', component: HomeView ,meta: { title: 'FCC: Tribute Page' }},
  { path: '/login', name: 'Login', component: MyLogin },
  { path: '/register', name: 'Register', component: MyRegister }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title || '默认标题';
  next();
});


export default router;
