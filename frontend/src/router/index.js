import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import MyLogin from '../components/MyLogin.vue';
import MyRegister from '../components/MyRegister.vue';
import MovieList from '../views/MoviesList.vue';
import MovieDetail from '../views/MovieDetail.vue';

const routes = [
  { path: '/', name: 'Home', component: HomeView, meta: { title: 'FCC: Tribute Page' }},
  { path: '/login', name: 'Login', component: MyLogin },
  { path: '/register', name: 'Register', component: MyRegister },
  { path: '/movies', name: 'MovieList', component: MovieList, meta: { title: 'Movie List', requiresAuth: true }},  // 可能需要登录才能访问
  { path: '/movies/:id', name: 'MovieDetail', component: MovieDetail, meta: { requiresAuth: true }},  // 详情页需要登录才能访问
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  const isLoggedIn = localStorage.getItem('authToken'); // 检查本地存储中是否有 Token
  document.title = to.meta.title || '默认标题';

  if (to.matched.some(record => record.meta.requiresAuth) && !isLoggedIn) {
    // 如果路由需要认证，且用户未登录，重定向到登录页面
    next({ name: 'Login' });
  } else {
    next(); // 否则正常导航到目标页面
  }
});

export default router;
