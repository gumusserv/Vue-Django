// import { createStore } from 'vuex';
// import axios from 'axios';

// export default createStore({
//   state: {
//     isAuthenticated: false
//   },
//   mutations: {
//     setAuth(state, status) {
//       state.isAuthenticated = status;
//     }
//   },
//   actions: {
//     login({ commit }, credentials) {
//       return axios.post('http://127.0.0.1:8000/api/accounts/login/', credentials)
//         .then(() => {
//           commit('setAuth', true);
//         });
//     },
//     register({ commit }, credentials) {
//       return axios.post('http://127.0.0.1:8000/api/accounts/register/', credentials)
//         .then(() => {
//           commit('setAuth', true);
//         });
//     },
//     logout({ commit }) {
//       commit('setAuth', false);
//     }
//   }
// });

// src/store/index.js
import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    isAuthenticated: false
  },
  mutations: {
    setAuthentication(state, status) {
      state.isAuthenticated = status;
    }
  },
  actions: {
    login({ commit }, credentials) {
      return axios.post('http://127.0.0.1:8000/api/accounts/login/', credentials)
        .then(() => {
          commit('setAuthentication', true);
        });
    },
    logout({ commit }) {
      commit('setAuthentication', false);
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
    }
  }
});
