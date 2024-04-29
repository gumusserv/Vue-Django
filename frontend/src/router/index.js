import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import MyLogin from '../components/MyLogin.vue';
import MyRegister from '../components/MyRegister.vue';
import MovieList from '../views/MoviesList.vue';  // 新增导入 MovieList 组件
import MovieDetail from '../views/MovieDetail.vue';

const routes = [
  { path: '/', name: 'Home', component: HomeView ,meta: { title: 'FCC: Tribute Page' }},
  { path: '/login', name: 'Login', component: MyLogin },
  { path: '/register', name: 'Register', component: MyRegister },
  { path: '/movies', name: 'MovieList', component: MovieList, meta: { title: 'Movie List' }},  // 新增路由
  { path: '/movies/:id', name: 'MovieDetail', component: MovieDetail },
  { path: '/movies/page/:page?', name: 'MovieListWithPage', component: MovieList, meta: { title: 'Movie List' }},  // 新增路由带页码
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
