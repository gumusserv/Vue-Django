import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    isAuthenticated: false,
    username: null,
    authToken: null  // 存储认证Token
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
    }
  },
  actions: {
    initializeAuth({ commit }) {
      const token = localStorage.getItem('userToken');
      if (token) {
        commit('setAuthToken', token);
        commit('setAuthentication', true);
        // Optionally get username from localStorage or another API call
        commit('setUsername', localStorage.getItem('username'));
      }
    },
    login({ commit }, credentials) {
      return axios.post('http://127.0.0.1:8000/api/accounts/login/', credentials)
        .then(response => {
          localStorage.setItem('userToken', response.data.token);  // Assume the token is returned by your backend
          localStorage.setItem('username', response.data.username || credentials.username);
          commit('setAuthToken', response.data.token);
          commit('setAuthentication', true);
          commit('setUsername', response.data.username || credentials.username);
        });
    },
    logout({ commit }) {
      localStorage.removeItem('userToken');
      localStorage.removeItem('username');
      commit('setAuthToken', null);
      commit('setAuthentication', false);
      commit('setUsername', null);
    },
    register({ commit }, credentials) {
      return axios.post('http://127.0.0.1:8000/api/accounts/register/', credentials)
        .then(() => {
          // Optionally handle token if registration also logs the user in
          commit('setAuthentication', true);
          commit('setUsername', credentials.username);  // Assuming username is part of credentials
        });
    }
  },
  getters: {
    isAuthenticated(state) {
      return state.isAuthenticated;
    },
    username(state) {
      return state.username;
    }
  }
});

