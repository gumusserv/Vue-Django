<template>
<div class="background-image">
  <div class="container1">
    <div class="top">
      <div class="input-container1">
        <input type="text" v-model="searchQuery" placeholder="Search by movie title" @keyup.enter="fetchMoviesAndInitPage" class="search-input"/>
        <div class="search-button" @click="fetchMovies">
          <i class="fa fa-search"></i>
        </div>
        <div id="stats" v-if="!loading && !error">
          <span>{{totalResults  }} results found</span>
        </div>
        <div v-if="loading">Loading...</div>
        <div v-if="error">Error loading data: {{ error }}</div>
      </div>
    </div>

    <div class="navbar">
      <ul class="nav-list">
        <li><router-link to="/">主页</router-link></li>
        <li><router-link to="/movies">发现</router-link></li>
        <li v-if="isAuthenticated"><router-link to="/logout" @click.prevent="logout">退出</router-link></li>
        <li v-else><router-link to="/login">登录/注册</router-link></li>
      </ul>
    </div>


    
    <div class="content" v-if="!loading && !error">
      <div class="facets">
        <div class="facet">
          <div class="facet-title">Genre</div>
          <!-- Genre filters here -->
          <ul>
            <li v-for="genre in genres" :key="genre.name">
              <label>
                <input type="checkbox" v-model="genre.selected" @change="fetchMoviesAndInitPage">
                {{ genre.name }} <span class="genre-count">({{ genre.count }})</span>
              </label>
            </li>
          </ul>
        </div>


        <div class="facet">
          <div class="facet-title">Rating</div>
          <ul>
            <li v-for="rating in ratings" :key="rating.score">
              <label>
                <input type="radio" v-model="ratingFilter" :value="rating.score" @change="fetchMoviesAndInitPage">
                {{ rating.score }} stars and above ({{ rating.count }})
              </label>
            </li>
          </ul>
        </div>

        <div class="facet">
          <div class="facet-title">Year</div>
          <div class="year-range-selector">
            <label for="year-min">From:</label>
            <input type="range" id="year-min" v-model="yearMin" min="1951" max="2024" @change="fetchMoviesAndInitPage" />
            <span>{{ yearMin }}</span>
          </div>
          <div class="year-range-selector">
            <label for="year-max">To:</label>
            <input type="range" id="year-max" v-model="yearMax" min="1951" max="2024" @change="fetchMoviesAndInitPage" />
            <span>{{ yearMax }}</span>
          </div>
        </div>


      </div>
        
        

      <div class="canvas">
        <!-- <ul>
          <li v-for="movie in movies" :key="movie.id">
            <router-link :to="`/movies/${movie.movie_id}`">
              <article class="movie">
                <img class="movie-image" :src="movie.cover_image_url" />
                <div class="movie-meta">
                  <div class="movie-title">
                    {{ movie.title }}
                    <span class="movie-year">{{ movie.year }}</span>
                  </div>
                </div>
              </article>
            </router-link>
          </li>
        </ul> -->
        <div class="movie-list">
          <li v-for="movie in movies" :key="movie.id">
            <router-link :to="`/movies/${movie.movie_id}`">
              <article class="movie">
                <img class="movie-image" :src="movie.cover_image_url" />
                <div class="movie-meta">
                  <div class="movie-title">
                    {{ movie.title }}
                    <span class="movie-year">{{ movie.year }}</span>
                  </div>
                  <div class="movie-genres">
                    Genres: {{ movie.genre }}
                  </div>
                  <div class="movie-rating">
                    Rating: {{ movie.historical_rating }}
                  </div>
                </div>
              </article>
            </router-link>
          </li>
        </div>

        <div>
          <button @click="previousPage" :disabled="currentPage <= 1">Previous Page</button>
          <button @click="nextPage" :disabled="currentPage >= totalPages">Next Page</button>
        </div>
        <div id="pagination"></div>
      </div>
    </div>
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
      genres: [
        { name: '科幻', count: 0, selected: false },
        { name: '冒险', count: 0, selected: false },
        { name: '动作', count: 0, selected: false },
        { name: '喜剧', count: 0, selected: false },
        { name: '戏剧', count: 0, selected: false },
        { name: '爱情', count: 0, selected: false }
      ],
      ratingFilter: 0, // 默认不过滤（显示所有评分）
      ratings: [
        { score: 4, count: 0 },
        { score: 3, count: 0 },
        { score: 2, count: 0 },
        { score: 1, count: 0 },
        { score: 0, count: 0 }
      ],
      yearMin: 1951,
      yearMax: 2024,
      totalResults: 0,
    };
  },
  computed: {
    placeholderText() {
      return this.searchType === 'title' ? 'Enter movie title' : 'Enter genre';
    },
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    username() {
      return this.$store.getters.username;
    }
    
  },
  methods: {
    fetchMoviesAndInitPage(){
      this.currentPage = 1;
      this.fetchMovies();
    },
    fetchMovies() {
      this.loading = true;
      const selectedGenres = this.genres.filter(g => g.selected).map(g => g.name);
      const params = {
        page: this.currentPage,
        search: this.searchQuery,
        genres: selectedGenres.join(','),
        ratingMin: this.ratingFilter, // 添加评分过滤
        year_min: this.yearMin,
        year_max: this.yearMax,
      };

      axios.get('http://10.181.91.67:8000/movies/api/movies/', { params })
        .then(response => {
          this.movies = response.data.results;
          this.totalResults = response.data.count;
          this.totalPages = Math.ceil(response.data.count / 9);
          this.loading = false;
          this.fetchGenreCounts();
          this.fetchRatingCounts();
        })
        .catch(error => {
          this.error = "Failed to load movies: " + error.message;
          this.loading = false;
        });
    },
    


    fetchGenreCounts() {
      // 准备发送到后端的筛选参数
      const selectedGenres = this.genres.filter(g => g.selected).map(g => g.name);
      const params = {
        search: this.searchQuery, // 搜索关键词
        genres: selectedGenres.join(','), // 已选择的题材
        ratingMin: this.ratingFilter, // 最小评分
        year_min: this.yearMin,
        year_max: this.yearMax,
      };

      // 发送请求到后端，获取带有当前筛选条件的题材计数
      axios.get('http://10.181.91.67:8000/movies/api/genres/counts', { params })
        .then(response => {
          // 更新前端的题材数组，以匹配从后端接收到的计数
          this.genres.forEach(genre => {
            const found = response.data.genres.find(g => g.name === genre.name);
            genre.count = found ? found.count : 0; // 找到相应题材则更新，否则设为0
          });
        })
        .catch(error => {
          console.error("There was an error fetching the genre counts:", error);
        });
    },

    fetchRatingCounts() {
      const selectedGenres = this.genres.filter(g => g.selected).map(g => g.name);
      const params = {
        search: this.searchQuery,
        genres: selectedGenres.join(','),
        year_min: this.yearMin,
        year_max: this.yearMax,
      };

      axios.get('http://10.181.91.67:8000/movies/api/ratings/counts', { params })
        .then(response => {
          this.ratings.forEach(rating => {
            const found = response.data.ratings.find(r => r.rating === rating.score);
            rating.count = found ? found.count : 0;
          });
        })
        .catch(error => {
          console.error("There was an error fetching the rating counts:", error);
        });
    },

    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
        this.fetchMovies();
      }
    },
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
        this.fetchMovies();
      }
    },
    resetSearch() {
      this.searchQuery = '';
      this.genres.forEach(g => g.selected = false);
      this.currentPage = 1;
      this.fetchMovies();
    },
    logout() {
      this.$store.dispatch('logout').then(() => {
        this.$router.push('/login');
      });
    }
  },
  mounted() {
    this.fetchMovies();
    this.fetchGenreCounts();
  }
}
</script>

