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
      <button @click="toggleFavorite" v-if="isAuthenticated">
        <i class="fa" :class="isFavorited ? 'fa-star' : 'fa-star-o'"></i> {{ isFavorited ? '取消收藏' : '收藏' }}
      </button>
      <!-- 评论区 -->
      <div>
        <textarea v-model="userComment" placeholder="Add your comment here..."></textarea>
        <button @click="submitComment" v-if="isAuthenticated">Submit Comment</button>
        <button @click="deleteComment" v-if="isAuthenticated">Delete Comment</button>
      </div>

      <!-- 评分区 -->
      <div>
        <input type="number" v-model.number="userRating" placeholder="Rate (0-5)" min="0" max="5">
        <button @click="submitRating" v-if="isAuthenticated">Submit Rating</button>
        <button @click="deleteRating" v-if="isAuthenticated">Delete Rating</button>
      </div>
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
        userComment: '',
        userRating: null,  // 存储用户输入的评分
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
        axios.get(`http://10.110.0.110:8000/movies/api/movies/${movieId}/`)
          .then(response => {
            this.movie = response.data;
            this.checkFavorite();
          })
          .catch(error => {
            console.error("There was an error fetching the movie details:", error);
          });
      },
      // addFavorite() {
      //   const username = this.$store.getters.username;  // 从 Vuex 获取用户名
      //   const movie_id = this.$route.params.id;  // 从路由参数获取电影ID

      //   // 打印参数
      //   console.log('Username:', username);
      //   console.log('Movie ID:', movie_id);

      //   axios.post(`http://10.110.0.110:8000/api/favorites/add/`,{
      //       username: username,
      //       movie_id: movie_id
      //     })
      //   .then(() => {
      //     alert('电影已成功收藏');
      //   })
      //   .catch(error => {
      //     console.error('Error adding to favorites:', error);
      //     alert('收藏失败，可能是因为未登录或其他错误');
      //   });
      // },
      toggleFavorite() {
            const url = `http://10.110.0.110:8000/api/favorites/${this.isFavorited ? 'remove' : 'add'}/`;
            axios.post(url, {
                username: this.username,
            movie_id: this.movie.movie_id
        })
        .then(() => {
            this.isFavorited = !this.isFavorited;  // 切换收藏状态
            alert(`电影已${this.isFavorited ? '收藏' : '取消收藏'}`);
        })
        .catch(error => {
            console.error('Error toggling favorite:', error);
            alert('操作失败，可能是因为未登录或其他错误');
        });
    },
    checkFavorite() {
        const username = this.$store.getters.username;  // 从 Vuex 获取用户名
        const movie_id = this.$route.params.id;  // 从路由参数获取电影ID
        axios.get(`http://10.110.0.110:8000/api/favorites/check/${username}/${movie_id}/`)  // 确保末尾有斜杠
        .then(response => {
            this.isFavorited = response.data.isFavorited;
        })
        .catch(error => {
            console.error('Error checking favorite status:', error);
        });
    },

      submitComment() {
        const username = this.$store.getters.username;  // 从 Vuex 获取用户名
        const movie_id = this.$route.params.id;  // 从路由参数获取电影ID

        axios.post('http://10.110.0.110:8000/api/comment/add-comment/', {
          username: username,
          movie_id: movie_id,
          comment: this.userComment
        })
        .then(() => {
          alert('评论成功提交！');
        })
        .catch(error => {
          console.error('Error submitting comment:', error);
          alert('提交评论失败，可能是因为未登录或其他错误');
        });
      },
      deleteComment() {
        const username = this.$store.getters.username;  // 从 Vuex 获取用户名
        const movie_id = this.$route.params.id;  // 从路由参数获取电影ID
        // 假设后端提供了一个删除评论的API
        // axios.delete(`http://10.110.0.110:8000/api/comment/delete-comment`,{
        axios.post(`http://10.110.0.110:8000/api/comment/delete-comment/`,{
          username: username,
          movie_id: movie_id,
        })
        .then(() => {
          alert('评论已删除');
          this.userComment = '';
        })
        .catch(error => {
          console.error('Error deleting comment:', error);
          alert('删除评论失败');
        });
      },

      submitRating() {
        const username = this.$store.getters.username;  // 从 Vuex 获取用户名
        const movie_id = this.$route.params.id;  // 从路由参数获取电影ID
        // 假设后端提供了一个提交评分的API
        axios.post(`http://10.110.0.110:8000/api/comment/add-rating/`, {
          username: username,
          movie_id: movie_id,
          rating: this.userRating
        })
        .then(() => {
          alert('评分成功提交！');
          this.fetchMovieDetails();  // 重新获取电影详情以更新页面上的评分信息
        })
        .catch(error => {
          console.error('Error submitting rating:', error);
          alert('提交评分失败');
        });
      },

      deleteRating() {
        const username = this.$store.getters.username;  // 从 Vuex 获取用户名
        const movie_id = this.$route.params.id;  // 从路由参数获取电影ID
        // 假设后端提供了一个删除评分的API
        axios.delete(`http://10.110.0.110:8000/api/comment/delete-rating/`, {
          username: username,
          movie_id: movie_id,
        })
        .then(() => {
          alert('评分已删除');
          this.userRating = null;
        })
        .catch(error => {
          console.error('Error deleting rating:', error);
          alert('删除评分失败');
        });
      }
    },
    mounted() {
      this.fetchMovieDetails();
    }
  }
  </script>
  