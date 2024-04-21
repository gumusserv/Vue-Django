import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
store.dispatch('initializeAuth');

import './assets/global.css';


createApp(App).use(store).use(router).mount('#app')
