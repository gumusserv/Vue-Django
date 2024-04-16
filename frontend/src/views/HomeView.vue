<template>
<div class="background-image">

  <div class="container-fluid parallax">
    <div class="navbar">
      <ul class="nav-list">
        <li><router-link to="/">主页</router-link></li>
        <li><router-link to="/search">发现</router-link></li>
        <li v-if="isAuthenticated"><router-link to="/logout" @click.prevent="logout">退出</router-link></li>
        <li v-else><router-link to="/login">登录/注册</router-link></li>
      </ul>
    </div>
    
    <div class="heading text-center">
      <h2>The Films of</h2>
      <h1 class="text-uppercase">{{ username }}</h1>
    </div>
  </div>
  
  <div class="container-fluid py-5 bg-faded" id="hm">
    <div class="container">
      <div class="row py-3 pt-1">
        <div class="col-sm-12">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Hayao_Miyazaki_cropped_1_Hayao_Miyazaki_201211.jpg/800px-Hayao_Miyazaki_cropped_1_Hayao_Miyazaki_201211.jpg" class="img-fluid rounded-circle mx-auto d-block" style="max-width: 350px" alt="Hayao Miyazaki">
        </div>
      </div>
      <div class="row py-3">
        <p class="text-center lead">Hayao Miyazaki (宮崎駿, born January 5, 1941) is a Japanese film director, producer, screenwriter, animator, author, manga artist, and co-founder of Studio Ghibli.</p>
      </div>
      <div class="row py-3 pb-1">
        <div class="col-sm-12">
          <img src="https://upload.wikimedia.org/wikipedia/en/thumb/c/ca/Studio_Ghibli_logo.svg/1200px-Studio_Ghibli_logo.svg.png" class="img-fluid mx-auto d-block" style="max-width: 350px" alt="Studio Ghibli logo">
        </div>
      </div>
    </div>
  </div>
  <div class="container-fluid parallax bg-img2">
    <div class="middle">
      <div class="container" style="max-width: 550px">
        <blockquote class="text-center">
          <i class="fa fa-quote-left fa-3x fa-pull-left" aria-hidden="true"></i>
          <p class="mb-1 lead">Many of my movies have strong female leads—brave, self-sufficient girls that don’t think twice about fighting for what they believe in with all their heart. They’ll need a friend, or a supporter, but never a saviour.</p>
          <footer class="blockquote-footer text-uppercase text-white">Hayao Miyazaki</footer>
        </blockquote>
      </div>
    </div>
  </div>

  <div class="container pb-3 pt-5">
    <div class="card-deck">
      <div class="card">
        <img class="card-img-top img-fluid" src="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/yp8vEZflGynlEylxEesbYasc06i.jpg" alt="Ponyo (2008)">
        <div class="card-block">
          <h4 class="card-title">Ponyo <small class="text-muted">(2008)</small></h4>
          <p class="card-text">Inspired by the Hans Christian Andersen story, <cite>The Little Mermaid</cite>, the film centers on a goldfish named Ponyo who befriends a five-year-old human boy, Sōsuke, and wants to become a human girl. (From <a href="https://en.wikipedia.org/wiki/Ponyo" target="_blank" class="card-link"><cite>Wikipedia</cite></a>)</p>
        </div>
        <div class="card-footer">
          <a href="https://www.themoviedb.org/movie/12429" target="_blank" class="card-link">The Movie DB</a>
        </div>
      </div>
      <div class="card">
        <img class="card-img-top img-fluid" src="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/jfwSexzlIzaOgxP9A8bTA6t8YYb.jpg" alt="The Wind Rises (2013)">
        <div class="card-block">
          <h4 class="card-title">The Wind Rises <small class="text-muted">(2013)</small></h4>
          <p class="card-text"><cite>The Wind Rises</cite> is a fictionalized biopic of Jiro Horikoshi (1903–1982), designer of the Mitsubishi A5M fighter aircraft and its successor, the Mitsubishi A6M Zero, used by the Empire of Japan during World War II. The film is adapted from Miyazaki’s manga of the same name, which was in turn loosely based on the 1937 short story The Wind Has Risen by Tatsuo Hori. (From <a href=" https://en.wikipedia.org/wiki/The_Wind_Rises" target="_blank" class="card-link"><cite>Wikipedia</cite></a>)</p>
        </div>
        <div class="card-footer">
          <a href="https://www.themoviedb.org/movie/149870-kaze-tachinu" target="_blank" class="card-link">The Movie DB</a>
        </div>
      </div>
    </div>
    <div class="card-deck">
      <div class="card" style="cursor:pointer;" onclick="location.href='/favorites';" id = "emptyCard">
        <img class="card-img-top img-fluid" src="path_to_placeholder_image.jpg" alt="空白卡片图片">
        <div class="card-block">
            <h4 class="card-title">点击搜索电影</h4>
            <p class="card-text">点击这里搜索您感兴趣的电影。</p>
        </div>
        <div class="card-footer">
            <a href="/favorites" class="card-link">搜索</a>
        </div>
      </div>
      <div class="card" style="cursor:pointer;" onclick="location.href='/favorites';">
        <img class="card-img-top img-fluid" src="path_to_placeholder_image.jpg" alt="空白卡片图片">
        <div class="card-block">
            <h4 class="card-title">点击搜索电影</h4>
            <p class="card-text">点击这里搜索您感兴趣的电影。</p>
        </div>
        <div class="card-footer">
            <a href="/favorites" class="card-link">搜索</a>
        </div>
      </div>
    </div>
  
    <div class="row my-4">
      <div class="col-sm-12 text-center">
        <a href="https://en.wikipedia.org/wiki/Works_of_Hayao_Miyazaki" target="_blank" class="btn btn-info">More works of Hayao Miyazaki</a>
      </div>
    </div>
    <hr>
    <footer class="text-center">
      <p><i class="fa fa-code fa-1x" aria-hidden="true"></i> by <a href="https://codepen.io/rchoi01/" target="_blank" class="card-link">Rachel</a></p>
    </footer>

  </div>



</div>


</template>


<script>
export default {
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
    }
  }
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



</style>
