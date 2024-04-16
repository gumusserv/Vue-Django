// src/store/index.js
import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    isAuthenticated: false,
    username: null
  },
  mutations: {
    setAuthentication(state, status) {
      state.isAuthenticated = status;
    },
    setUsername(state, username) {
      state.username = username;
    }
  },
  actions: {
    login({ commit }, credentials) {
      return axios.post('http://127.0.0.1:8000/api/accounts/login/', credentials)
        .then(response => {
          commit('setAuthentication', true);
          commit('setUsername', response.data.username || credentials.username);
        });
    },
    logout({ commit }) {
      commit('setAuthentication', false);
      commit('setAuthentication', null);
    },
    register({ commit }, credentials) {
      return axios.post('http://127.0.0.1:8000/api/accounts/register/', credentials)
        .then(() => {
          commit('setAuthentication', true);
        });
    }
  },
  getters: {
    isAuthenticated(state) {
      return state.isAuthenticated;
    },
    username(state){
      return state.username;  // 获取用户名
    } 
  }
});
