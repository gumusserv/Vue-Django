<template>
    <div class="movie-detail" v-if="movie">
      
      <!-- <h1>{{ movie.title }}</h1>
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
      </button> -->
      <!-- 评论区 -->
      <!-- <div>
        <textarea v-model="userComment" placeholder="Add your comment here..."></textarea>
        <button @click="submitComment" v-if="isAuthenticated">Submit Comment</button>
        <button @click="deleteComment" v-if="isAuthenticated">Delete Comment</button>
      </div> -->

      <!-- 评分区 -->
      <!-- <div>
        <input type="number" v-model.number="userRating" placeholder="Rate (0-5)" min="0" max="5">
        <button @click="submitRating" v-if="isAuthenticated">Submit Rating</button>
        <button @click="deleteRating" v-if="isAuthenticated">Delete Rating</button>
      </div> -->
      <section class="content">
        <article class="demo-area">
        <img class="demo-trigger" :src="movie.cover_image_url" data-zoom="https://demos.imgix.net/wristwatch.jpg?w=1000&ch=DPR&dpr=2">
        <div class="detail">
        <section>
          <div class="title-row">
            <h1><strong>{{ movie.title }} ({{ movie.year }})</strong></h1>
            <button @click="toggleFavorite" v-if="isAuthenticated" style="margin-left: 30px;">
              <i class="fa" :class="isFavorited ? 'fa-heart' : 'fa-heart-o'" style="color: red;"></i>
              {{ isFavorited ? '取消收藏' : '收藏' }}
          </button>
        </div>
            <ul>
              <li><p><strong>时长:</strong> {{ movie.duration }} minutes</p></li>
              <li><p><strong>导演:</strong> {{ movie.director }}</p></li>
              <li><p><strong>演员:</strong> {{ movie.actors }}</p></li>
              <li><p><strong>主题:</strong> {{ movie.genre }}</p></li>
              <li><p><strong>评分:</strong> {{ movie.historical_rating }}</p></li>
              <li><p><strong>链接:</strong> {{ movie.movie_link }}</p></li>
            </ul>
            <form class="rating">
              <div class="myRating">
              <p>评价:</p>
              <div class="rating__stars">
                <input id="rating-1" class="rating__input rating__input-1" type="radio" name="rating" value="1" v-model.number="userRating" @change="submitRating" v-if="isAuthenticated">
                <input id="rating-2" class="rating__input rating__input-2" type="radio" name="rating" value="2" v-model.number="userRating" @change="submitRating" v-if="isAuthenticated">
                <input id="rating-3" class="rating__input rating__input-3" type="radio" name="rating" value="3" v-model.number="userRating" @change="submitRating" v-if="isAuthenticated">
                <input id="rating-4" class="rating__input rating__input-4" type="radio" name="rating" value="4" v-model.number="userRating" @change="submitRating" v-if="isAuthenticated">
                <input id="rating-5" class="rating__input rating__input-5" type="radio" name="rating" value="5" v-model.number="userRating" @change="submitRating" v-if="isAuthenticated">
                <label class="rating__label" for="rating-1">
                  <svg class="rating__star" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true">
                    <g transform="translate(16,16)">
                      <circle class="rating__star-ring" fill="none" stroke="#000" stroke-width="16" r="8" transform="scale(0)" />
                    </g>
                    <g stroke="#000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <g transform="translate(16,16) rotate(180)">
                        <polygon class="rating__star-stroke" points="0,15 4.41,6.07 14.27,4.64 7.13,-2.32 8.82,-12.14 0,-7.5 -8.82,-12.14 -7.13,-2.32 -14.27,4.64 -4.41,6.07" fill="none" />
                        <polygon class="rating__star-fill" points="0,15 4.41,6.07 14.27,4.64 7.13,-2.32 8.82,-12.14 0,-7.5 -8.82,-12.14 -7.13,-2.32 -14.27,4.64 -4.41,6.07" fill="#000" />
                      </g>
                      <g transform="translate(16,16)" stroke-dasharray="12 12" stroke-dashoffset="12">
                        <polyline class="rating__star-line" transform="rotate(0)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(72)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(144)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(216)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(288)" points="0 4,0 16" />
                      </g>
                    </g>
                  </svg>
                  <span class="rating__sr">1 star—Terrible</span>
                </label>
                <label class="rating__label" for="rating-2">
                  <svg class="rating__star" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true">
                    <g transform="translate(16,16)">
                      <circle class="rating__star-ring" fill="none" stroke="#000" stroke-width="16" r="8" transform="scale(0)" />
                    </g>
                    <g stroke="#000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <g transform="translate(16,16) rotate(180)">
                        <polygon class="rating__star-stroke" points="0,15 4.41,6.07 14.27,4.64 7.13,-2.32 8.82,-12.14 0,-7.5 -8.82,-12.14 -7.13,-2.32 -14.27,4.64 -4.41,6.07" fill="none" />
                        <polygon class="rating__star-fill" points="0,15 4.41,6.07 14.27,4.64 7.13,-2.32 8.82,-12.14 0,-7.5 -8.82,-12.14 -7.13,-2.32 -14.27,4.64 -4.41,6.07" fill="#000" />
                      </g>
                      <g transform="translate(16,16)" stroke-dasharray="12 12" stroke-dashoffset="12">
                        <polyline class="rating__star-line" transform="rotate(0)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(72)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(144)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(216)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(288)" points="0 4,0 16" />
                      </g>
                    </g>
                  </svg>
                  <span class="rating__sr">2 stars—Bad</span>
                </label>
                <label class="rating__label" for="rating-3">
                  <svg class="rating__star" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true">
                    <g transform="translate(16,16)">
                      <circle class="rating__star-ring" fill="none" stroke="#000" stroke-width="16" r="8" transform="scale(0)" />
                    </g>
                    <g stroke="#000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <g transform="translate(16,16) rotate(180)">
                        <polygon class="rating__star-stroke" points="0,15 4.41,6.07 14.27,4.64 7.13,-2.32 8.82,-12.14 0,-7.5 -8.82,-12.14 -7.13,-2.32 -14.27,4.64 -4.41,6.07" fill="none" />
                        <polygon class="rating__star-fill" points="0,15 4.41,6.07 14.27,4.64 7.13,-2.32 8.82,-12.14 0,-7.5 -8.82,-12.14 -7.13,-2.32 -14.27,4.64 -4.41,6.07" fill="#000" />
                      </g>
                      <g transform="translate(16,16)" stroke-dasharray="12 12" stroke-dashoffset="12">
                        <polyline class="rating__star-line" transform="rotate(0)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(72)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(144)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(216)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(288)" points="0 4,0 16" />
                      </g>
                    </g>
                  </svg>
                  <span class="rating__sr">3 stars—OK</span>
                </label>
                <label class="rating__label" for="rating-4">
                  <svg class="rating__star" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true">
                    <g transform="translate(16,16)">
                      <circle class="rating__star-ring" fill="none" stroke="#000" stroke-width="16" r="8" transform="scale(0)" />
                    </g>
                    <g stroke="#000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <g transform="translate(16,16) rotate(180)">
                        <polygon class="rating__star-stroke" points="0,15 4.41,6.07 14.27,4.64 7.13,-2.32 8.82,-12.14 0,-7.5 -8.82,-12.14 -7.13,-2.32 -14.27,4.64 -4.41,6.07" fill="none" />
                        <polygon class="rating__star-fill" points="0,15 4.41,6.07 14.27,4.64 7.13,-2.32 8.82,-12.14 0,-7.5 -8.82,-12.14 -7.13,-2.32 -14.27,4.64 -4.41,6.07" fill="#000" />
                      </g>
                      <g transform="translate(16,16)" stroke-dasharray="12 12" stroke-dashoffset="12">
                        <polyline class="rating__star-line" transform="rotate(0)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(72)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(144)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(216)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(288)" points="0 4,0 16" />
                      </g>
                    </g>
                  </svg>
                  <span class="rating__sr">4 stars—Good</span>
                </label>
                <label class="rating__label" for="rating-5">
                  <svg class="rating__star" width="32" height="32" viewBox="0 0 32 32" aria-hidden="true">
                    <g transform="translate(16,16)">
                      <circle class="rating__star-ring" fill="none" stroke="#000" stroke-width="16" r="8" transform="scale(0)" />
                    </g>
                    <g stroke="#000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <g transform="translate(16,16) rotate(180)">
                        <polygon class="rating__star-stroke" points="0,15 4.41,6.07 14.27,4.64 7.13,-2.32 8.82,-12.14 0,-7.5 -8.82,-12.14 -7.13,-2.32 -14.27,4.64 -4.41,6.07" fill="none" />
                        <polygon class="rating__star-fill" points="0,15 4.41,6.07 14.27,4.64 7.13,-2.32 8.82,-12.14 0,-7.5 -8.82,-12.14 -7.13,-2.32 -14.27,4.64 -4.41,6.07" fill="#000" />
                      </g>
                      <g transform="translate(16,16)" stroke-dasharray="12 12" stroke-dashoffset="12">
                        <polyline class="rating__star-line" transform="rotate(0)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(72)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(144)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(216)" points="0 4,0 16" />
                        <polyline class="rating__star-line" transform="rotate(288)" points="0 4,0 16" />
                      </g>
                    </g>
                  </svg>
                  <span class="rating__sr">5 stars—Excellent</span>
                </label>
                <p class="rating__display" data-rating="1" hidden>Terrible</p>
                <p class="rating__display" data-rating="2" hidden>Bad</p>
                <p class="rating__display" data-rating="3" hidden>OK</p>
                <p class="rating__display" data-rating="4" hidden>Good</p>
                <p class="rating__display" data-rating="5" hidden>Excellent</p>
              </div>
            </div>
            </form>
          </section>
        </div>
        </article>
      </section>
      <section class="content">
        <article>
          <h1>电影介绍</h1>
          <p>{{movie.description}}</p>
          <p>忘了写电影介绍字段, 先拿这段文字占位置.............</p>
          
        </article>
      </section>



      <div class="comments-section">
        <div class="comments">
          <h4>COMMENTS</h4>
          <div id="comments-container">
            <div class="comment" v-for="comment in comments" :key="comment.username">
              <div class="comment-user">
                <div class="avatar">
                  {{ comment.username }}
                </div>
              </div>
              <div class="comment-text">
                {{ comment.comment_text }}
              </div>
            </div> 
          </div>
        </div>
        <div class="comments">
          <h4>LEAVE A COMMENT</h4>
          <div id="comments-container">
            <div class="comment">
              <textarea v-model="userComment" placeholder="Add your comment here..." v-if="!hasUserCommented()"></textarea>
              <textarea v-model="userComment" placeholder="You have comment." v-else></textarea>
              <br>
              <button @click="submitComment" v-if="isAuthenticated">Submit Comment</button>
              <button @click="deleteComment" v-if="isAuthenticated">Delete Comment</button>
            </div>
          </div>
          
          <div id="comment-form"></div>
        </div>
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
        loading: false,
        movie: null,
        isFavorited: false,  // 初始未收藏
        userComment: '',
        userRating: null,  // 存储用户输入的评分
        // lastConfirmedRating: null // 最后一次提交的评分
        comments: []
      };
    },
    computed: {
      isAuthenticated() {
        return this.$store.getters.isAuthenticated;
      },
      username() {
        return this.$store.getters.username;
      },
      
    },
    methods: {
      hasUserCommented() {
        const currentUsername = this.username;
        // return this.comments.some(comment => comment.username === currentUsername);
        const userComment = this.comments.find(comment => comment.username === currentUsername && comment.comment_text != null);
        if (userComment) {
          console.log(`User ${currentUsername} has commented: ${userComment.comment_text}`);
          this.userComment = userComment.comment_text;
          return true;
        }
        console.log(`没评论!!!!!!!`);
        return false;
        },
      fetchComments() {
        this.loading = true;
        const movieId = this.$route.params.id;
        axios.get(`http://10.181.91.67:8000/api/comment/get_comments_byMovies/?movie_id=${movieId}`)
          .then(response => {
            this.comments = response.data.results;
            this.loading = false;
            console.log('Movie ID:', this.favorites);
          })
          .catch(error => {
            console.error("Failed to load favorites: ", error.message);
            this.loading = false;
          });
      },
      fetchMovieDetails() {
        const movieId = this.$route.params.id;
        axios.get(`http://10.181.91.67:8000/movies/api/movies/${movieId}/`)
          .then(response => {
            this.movie = response.data;
            this.checkFavorite();
          })
          .catch(error => {
            console.error("There was an error fetching the movie details:", error);
          });
        this.fetchComments();
      },
      toggleFavorite() {
            const url = `http://10.181.91.67:8000/api/favorites/${this.isFavorited ? 'remove' : 'add'}/`;
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
        axios.get(`http://10.181.91.67:8000/api/favorites/check/${username}/${movie_id}/`)  // 确保末尾有斜杠
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

        axios.post('http://10.181.91.67:8000/api/comment/add-comment/', {
          username: username,
          movie_id: movie_id,
          comment: this.userComment
        })
        .then(() => {
          alert('评论成功提交！');
          this.fetchComments();
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
        // axios.delete(`http://10.181.91.67:8000/api/comment/delete-comment`,{
        axios.post(`http://10.181.91.67:8000/api/comment/delete-comment/`,{
          username: username,
          movie_id: movie_id,
        })
        .then(() => {
          alert('评论已删除');
          this.userComment = '';
          this.fetchMovieDetails();
          this.fetchComments();
        })
        .catch(error => {
          console.error('Error deleting comment:', error);
          alert('删除评论失败');
        });
      },

      submitRating() {
        const rating = parseInt(this.userRating, 10);  // 确保评分是一个整数
        
        const username = this.$store.getters.username;  // 从 Vuex 获取用户名
        const movie_id = this.$route.params.id;  // 从路由参数获取电影ID
        

        // 检查评分是否在0到5之间
        if (rating < 0 || rating > 5) {
          // alert('评分值必须在0到5之间');
          return;
        }
        this.lastConfirmedRating = rating;
        // 假设后端提供了一个提交评分的API
        axios.post(`http://10.181.91.67:8000/api/comment/add-rating/`, {
          username: username,
          movie_id: movie_id,
          // rating: this.userRating
          rating: rating,
        })
        .then(() => {
          // alert('评分成功提交！');
          this.fetchMovieDetails();  // 重新获取电影详情以更新页面上的评分信息
        })
        .catch(error => {
          console.error('Error submitting rating:', error);
          // alert('提交评分失败');
        });
        
      },

      deleteRating() {
        const username = this.$store.getters.username;  // 从 Vuex 获取用户名
        const movie_id = this.$route.params.id;  // 从路由参数获取电影ID
        // 假设后端提供了一个删除评分的API
        axios.delete(`http://10.181.91.67:8000/api/comment/delete-rating/`, {
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
      this.fetchComments();
    }
  }
  </script>
  
<style scoped>
@charset "UTF-8";
@import url(https://fonts.googleapis.com/css?family=Roboto:400,500,300);
/* Foreground color for text and UI elements */
/* 20% lighter */
/* 20% darker */
/* Used for borders, dividers, etc. */
/* 10% lighter */
/* 10% darker */
/*--- Inverted Colors ---*/
/* Background color */
/* 10% lighter */
/* 10% darker */
/* Foreground color for text and UI elements */
/* Used for borders, dividers, etc. */
/* 10% lighter */
/* 10% darker */
/*--- Accent Colors ---*/
/* Primary accent color (orange) */
/* 10% lighter */
/* 10% darker */
/* 20% lighter */
/* 20% darker */
/* Secondary accent color (blue) */
/* 10% lighter */
/* 10% darker */
/* 20% lighter */
/* 20% darker */
/* Tertiary accent colors */
/* H:156 S:82 B:89 */
/* 20% lighter */
/* 10% darker */
/* Basic */
body {
  color: #475F72;
  font-family: "Roboto", "Helvetica Neue", "Helvetica", "Arial", "sans";
  font-size: 16px;
  margin: 0 0 0 0;
  text-rendering: optimizeLegibility;
}

article {
  margin: 2em auto 0 auto;
  max-width: 60em;
}
article > img {
  max-width: 100%;
}
article figure img {
  max-width: 100%;
}

article:first-child {
  margin-top: 0;
}

article:after {
  content: "";
  display: block;
  clear: both;
}

blockquote {
  border-left: solid 4px #6686a0;
  color: #6686a0;
  font-size: 150%;
  font-weight: 400;
  line-height: 1.4;
  margin: 1em;
  max-width: 640px;
  padding: 0 0 0 1em;
  text-indent: 0em;
}

button, a.button {
  align-items: flex-start;
  background-color: #00C0FA;
  border: none;
  border-radius: 4px;
  border-bottom: solid 2px #D0D7DD;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  color: #FFF;
  display: inline-block;
  font-family: "Roboto", "Helvetica Neue", "Helvetica", "Arial", "sans";
  font-size: 12px;
  line-height: 1;
  margin: 0;
  padding: 12px;
  text-align: center;
  text-decoration: none;
  text-transform: uppercase;
  vertical-align: bottom;
}
button:focus, a.button:focus {
  outline: none;
}
button:hover, a.button:hover {
  background-color: #2ecfff;
  cursor: pointer;
}
button:active, a.button:active {
  background-color: #0099c7;
  outline: none;
}

code {
  color: #6686a0;
  font-family: "Andale Mono", "Menlo", mono;
  padding: 0 0.4em;
  background-color: rgba(125, 144, 160, 0.1);
  border-radius: 3px;
  display: inline-block;
}

figure {
  margin: 2em 0;
  padding: 0;
}
figure figcaption {
  color: #b2bec8;
  font-size: 1em;
  padding-top: 1em;
}

figure:first-child {
  margin-top: 0;
}

footer {
  max-width: 36em;
  margin: 0 auto;
  padding-top: 2em;
  padding-bottom: 2em;
  text-align: center;
}

h1, h2, h3 {
  color: #475F72;
  font-size: 280%;
  font-weight: 500;
  line-height: 1.2;
  text-align: left;
  margin: 0 0 0.25em 0;
}

h2, h3, h4, h5, h6 {
  color: #6686a0;
  font-size: 180%;
  font-weight: 400;
  margin: 0 0 0.5em 0;
}

h3, h4, h5, h6 {
  color: #475F72;
  font-size: 150%;
  margin: 0 0 0.2em 0;
}

hr {
  margin: 2em 0;
  padding: 0;
  border-top: solid 1px rgba(102, 134, 160, 0.1);
}

p {
  margin-bottom: 1em;
  text-align: left;
  color: #475F72;
  line-height: 1.45;
  
}

p a {
  border-bottom: solid 1px #00C0FA;
  color: #00C0FA;
  text-decoration: none;
}
p a:active {
  background-color: #00C0FA;
  border-bottom: solid 1px #00C0FA;
  color: #FFF;
}
p a:hover {
  border-bottom: dotted 1px #2ecfff;
  color: #2ecfff;
}

section {
  padding: 2em 0 0;
}

ul, ol {
  color: #475F72;
  margin-bottom: 1em;
}
ul li, ol li {
  margin-bottom: 0.5em;
  font-size: 150%;
}
ul li:last-child, ol li:last-child {
  margin-bottom: 0;
}

.button-group {
  margin-top: 2em;
  text-align: center;
}

.content {
  margin-top: 2em;
  clear: both;
  padding-left: 1.5em;
  padding-right: 1.5em;
}
@media (min-width: 768px) {
  .content {
    padding-left: 0;
    padding-right: 0;
  }
}

section.content:first-child {
  padding-top: 0;
}

/* Single Line Code View for Imgix URLs*/
.single-line {
  display: block;
  margin: 0;
  padding: 0;
  width: 100%;
  overflow: hidden;
  white-space: nowrap;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  border-radius: 4px;
  /* Include a Sandbox Button Link */
}
.single-line code {
  font-size: 16px;
  overflow-x: scroll;
  width: 100%;
  word-break: keep-all;
  padding: 1em;
  line-height: 1;
  border-radius: 4px 0 0 4px;
  display: inline-block;
  color: #61daff;
  background: #354b5a;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  vertical-align: bottom;
}
.single-line.sandbox {
  position: relative;
  padding-right: 4px;
  border-radius: 4px 0 0 4px;
}
.single-line .sandbox-link {
  background: url("https://assets.imgix.net/presskit/imgix-presskit.pdf?page=1&fm=png8&w=48") no-repeat;
  background-color: #F8510F;
  display: block;
  min-height: 46px;
  border-bottom: solid 2px #ce3f06;
  width: 48px;
  text-indent: -9999px;
  position: absolute;
  right: 0;
  border-radius: 0 4px 4px 0;
}

/* Transparent Grids for PNGs and gifs */
.transparency-dark {
  background: #496070;
  background-image: -moz-linear-gradient(45deg, #354651 25%, transparent 25%), -moz-linear-gradient(-45deg, #354651 25%, transparent 25%), -moz-linear-gradient(45deg, transparent 75%, #354651 75%), -moz-linear-gradient(-45deg, transparent 75%, #354651 75%);
  background-image: -webkit-gradient(linear, 0 100%, 100% 0, color-stop(0.25, #354651), color-stop(0.25, rgba(0, 0, 0, 0))), -webkit-gradient(linear, 0 0, 100% 100%, color-stop(0.25, #354651), color-stop(0.25, rgba(0, 0, 0, 0))), -webkit-gradient(linear, 0 100%, 100% 0, color-stop(0.75, rgba(0, 0, 0, 0)), color-stop(0.75, #354651)), -webkit-gradient(linear, 0 0, 100% 100%, color-stop(0.75, rgba(0, 0, 0, 0)), color-stop(0.75, #354651));
  -moz-background-size: 10px 10px;
  background-size: 10px 10px;
  -webkit-background-size: 10px 10px;
  background-position: 0 0, 5px 0, 5px -5px, 0 5px;
}

.transparency-light {
  background: #efefef;
  background-image: -moz-linear-gradient(45deg, #dfdfdf 25%, transparent 25%), -moz-linear-gradient(-45deg, #dfdfdf 25%, transparent 25%), -moz-linear-gradient(45deg, transparent 75%, #dfdfdf 75%), -moz-linear-gradient(-45deg, transparent 75%, #dfdfdf 75%);
  background-image: -webkit-gradient(linear, 0 100%, 100% 0, color-stop(0.25, #dfdfdf), color-stop(0.25, rgba(0, 0, 0, 0))), -webkit-gradient(linear, 0 0, 100% 100%, color-stop(0.25, #dfdfdf), color-stop(0.25, rgba(0, 0, 0, 0))), -webkit-gradient(linear, 0 100%, 100% 0, color-stop(0.75, rgba(0, 0, 0, 0)), color-stop(0.75, #dfdfdf)), -webkit-gradient(linear, 0 0, 100% 100%, color-stop(0.75, rgba(0, 0, 0, 0)), color-stop(0.75, #dfdfdf));
  -moz-background-size: 10px 10px;
  background-size: 10px 10px;
  -webkit-background-size: 10px 10px;
  background-position: 0 0, 5px 0, 5px -5px, 0 5px;
}

.responsive {
  width: 100%;
  text-align: center;
  padding: 20px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  border-top: solid 10px #00C0FA;
  color: #00C0FA;
  position: relative;
  line-height: 1.4;
  font-weight: 100;
}

.responsive:before {
  content: "⇄";
  position: absolute;
  right: 20px;
}

.responsive:after {
  font-size: 100%;
  vertical-align: baseline;
  font-weight: 400;
}

/* Wider than desktop */
@media (min-width: 1200px) {
  .responsive {
    border-top: solid 10px #00C0FA;
  }

  .responsive:after {
    content: "Large Desktop";
    font-size: 100%;
  }
}
/* Landscape phone to desktop */
@media (max-width: 1199px) {
  .responsive {
    border-top: solid 10px #2ecfff;
  }

  .responsive:after {
    content: "Desktop";
    font-size: 100%;
  }
}
/* Landscape phone to landscape tablet */
@media (max-width: 979px) {
  .responsive {
    border-top: solid 10px #00C0FA;
  }

  .responsive:after {
    content: "Landscape Tablet";
    font-size: 100%;
  }
}
/* Small desktop */
@media (min-width: 980px) and (max-width: 1199px) {
  .responsive:after {
    content: "Small desktop";
    font-size: 100%;
  }
}
/* Portrait tablet to landscape tablet */
@media (min-width: 768px) and (max-width: 979px) {
  .responsive {
    border-top: solid 10px #0099c7;
  }

  .responsive:after {
    content: "Portrait Tablet";
    font-size: 100%;
  }
}
/* Landscape phone to portrait tablet */
@media (max-width: 767px) {
  .responsive {
    font-size: 14px;
    border-top: solid 10px #0099c7;
  }

  .responsive:after {
    content: "Landscape Phone";
    font-size: 100%;
  }
}
@media (max-width: 480px) {
  .responsive {
    font-size: 12px;
    text-align: left;
    border-top: solid 10px #0099c7;
  }

  .responsive:after {
    content: "Portrait Phone";
  }
}
figure {
  text-align: center;
}

picture {
  text-align: center;
}

.demo-area {
  background: #FAFAFA;
  border-radius: 8px;
  padding: 20px;
}
.demo-area section {
  padding-top: 0;
}

.demo-trigger {
  display: inline-block;
  width: 30%;
  float: left;
}

.detail {
  position: relative;
  width: 65%;
  margin-left: 5%;
  float: left;
}
.detail button {
  vertical-align: middle;
  opacity: 0.5;
  cursor: unset;
  background: #7d90a0;
  margin-left: 1em;
}

@media (max-width: 610px) {
  .detail, .demo-trigger {
    float: none;
  }

  .demo-trigger {
    display: block;
    width: 50%;
    max-width: 200px;
    margin: 0 auto;
  }

  .detail {
    margin: 0;
    width: auto;
  }

  p {
    margin: 0 auto 1em;
  }

  .responsive-hint {
    display: none;
  }

  h3 {
    margin-top: 20px;
  }
}

.myRating {
    display: flex;        /* 启用 Flexbox */
    align-items: center;  /* 垂直居中子元素 */
}
.rating {
  margin: auto;
  --bg: #e3e4e8;
  --fg: #17181c;
  --primary: #255ff4;
  --yellow: #f4a825;
  --yellow-t: rgba(244, 168, 37, 0);
  --bezier: cubic-bezier(0.42,0,0.58,1);
  --trans-dur: 0.3s;
  font-size: calc(24px + (30 - 24) * (100vw - 320px) / (1280 - 320));
}
.rating__display {
  font-size: 1em;
  font-weight: 500;
  min-height: 1.25em;
  position: absolute;
  top: 100%;
  width: 100%;
  text-align: center;
}
.rating__stars {
  display: flex;
  padding-bottom: 0.375em;
  position: relative;
  margin-left: 20px;    /* 根据需要给星级评分组件添加左边距 */
}
.rating__star {
  display: block;
  overflow: visible;
  pointer-events: none;
  width: 2em;
  height: 2em;
}
.rating__star-ring, .rating__star-fill, .rating__star-line, .rating__star-stroke {
  animation-duration: 1s;
  animation-timing-function: ease-in-out;
  animation-fill-mode: forwards;
}
.rating__star-ring, .rating__star-fill, .rating__star-line {
  stroke: var(--yellow);
}
.rating__star-fill {
  fill: var(--yellow);
  transform: scale(0);
  transition: fill var(--trans-dur) var(--bezier), transform var(--trans-dur) var(--bezier);
}
.rating__star-line {
  stroke-dasharray: 12 13;
  stroke-dashoffset: -13;
}
.rating__star-stroke {
  stroke: #c7cad1;
  transition: stroke var(--trans-dur);
}
.rating__label {
  cursor: pointer;
  padding: 0.125em;
}
.rating__label--delay1 .rating__star-ring, .rating__label--delay1 .rating__star-fill, .rating__label--delay1 .rating__star-line, .rating__label--delay1 .rating__star-stroke {
  animation-delay: 0.05s;
}
.rating__label--delay2 .rating__star-ring, .rating__label--delay2 .rating__star-fill, .rating__label--delay2 .rating__star-line, .rating__label--delay2 .rating__star-stroke {
  animation-delay: 0.1s;
}
.rating__label--delay3 .rating__star-ring, .rating__label--delay3 .rating__star-fill, .rating__label--delay3 .rating__star-line, .rating__label--delay3 .rating__star-stroke {
  animation-delay: 0.15s;
}
.rating__label--delay4 .rating__star-ring, .rating__label--delay4 .rating__star-fill, .rating__label--delay4 .rating__star-line, .rating__label--delay4 .rating__star-stroke {
  animation-delay: 0.2s;
}
.rating__input {
  position: absolute;
  -webkit-appearance: none;
  appearance: none;
}
.rating__input:hover ~ [data-rating]:not([hidden]) {
  display: none;
}
.rating__input-1:hover ~ [data-rating="1"][hidden], .rating__input-2:hover ~ [data-rating="2"][hidden], .rating__input-3:hover ~ [data-rating="3"][hidden], .rating__input-4:hover ~ [data-rating="4"][hidden], .rating__input-5:hover ~ [data-rating="5"][hidden], .rating__input:checked:hover ~ [data-rating]:not([hidden]) {
  display: block;
}
.rating__input-1:hover ~ .rating__label:first-of-type .rating__star-stroke, .rating__input-2:hover ~ .rating__label:nth-of-type(-n + 2) .rating__star-stroke, .rating__input-3:hover ~ .rating__label:nth-of-type(-n + 3) .rating__star-stroke, .rating__input-4:hover ~ .rating__label:nth-of-type(-n + 4) .rating__star-stroke, .rating__input-5:hover ~ .rating__label:nth-of-type(-n + 5) .rating__star-stroke {
  stroke: var(--yellow);
  transform: scale(1);
}
.rating__input-1:checked ~ .rating__label:first-of-type .rating__star-ring, .rating__input-2:checked ~ .rating__label:nth-of-type(-n + 2) .rating__star-ring, .rating__input-3:checked ~ .rating__label:nth-of-type(-n + 3) .rating__star-ring, .rating__input-4:checked ~ .rating__label:nth-of-type(-n + 4) .rating__star-ring, .rating__input-5:checked ~ .rating__label:nth-of-type(-n + 5) .rating__star-ring {
  animation-name: starRing;
}
.rating__input-1:checked ~ .rating__label:first-of-type .rating__star-stroke, .rating__input-2:checked ~ .rating__label:nth-of-type(-n + 2) .rating__star-stroke, .rating__input-3:checked ~ .rating__label:nth-of-type(-n + 3) .rating__star-stroke, .rating__input-4:checked ~ .rating__label:nth-of-type(-n + 4) .rating__star-stroke, .rating__input-5:checked ~ .rating__label:nth-of-type(-n + 5) .rating__star-stroke {
  animation-name: starStroke;
}
.rating__input-1:checked ~ .rating__label:first-of-type .rating__star-line, .rating__input-2:checked ~ .rating__label:nth-of-type(-n + 2) .rating__star-line, .rating__input-3:checked ~ .rating__label:nth-of-type(-n + 3) .rating__star-line, .rating__input-4:checked ~ .rating__label:nth-of-type(-n + 4) .rating__star-line, .rating__input-5:checked ~ .rating__label:nth-of-type(-n + 5) .rating__star-line {
  animation-name: starLine;
}
.rating__input-1:checked ~ .rating__label:first-of-type .rating__star-fill, .rating__input-2:checked ~ .rating__label:nth-of-type(-n + 2) .rating__star-fill, .rating__input-3:checked ~ .rating__label:nth-of-type(-n + 3) .rating__star-fill, .rating__input-4:checked ~ .rating__label:nth-of-type(-n + 4) .rating__star-fill, .rating__input-5:checked ~ .rating__label:nth-of-type(-n + 5) .rating__star-fill {
  animation-name: starFill;
}
.rating__input-1:not(:checked):hover ~ .rating__label:first-of-type .rating__star-fill, .rating__input-2:not(:checked):hover ~ .rating__label:nth-of-type(2) .rating__star-fill, .rating__input-3:not(:checked):hover ~ .rating__label:nth-of-type(3) .rating__star-fill, .rating__input-4:not(:checked):hover ~ .rating__label:nth-of-type(4) .rating__star-fill, .rating__input-5:not(:checked):hover ~ .rating__label:nth-of-type(5) .rating__star-fill {
  fill: var(--yellow-t);
}
.rating__sr {
  clip: rect(1px, 1px, 1px, 1px);
  overflow: hidden;
  position: absolute;
  width: 1px;
  height: 1px;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg: #17181c;
    --fg: #e3e4e8;
  }

  .rating {
    margin: auto;
  }
  .rating__star-stroke {
    stroke: #454954;
  }
}
@keyframes starRing {
  from, 20% {
    animation-timing-function: ease-in;
    opacity: 1;
    r: 8px;
    stroke-width: 16px;
    transform: scale(0);
  }
  35% {
    animation-timing-function: ease-out;
    opacity: 0.5;
    r: 8px;
    stroke-width: 16px;
    transform: scale(1);
  }
  50%, to {
    opacity: 0;
    r: 16px;
    stroke-width: 0;
    transform: scale(1);
  }
}
@keyframes starFill {
  from, 40% {
    animation-timing-function: ease-out;
    transform: scale(0);
  }
  60% {
    animation-timing-function: ease-in-out;
    transform: scale(1.2);
  }
  80% {
    transform: scale(0.9);
  }
  to {
    transform: scale(1);
  }
}
@keyframes starStroke {
  from {
    transform: scale(1);
  }
  20%, to {
    transform: scale(0);
  }
}
@keyframes starLine {
  from, 40% {
    animation-timing-function: ease-out;
    stroke-dasharray: 1 23;
    stroke-dashoffset: 1;
  }
  60%, to {
    stroke-dasharray: 12 13;
    stroke-dashoffset: -13;
  }
}


.title-row {
    display: flex;
    align-items: center;
}

.fa-heart {
    margin-left: 10px;
    cursor: pointer;
}

.fa-heart.is-favorite {
    color: red; /* 当为收藏状态时，显示为红色 */
}
.fa {
    font-size: 48px; /* 调整图标大小 */
    transition: all 0.3s; /* 添加过渡效果，使变化更平滑 */
}

.fa-heart-o:hover,
.fa-heart:hover {
    transform: scale(1.1); /* 鼠标悬停时放大图标 */
}





.comment-user {
  display: flex;          /* 使用flex布局 */
  justify-content: center; /* 水平居中 */
  align-items: center;     /* 垂直居中 */
  height: 100%;            /* 可以设置为需要的高度 */
}

.comments-section {
  margin: 0 15px;
  position: absolute;
  left: 50%;
  transform: translate(-50%, 0);
  width: 800px;
  margin-bottom: 10%;
}
.comments-section h4 {
  margin: 0;
  margin-top: 40px;
  margin-bottom: 10px;
  font-weight: bold;
  font-size: 1.2rem;
  color: rgb(42, 16, 146);
  border-bottom: 1px solid #666;
  padding-bottom: 5px;
}
.comments-section .comments {
  color: white;
}
.comments-section .comments h4 {
  border: 0;
}
.comments-section .comment {
  background: #05436a;
  padding: 20px;
  font-size: 15px;
  margin-bottom: 20px;
}
.comments-section .comment blockquote {
  color: #eee;
  padding: 1em;
  border-left: 2px solid #76daff;
  background: rgba(0, 0, 0, 0.05);
}
.comments-section .comment code {
  font-family: Menlo, Monaco, monospace;
  background: rgba(0, 0, 0, 0.2);
  padding: 2px 5px;
  margin: 0 2px;
  border-radius: 2px;
}
.comments-section .comment .box {
  background: #1d201f;
  padding: 20px;
}
.comments-section .comment .box pre {
  overflow: auto;
  margin: 0;
}
.comments-section .comment .box pre code {
  background: transparent;
}
.comments-section .comment .box + .box {
  padding-top: 0px;
}
.comments-section .comment a {
  color: #76daff;
  text-decoration: none;
}
.comments-section .comment .comment-user {
  border-bottom: 1px solid #555;
  padding: 10px 45px 20px;
  display: flex;
  align-items: center;
}
.comments-section .comment .comment-user .avatar img {
  width: 35px;
  height: 35px;
}
.comments-section .comment .comment-user .username {
  color: #76daff;
}
.comments-section .comment .comment-user .user-details {
  color: #666;
  margin-left: 10px;
}
.comments-section .comment .comment-user .user-details span:last-child {
  color: #999;
  font-size: 80%;
}
.comments-section .comment .comment-text {
  padding: 10px 45px 20px;
}

/* EDITOR STYLE */
.CodepenCommentEditor-root {
  background: transparent;
  font-family: "Lato", serif;
  font-size: 14px;
}

.CodepenCommentEditor-editor {
  background: #fff;
  border: 3px solid #ccc;
  cursor: text;
  font-size: 13px;
  margin-top: 10px;
  font-family: "Lato";
  transition: all 0.2s ease-in;
}

.CodepenCommentEditor-focus {
  border-color: #555;
}

.CodepenCommentEditor-editor .public-DraftEditorPlaceholder-root,
.CodepenCommentEditor-editor .public-DraftEditor-content {
  padding-left: 5px;
  padding-top: 5px;
}

.CodepenCommentEditor-editor .public-DraftEditor-content {
  min-height: 100px;
}

.CodepenCommentEditor-hidePlaceholder .public-DraftEditorPlaceholder-root {
  display: none;
}

.CodepenCommentEditor-editor .CodepenCommentEditor-blockquote {
  border-left: 2px solid #76daff;
  background-color: rgba(0, 0, 0, 0.05);
  color: #666;
  font-style: italic;
  margin: 16px 0;
  margin-right: 5px;
  padding: 10px 20px;
}

.CodepenCommentEditor-editor .public-DraftStyleDefault-pre {
  margin-right: 5px;
  background-color: rgba(0, 0, 0, 0.05);
  font-family: "Inconsolata", "Menlo", "Consolas", monospace;
  font-size: 16px;
  padding: 20px;
}

.CodepenCommentEditor-controls {
  font-family: "Lato", sans-serif;
  font-size: 12px;
  margin-bottom: 2px;
  -webkit-user-select: none;
     -moz-user-select: none;
      -ms-user-select: none;
          user-select: none;
}

.CodepenCommentEditor-styleButton {
  display: inline-block;
  color: #fff;
  cursor: pointer;
  margin-right: 16px;
  padding: 2px 7px;
  border: 1px solid transparent;
  margin: 0 5px 0 0;
  border-radius: 3px;
  background: #343436;
}

.CodepenCommentEditor-submitButton {
  color: white;
  cursor: pointer;
  float: left;
  margin-top: 5px;
  padding: 10px 16px;
  background: none;
  border: 3px solid #ccc;
  border-radius: 3px;
}
.CodepenCommentEditor-submitButton:hover {
  background: white;
  border-color: white;
  color: black;
}

.CodepenCommentEditor-activeButton {
  background: #4d4d50;
  transform: translateY(1px);
}
</style>