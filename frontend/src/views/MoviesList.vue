<template>
  <div class="movie-list">
    <select v-model="searchType" @change="resetSearch">
      <option value="title">Search by Title</option>
      <option value="genre">Search by Genre</option>
    </select>
    <input v-model="searchQuery" :placeholder="placeholderText" @keyup.enter="fetchMovies">
    <button @click="fetchMovies">Search</button>
    <div v-if="loading">
      Loading...
    </div>
    <div v-else>
      <ul>
        <li v-for="movie in movies" :key="movie.id">
          <router-link :to="`/movies/${movie.movie_id}`">
            <h3>{{ movie.title }}</h3>
          </router-link>
        </li>

      </ul>
      <button @click="nextPage" :disabled="currentPage >= totalPages">Next Page</button>
    </div>
    <div v-if="error">
      Error loading data: {{ error }}
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      loading: false,
      error: null,
      movies: [],
      currentPage: 1,
      totalPages: 0,
      searchQuery: '',
      searchType: 'title',
    };
  },
  computed: {
    placeholderText() {
      return this.searchType === 'title' ? 'Enter movie title' : 'Enter genre';
    }
  },
  methods: {
    fetchMovies() {
      this.loading = true;
      const params = {
        page: this.currentPage,
        [this.searchType]: this.searchQuery
      };

      axios.get('http://127.0.0.1:8000/movies/api/movies/', { params })
        .then(response => {
          this.movies = response.data.results;
          this.totalPages = Math.ceil(response.data.count / 10);  // 根据后端返回的总数计算总页数
          this.loading = false;
        })
        .catch(error => {
          console.error("There was an error fetching the movies:", error);
          this.error = "Failed to load movies.";
          this.loading = false;
        });
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.fetchMovies(++this.currentPage);
      }
    },
    resetSearch() {
      this.searchQuery = '';
      this.movies = [];
      this.currentPage = 1;
      this.fetchMovies();
    }
  },
  mounted() {
    this.fetchMovies();
  }
}
</script>