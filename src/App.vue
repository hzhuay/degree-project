<template>
  <div id="app">

<!--      <router-link :to="'/user/'+userId">用户</router-link>-->
<!--      <router-link :to="{path: '/profile', query: {name: 'Jack', age: 18}}"></router-link>-->
<!--      <button @click="jump">跳转</button>-->

    <router-view></router-view>
<!--    footer-->
    <footer class="footer-area">
      <div class="footer-top">
        <div class="container">
          <div class="row">
            <div class="col-md-4">
              <a href="index.html"><img src="assets/img/logo.png" alt="img"></a>
            </div>
            <div class="col-md-8 text-md-right mt-3 mt-md-0">
              <ul class="social-area">
                <li><a href="#"><i class="fab fa-facebook-f" aria-hidden="true"></i></a></li>
                <li><a href="#"><i class="fab fa-twitter" aria-hidden="true"></i></a></li>
                <li><a href="#"><i class="fab fa-instagram" aria-hidden="true"></i></a></li>
                <li><a href="#"><i class="fab fa-skype" aria-hidden="true"></i></a></li>
                <li><a href="#"><i class="fab fa-pinterest-p" aria-hidden="true"></i></a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="footer-middle bg-black">
        <div class="container">
          <div class="row">
            <div class="col-lg-4 col-md-6">
              <div class="widget widget_about">
                <h4 class="widget-title">Company</h4>
                <div class="details">
                  <p>Lorem ipsum dolor sit amet, Lorem ipsum dolor sit amet, consectetur et adipisicing eiusmod tempor incididunt labore</p>
                  <p><i class="fas fa-map-marker-alt"></i> 420 Love Sreet 133/2 Mirpur City, Dhaka</p>
                  <p><i class="fas fa-phone-volume"></i> +(066) 19 5017 800 628</p>
                  <p><i class="fas fa-envelope"></i> <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="355c5b535a1b565a5b41545641755258545c591b565a58">[email&#160;protected]</a></p>
                </div>
              </div>
            </div>
            <div class="col-lg-4 col-md-6">
              <div class="widget widget_newsfeed">
                <h4 class="widget-title">News Feed</h4>
                <ul>
                  <li><a href="#"><i class="far fa-user"></i>By Admin</a><span><i class="far fa-calendar-alt"></i>Marce 9 , 2020</span></li>
                  <li><a href="#"><i class="far fa-user"></i>By Admin</a><span><i class="far fa-calendar-alt"></i>Marce 9 , 2020</span></li>
                  <li><a href="#"><i class="far fa-user"></i>By Admin</a><span><i class="far fa-calendar-alt"></i>Marce 9 , 2020</span></li>
                  <li><a href="#"><i class="far fa-user"></i>By Admin</a><span><i class="far fa-calendar-alt"></i>Marce 9 , 2020</span></li>
                  <li><a href="#"><i class="far fa-user"></i>By Admin</a><span><i class="far fa-calendar-alt"></i>Marce 9 , 2020</span></li>
                </ul>
              </div>
            </div>
            <div class="col-lg-4 col-md-9">
              <div class="widget widget_subscribe mb-4">
                <h4 class="widget-title">Newslatter</h4>
                <div class="details">
                  <p>Lorem ipsum dolor sit amet,</p>
                  <div class="footer-subscribe-inner">
                    <input type="text" placeholder="Your Mail">
                    <a class="btn btn-base" href="#">Subscribe</a>
                  </div>
                </div>
              </div>
              <div class="widget widget-tags pt-2">
                <h5 class="widget-title mb-3">House Tags</h5>
                <div class="tagcloud mt-0">
                  <a href="#">Creative</a>
                  <a href="#">Development</a>
                  <a href="#">Beach</a>
                  <a href="#">Villa</a>
                  <a href="#">Clean</a>
                  <a href="#">Seo</a>
                  <a href="#">Appertment</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="footer-bottom bg-black">
        <div class="container">
          <div class="row">
            <div class="col-md-7 align-self-center">
              <p>©2021, Copy Right By Solverwp. All Rights Reserved</p>
            </div>
            <div class="col-md-5 text-md-right">
              <ul>
                <li>
                  <a href="index.html">Home</a>
                </li>
                <li>
                  <a href="about.html">About</a>
                </li>
                <li>
                  <a href="blog.html">Blog</a>
                </li>
                <li>
                  <a href="contact.html">Contact</a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </footer>

  </div>
</template>

<script>

  export default {
    data() {
      return {
        name: 'Jack',
        userId: 1,
        isfix: false,
        activeIndex: '1',
        input3: '',
        publicPath: process.env.BASE_URL
      }
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  color: #2c3e50;
}


/*.fix-head{*/
/*  background-color: #f6f6f6;*/
/*  position: fixed;*/
/*  top: 0px;*/
/*  width: 100%;*/
/*  height: 10px;*/
/*  z-index: 999;*/
/*}*/


/*.el-menu{*/
/*  height: 40px; width: 100%; position: fixed; top: 0px; left: 0px; right: 0px; background-color: #f6f6f6; z-index: 999*/
/*}*/

/*.el-menu-item{*/
/*  height: 40px !important;*/
/*  line-height: 40px !important;*/
/*}*/
</style>