<style scoped>
* {
  box-sizing: border-box;
}



.container1 {
  /* display: flex; */
  flex-direction: column;
  width: 85%;
  min-height: 100vh; /* 使容器至少有视窗的高度 */
  margin: 0 auto; /* 水平居中 */
  justify-content: center; /* 垂直居中 */
  align-items: center; /* 使容器内的项目居中 */
}

.top {
  display: flex;
  justify-content: flex-start; /* 添加居中显示 */
  padding: 20px;
  width: 60%;
  margin: 0 auto; /* 水平居中 */
}

.input-container1 {
  display: flex;
  align-items: center;
  position: relative;
  justify-content: flex-start; /* 从左侧开始显示元素 */
  width: 100%;
  background-color: #fff; /* 背景色 */
  box-shadow: 0 2px 6px rgba(0,0,0,0.1); /* 阴影效果 */
  border-radius: 5px; /* 圆角边框 */
}

.input-container1 input {
  flex-grow: 1; /* 使输入框自适应宽度 */
  padding: 10px;
  border: none; /* 去除边框 */
  outline: none;
}

.search-select {
  border: 1px solid #cccccc; /* 给下拉菜单添加轻微的边框 */
  background-color: #ffffff; /* 设置白色背景 */
  padding: 10px 15px; /* 增加内边距以改善触摸体验 */
  margin-right: 10px;
  outline: none;
  cursor: pointer;
  border-radius: 5px; /* 添加圆角以使外观更加平滑 */
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1); /* 添加内阴影以增加深度感 */
  transition: all 0.3s; /* 添加过渡动画，使焦点和悬停效果更平滑 */
}

