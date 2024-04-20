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
    },
    mounted() {
      this.fetchMovieDetails();
    }
  }
  </script>
  