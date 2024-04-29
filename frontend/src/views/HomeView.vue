<template>
<div class="background-image">

  <div class="container-fluid parallax">
    <div class="navbar">
      <ul class="nav-list">
        <li><router-link to="/">主页</router-link></li>
        <li><router-link to="/movies">发现</router-link></li>
        <li v-if="isAuthenticated"><router-link to="/logout" @click.prevent="logout">退出</router-link></li>
        <li v-else><router-link to="/login">登录/注册</router-link></li>
      </ul>
    </div>
    
    <div class="heading text-center">
      <h2>The Films of</h2>
      <h1 class="text-uppercase">{{ username }}</h1>
    </div>
  </div>

  <div class="container pb-3 pt-5">
  
    <div class="card-deck">
      <div class="card" v-for="movie in favorites" :key="movie.id">
        <img class="card-img-top img-fluid" :src="movie.cover_image_url" :alt="movie.title">
        <div class="card-block">
          <h4 class="card-title">{{ movie.title }} <small class="text-muted">({{ movie.year }})</small></h4>
          <p class="card-text">{{ movie.description }}</p>
        </div>
        <div class="card-footer">
          <a :href="movie.detail_url" target="_blank" class="card-link">More Info</a>
        </div>
      </div>
    </div>
  </div>

  <div class="comments-section">
    <div class="comments">
      <h4>COMMENTS</h4>
      <div id="comments-container">
        <div class="comment" v-for="comment in comments" :key="comment.movie_id">
          <div class="comment-user">
            <div class="avatar">
              {{ comment.movie_title }}
            </div>
          </div>
          <div class="comment-text">
            {{ comment.comment_text }}
          </div>
        </div>
      </div>
    </div>
    <div class="comment-editor">
      <h4>LEAVE A COMMENT</h4>
      <div id="comment-form"></div>
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
      favorites: [], // 存储收藏的电影列表
      comments: [],
    };
  },
  name: 'HomeView',
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    username() {
      return this.$store.getters.username;
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('logout').then(() => {
        this.$router.push('/login');
      });
    },
    fetchFavorites() {
      this.loading = true;
      const username = this.$store.getters.username;
      axios.get(`http://10.181.91.67:8000/api/favorites/get_favorites/?username=${username}`)
        .then(response => {
          this.favorites = response.data.results;
          this.loading = false;
          console.log('Movie ID:', this.favorites);
        })
        .catch(error => {
          console.error("Failed to load favorites: ", error.message);
          this.loading = false;
        });
    },
    fetchComments() {
      this.loading = true;
      const username = this.$store.getters.username;
      axios.get(`http://10.181.91.67:8000/api/comment/get_comments/?username=${username}`)
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
  },
  mounted() {
    this.fetchFavorites();
    this.fetchComments();
  },
}
</script>

<style>
/* .auth-options button {
  margin: 10px;
  padding: 5px 20px;
} */

.background-image {
  background-image: url('https://wallpapercave.com/wp/wp1906348.png');
  background-size: cover;
  background-position: center;
  height: 100vh; /* 调整高度为视窗高度，或其他值 */
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
