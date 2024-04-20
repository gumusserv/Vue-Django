// src/store/index.js
import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    isAuthenticated: false,
    username: null,
    authToken: localStorage.getItem('authToken') || null, // 添加 Token 初始状态
  },
  mutations: {
    setAuthentication(state, status) {
      state.isAuthenticated = status;
    },
    setUsername(state, username) {
      state.username = username;
    },
    setAuthToken(state, token) {
      state.authToken = token;
      localStorage.setItem('authToken', token); // 保存 Token 到 localStorage
    },
    clearAuthToken(state) {
      state.authToken = null;
      localStorage.removeItem('authToken'); // 从 localStorage 移除 Token
      state.isAuthenticated = false; // 确保认证状态被重置
      state.username = null;
    }
  },
  actions: {
    login({ commit }, credentials) {
      return axios.post('http://127.0.0.1:8000/api/accounts/login/', credentials)
        .then(response => {
          commit('setAuthentication', true);
          commit('setUsername', response.data.username || credentials.username);
          commit('setAuthToken', response.data.token); // 假设后端返回 token
          localStorage.setItem('authToken', response.data.token); // 保存 Token 到 localStorage
        })
        .catch(error => {
          console.error('Login failed:', error);
          alert('Login Failed: ' + error.response.data.error);
          commit('setAuthentication', false);  // 确保认证状态为未登录
        });
    },
    logout({ commit }) {
      localStorage.removeItem('authToken'); // 移除 Token
      commit('setAuthentication', false);
      commit('setAuthentication', null);
      commit('clearAuthToken'); // 清除 Token 和认证状态
    },
    register({ commit }, credentials) {
      return axios.post('http://127.0.0.1:8000/api/accounts/register/', credentials)
        .then(response => {
          commit('setAuthentication', true);
          commit('setAuthToken', response.data.token); // 假设注册后立即登录
        });
    }
  },
  getters: {
    isAuthenticated(state) {
      return state.isAuthenticated;
    },
    username(state){
      return state.username;  // 获取用户名
    },
    authToken(state) {
      return state.authToken; // 提供 Token
    }
  }
});
