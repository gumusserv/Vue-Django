<template>
    <div class="movie-detail" v-if="movie">
      <h1>{{ movie.title }}</h1>
      <p><strong>Duration:</strong> {{ movie.duration }} minutes</p>
      <p><strong>Year:</strong> {{ movie.year }}</p>
      <p><strong>Director:</strong> {{ movie.director }}</p>
      <p><strong>Actors:</strong> {{ movie.actors }}</p>
      <p><strong>Genre:</strong> {{ movie.genre }}</p>
      <p><strong>Link:</strong> <a :href="movie.movie_link" target="_blank">{{ movie.movie_link }}</a></p>
      <p><strong>Cover:</strong> <img :src="movie.cover_image_url" alt="Cover Image"></p>
      <p><strong>Rating:</strong> {{ movie.historical_rating }}</p>
      <button @click="addFavorite" v-if="isAuthenticated">
        <i class="fa fa-star"></i> 收藏
      </button>
    </div>
    <div v-else>
        Loading movie details...
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        movie: null,
        isFavorited: false,  // 初始未收藏
      };
    },
    computed: {
      isAuthenticated() {
        return this.$store.getters.isAuthenticated;
      },
      username() {
        return this.$store.getters.username;
      }
    },
    methods: {
      fetchMovieDetails() {
        const movieId = this.$route.params.id;
        axios.get(`http://127.0.0.1:8000/movies/api/movies/${movieId}/`)
          .then(response => {
            this.movie = response.data;
          })
          .catch(error => {
            console.error("There was an error fetching the movie details:", error);
          });
      },
      addFavorite() {
        const username = this.$store.getters.username;  // 从 Vuex 获取用户名
        const movie_id = this.$route.params.id;  // 从路由参数获取电影ID

        // 打印参数
        console.log('Username:', username);
        console.log('Movie ID:', movie_id);

        axios.post(`http://127.0.0.1:8000/api/favorites/add/?username=${username}&movie_id=${movie_id}`)
        .then(() => {
          alert('电影已成功收藏');
        })
        .catch(error => {
          console.error('Error adding to favorites:', error);
          alert('收藏失败，可能是因为未登录或其他错误');
        });

      }
    },
    mounted() {
      this.fetchMovieDetails();
    }
  }
  </script>
  