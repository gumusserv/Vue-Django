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
    <button @click="toggleFavorite" :class="{'favorited': isFavorited}">
      <i class="fa" :class="isFavorited ? 'fa-star' : 'fa-star-o'"></i> 收藏
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
      isFavorited: false,
    };
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
    toggleFavorite() {
    const token = localStorage.getItem('authToken'); // 从 localStorage 获取 Token
      if (!token) {
        alert('请先登录再进行收藏！');
        this.$router.push('/login');
        return;
      }
      axios.post('/api/favorites/', { movie_id: this.movie.id }, {
        headers: { 'Authorization': `Token ${token}` }
      })
      .then(() => {
        this.isFavorited = true;
        alert('电影已收藏！');
      })
      .catch(error => {
        console.error('Error adding to favorites:', error);
        alert('收藏失败，请稍后重试！');
      });
    }
  },
  mounted() {
    this.fetchMovieDetails();
  }
}
</script>

  