.search-select:hover {
  border-color: #007BFF; /* 鼠标悬停时改变边框颜色 */
  background-color: #f8f8f8; /* 鼠标悬停时轻微改变背景色以指示可交互性 */
}

.search-select:focus {
  border-color: #0056b3; /* 聚焦时使用更深的蓝色边框 */
  box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.25); /* 添加焦点时的外阴影，以增强可见性 */
}


.search-button {
  align-self: stretch;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2.4em;
  font-size: 1.6em;
  background-color: #0082f3;
  color: white;
  cursor: pointer;
  text-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
  box-shadow: inset 0 -6px 12px -8px rgba(0, 0, 0, 0.2), inset 0 6px 12px -8px rgba(255, 255, 255, 0.2);
  border-radius: 5px; /* 圆角 */
  margin-left: 10px; /* 间距 */
}
.search-button:hover {
  background-color: #0d8eff;
}
.search-button:active {
  background-color: #0066c0;
  box-shadow: inset 0 2px 6px rgba(0, 0, 0, 0.2);
}

#search-box {
  width: 100%;
  font-size: inherit;
  border: 1px solid rgba(0, 0, 0, 0.3);
  border-left: none;
  box-shadow: inset 0 2px 6px rgba(0, 0, 0, 0.1);
  outline: none;
  padding: 0.8em 1em;
  font-size: 1.2em;
}
#search-box:focus {
  box-shadow: inset 0 2px 6px rgba(0, 100, 220, 0.15);
  border-color: rgba(0, 100, 220, 0.6);
}

#stats {
  z-index: 1;
  position: absolute;
  bottom: 0.6em;
  right: 0.6em;
  font-size: 0.8em;
  color: rgba(0, 0, 0, 0.4);
}

.content {
  display: flex;
  margin-top: 1rem;
  border: 1px solid rgba(0, 0, 0, 0.3);
}

.canvas {
  flex: 1;
  display: flex;
  flex-direction: column;
  position: relative;
  padding: 10px;
  background-color: rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.1);
}

#hits {
  flex: 1;
}

.ais-hits {
  display: flex;
  flex-wrap: wrap;
}

.ais-hits__empty {
  height: 100%;
  justify-content: center;
  align-items: center;
  font-size: 1.6em;
  color: rgba(0, 0, 0, 0.4);
}

.ais-hits--item {
  flex: 1 0 25%;
  min-width: 380px;
}

.movie {
  position: relative;
  display: flex;
  margin: 10px;
  border: 1px solid rgba(0, 0, 0, 0.4);
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  background-color: white;
  padding: 0.2em;
}

.movie-image {
  flex-shrink: 0;
  height: 231px;
  width: 154px;
  background-color: rgba(0, 0, 0, 0.1);
}

.movie-meta {
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin-left: 1em;
}

.movie-title {
  align-items: center;
  font-size: 1.1em;
  font-weight: bold;
}
.movie-title em {
  color: #0096e6;
  background: rgba(0, 160, 220, 0.2);
}

.movie-year {
  font-size: 0.8em;
  font-weight: normal;
  color: rgba(0, 0, 0, 0.6);
}

.movie-rating {
  margin-top: 0.2em;
}

.movie-genres {
  display: flex;
  flex-wrap: wrap;
  font-size: 0.8em;
  margin-top: 0.7em;
  margin-right: -0.4em;
  margin-bottom: -0.4em;
}

.movie-genre {
  color: rgba(0, 0, 0, 0.7);
  padding: 0.4em 0.6em;
  background-color: rgba(0, 0, 0, 0.1);
  margin-right: 0.4em;
  margin-bottom: 0.4em;
}

ul.ais-pagination {
  padding: 0;
  margin: 0;
}

#pagination {
  margin: 10px 0;
  text-align: center;
}

.ais-pagination--item {
  margin: 0 0.2em;
}

.ais-pagination--link {
  font-size: 1.2em;
  text-decoration: none;
  color: rgba(0, 0, 0, 0.4);
}
.ais-pagination--item__active .ais-pagination--link {
  font-weight: bold;
  color: rgba(0, 100, 220, 0.6);
}

.facets {
  width: 20%;
  min-width: 270px;
  border-right: 1px solid rgba(0, 0, 0, 0.3);
}

.facet {
  padding: 1em 0;
  border-bottom: 2px solid rgba(0, 0, 0, 0.1);
}

.facet-title {
  padding: 0 1em;
  font-size: 1.1em;
  margin-bottom: 0.6em;
}

.ais-refinement-list--item {
  padding: 0 1em;
  cursor: pointer;
  color: rgba(0, 0, 0, 0.7);
}
.ais-refinement-list--item:hover {
  color: black;
  background-color: rgba(0, 0, 0, 0.04);
}
.ais-refinement-list--item.ais-refinement-list--item__active {
  background-color: rgba(0, 0, 0, 0.08);
  font-weight: bold;
  color: black;
}

.ais-refinement-list--label {
  position: relative;
  display: flex;
  line-height: 1.4em;
  cursor: inherit;
}
.ais-refinement-list--label input[type=checkbox] {
  display: none;
}

.ais-refinement-list--count, .ais-star-rating--count {
  top: 0;
  position: absolute;
  right: 0;
  font-size: 0.8em;
  color: rgba(0, 0, 0, 0.4);
}

.ais-star-rating--item {
  padding: 0 1em;
  cursor: pointer;
  color: rgba(0, 0, 0, 0.7);
}
.ais-star-rating--item:hover {
  color: black;
  background-color: rgba(0, 0, 0, 0.04);
}
.ais-star-rating--item.ais-star-rating--item__active {
  background-color: rgba(0, 0, 0, 0.08);
  font-weight: bold;
  color: black;
}

.ais-star-rating--link {
  position: relative;
  display: block;
  text-decoration: none;
  line-height: 1.4em;
  color: inherit;
}

.ais-range-slider--tooltip {
  position: relative;
  background: none;
}

.ais-range-slider--handle {
  display: flex;
  justify-content: center;
}

#year {
  padding: 0 2em;
}

.facet ul {
  list-style: none;
  padding: 0;
}

.facet li {
  cursor: pointer;
  padding: 10px;
  border-bottom: 1px solid #ccc;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.facet li:hover {
  background-color: #f0f0f0;
}

.genre-count {
  color: #666;
  font-size: 0.9em;
}

input[type="radio"] {
  display: none;
}

input[type="radio"] + label:before {
  content: "\f005"; /* FontAwesome Star */
  font-family: FontAwesome;
  display: inline-block;
  margin-right: 5px;
}

input[type="radio"]:checked + label:before {
  color: #ffd700; /* Gold color for selected star */
}

.year-range-selector {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.year-range-selector label {
  margin-right: 10px;
}

.year-range-selector input[type="range"] {
  margin-right: 10px;
}

.movie-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between; /* This can adjust spacing */
  margin: 0 -15px; /* Adjust gutter space here */
}

.movie {
  flex: 1 1 29%; /* Adjusted for gutter */
  margin: 10px; /* Gutter space */
  padding: 10px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  border-radius: 5px;
  background-color: white;
}

@media (max-width: 800px) {
  .movie {
    flex: 1 1 47%; /* On smaller screens, show 2 per row */
  }
}

@media (max-width: 500px) {
  .movie {
    flex: 1 1 100%; /* On very small screens, show 1 per row */
  }
}



</style>