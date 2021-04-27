<template>
  <div class="home">
<!--    <img alt="Vue logo" src="../assets/logo.png">-->
<!--    <HelloWorld msg="Welcome to Your Vue.js App"/>-->
<!--    <button @click="search(0)">start</button>-->
<!--    <button @click="write">write</button>-->



    <div class="body-overlay" id="body-overlay"></div>
    <div class="td-search-popup" id="td-search-popup">
      <form action="index.html" class="search-form">
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Search.....">
        </div>
        <button type="submit" class="submit-btn"><i class="fa fa-search"></i></button>
      </form>
    </div>

    <div class="navbar-area navbar-area-1">
      <div class="navbar-top">
        <div class="container">
          <div class="row">
            <div class="col-lg-8 text-lg-left text-center">
              <ul>
                <li><p><img src="../assets/img/icon/location.png" alt="img"> 420 Love Sreet 133/2 flx City</p></li>
                <li><p><img src="../assets/img/icon/phone.png" alt="img"> +(06) 017 800 628</p></li>
                <li><p><img src="../assets/img/icon/envelope.png" alt="img"> <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="fe97909891d09d91908a9f9d8abe99939f9792d09d9193">[email&#160;protected]</a></p></li>
              </ul>
            </div>
            <div class="col-lg-4">
              <ul class="topbar-right text-lg-right text-center">
                <li>
                  <a class="ml-0" href="signup.html">Register</a>
                  <a href="signin.html">Login</a>
                </li>
                <li class="social-area">
                  <a href="#"><i class="fab fa-facebook-f" aria-hidden="true"></i></a>
                  <a href="#"><i class="fab fa-twitter" aria-hidden="true"></i></a>
                  <a href="#"><i class="fab fa-instagram" aria-hidden="true"></i></a>
                  <a href="#"><i class="fab fa-skype" aria-hidden="true"></i></a>
                  <a href="#"><i class="fab fa-pinterest-p" aria-hidden="true"></i></a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <nav class="navbar navbar-expand-lg">
        <div class="container nav-container">
          <div class="responsive-mobile-menu">
            <button class="menu toggle-btn d-block d-lg-none" data-target="#dkt_main_menu" aria-expanded="false" aria-label="Toggle navigation">
              <span class="icon-left"></span>
              <span class="icon-right"></span>
            </button>
          </div>
          <div class="logo">
            <a href="index.html"><img src="../assets/img/logo.png" alt="img"></a>
          </div>
          <div class="nav-right-part nav-right-part-mobile">
            <ul>
              <li><a class="search" href="#"><i class="fa fa-search"></i></a></li>
              <li><a class="btn btn-base" href="add-property.html"><span class="btn-icon"><i class="fa fa-plus"></i></span> <span class="btn-text">SUBMIT PROPERTY</span></a></li>
            </ul>
          </div>
          <div class="collapse navbar-collapse" id="dkt_main_menu">
            <ul class="navbar-nav menu-open text-center">
              <li class="menu-item-has-children current-menu-item">
                <a href="#">Home</a>
                <ul class="sub-menu">
                  <li><router-link to="/">Home</router-link></li>
                  <li><router-link to="/about">Predict</router-link></li>
                  <li><router-link to="/list">List</router-link></li>
                  <li><router-link to="/test">Test</router-link></li>
                </ul>
              </li>
              <li class="menu-item-has-children current-menu-item">
                <a href="#">Property</a>
                <ul class="sub-menu">
                  <li><a href="property.html">Property</a></li>
                  <li><a href="property-grid.html">Property Grid</a></li>
                  <li><a href="property-left-sidebar.html">Left Sidebar</a></li>
                  <li><a href="property-details.html">Property Details</a></li>
                </ul>
              </li>
              <li class="menu-item-has-children current-menu-item">
                <a href="#">Pages</a>
                <ul class="sub-menu">
                  <li><a href="about.html">About</a></li>
                  <li><a href="team.html">Team</a></li>
                  <li><a href="signin.html">Sign In</a></li>
                  <li><a href="signup.html">Sign Up</a></li>
                  <li><a href="add-property.html">Add Property</a></li>
                </ul>
              </li>
              <li class="menu-item-has-children current-menu-item">
                <a href="#">Blog</a>
                <ul class="sub-menu">
                  <li><a href="blog.html">Blog</a></li>
                  <li><a href="blog-grid.html">Blog Grid</a></li>
                  <li><a href="blog-left-sidebar.html">Left Sidebar</a></li>
                  <li><a href="blog-details.html">Blog Details</a></li>
                  <li><a href="blog-details-left-sidebar.html">Details Left Sidebar</a></li>
                </ul>
              </li>
              <li><a href="contact.html">Contact</a></li>
            </ul>
          </div>
          <div class="nav-right-part nav-right-part-desktop">
            <ul>
              <li><a class="search" href="#"><i class="fa fa-search"></i></a></li>
              <li><a class="btn btn-base" href="add-property.html"><span class="btn-icon"><i class="fa fa-plus"></i></span> <span class="btn-text">SUBMIT PROPERTY</span></a></li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
    <div class="banner-area banner-area-1 banner-area-bg" style="background: url('../assets/img/banner/1.png');">
      <div class="container">
        <div class="banner-area-inner">
          <div class="row justify-content-center">
            <div class="col-lg-8">
              <div class="banner-inner text-center">
                <p>Lorem ipsum dolor sit amet, consecteLorem ipsum dolor sit amet,</p>
                <div class="line"></div>
                <h2>The Best Way To Find Your Perfect Home</h2>
              </div>
            </div>

            <div class="col-lg-8 mt-4" style="display: none">
              <form class="main-search-inner">
                <div class="row custom-gutters-10">
                  <div class="col-md-3">
                    <el-select v-model="value" placeholder="请选择" class="home-select">
                      <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                      </el-option>
                    </el-select>
                  </div>
                  <div class="col-md-3">
                    <el-select v-model="value" placeholder="请选择" class="home-select">
                      <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                      </el-option>
                    </el-select>
                  </div>
                  <div class="col-md-3">
                    <el-select v-model="value" placeholder="请选择" class="home-select">
                      <el-option
                        v-for="item in options"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                      </el-option>
                    </el-select>
                  </div>
                  <div class="col-md-3">
                    <a class="btn btn-base w-100" href="#"><i class="fa fa-search mr-1"></i> Search</a>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="service-area">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-4 col-md-10">
            <div class="single-service-wrap">
              <div class="thumb">
                <img src="../assets/img/service/1.png" alt="icon">
              </div>
              <div class="single-service-details">
                <h4><a href="property-details.html">Sell Poparty</a></h4>
                <p>Lorem ipsum dolor sit consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore.</p>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-10">
            <div class="single-service-wrap">
              <div class="thumb">
                <img src="../assets/img/service/2.png" alt="icon">
              </div>
              <div class="single-service-details">
                <h4><a href="property-details.html">Daily Apartment</a></h4>
                <p>Lorem ipsum dolor sit consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore.</p>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-10">
            <div class="single-service-wrap mb-0">
              <div class="thumb">
                <img src="../assets/img/service/3.png" alt="icon">
              </div>
              <div class="single-service-details">
                <h4><a href="property-details.html">Family House</a></h4>
                <p>Lorem ipsum dolor sit consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="product-area pd-top-118 pd-bottom-90">
      <div class="container">
        <div class="section-title text-center">
          <h6>We are offring the best real estate</h6>
          <h2>Best House For You</h2>
        </div>
        <div class="row justify-content-center">
          <div class="col-lg-4 col-md-6">
            <div class="single-product-wrap">
              <div class="thumb">
                <img src="../assets/img/product/1.png" alt="img">
                <a class="cat" href="property-details.html">For Sell</a>
              </div>
              <div class="product-wrap-details">
                <div class="media">
                  <div class="author">
                    <img src="../assets/img/author/1.png" alt="img">
                  </div>
                  <div class="media-body">
                    <h6><a href="#">Owner Name</a></h6>
                    <p><img src="../assets/img/icon/location-alt.png" alt="img">New York real estate </p>
                  </div>
                  <a class="fav-btn float-right" href="#"><i class="far fa-heart"></i></a>
                </div>
                <div class="product-meta">
                  <span class="price">$ 80,650.00</span>
                  <div class="float-right d-inline-block">
                    <ul>
                      <li><img src="../assets/img/icon/triangle.png" alt="img">2</li>
                      <li><img src="../assets/img/icon/bed.png" alt="img">3</li>
                      <li><img src="../assets/img/icon/wall.png" alt="img">1026 sq ft</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6">
            <div class="single-product-wrap">
              <div class="thumb">
                <img src="../assets/img/product/2.png" alt="img">
                <a class="cat" href="property-details.html">For Sell</a>
              </div>
              <div class="product-wrap-details">
                <div class="media">
                  <div class="author">
                    <img src="../assets/img/author/2.png" alt="img">
                  </div>
                  <div class="media-body">
                    <h6><a href="#">Owner Name</a></h6>
                    <p><img src="../assets/img/icon/location-alt.png" alt="img">New York real estate </p>
                  </div>
                  <a class="fav-btn float-right" href="#"><i class="far fa-heart"></i></a>
                </div>
                <div class="product-meta">
                  <span class="price">$ 80,650.00</span>
                  <div class="float-right d-inline-block">
                    <ul>
                      <li><img src="../assets/img/icon/triangle.png" alt="img">2</li>
                      <li><img src="../assets/img/icon/bed.png" alt="img">3</li>
                      <li><img src="../assets/img/icon/wall.png" alt="img">1026 sq ft</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6">
            <div class="single-product-wrap">
              <div class="thumb">
                <img src="../assets/img/product/3.png" alt="img">
                <a class="cat" href="property-details.html">For Sell</a>
              </div>
              <div class="product-wrap-details">
                <div class="media">
                  <div class="author">
                    <img src="../assets/img/author/3.png" alt="img">
                  </div>
                  <div class="media-body">
                    <h6><a href="#">Owner Name</a></h6>
                    <p><img src="../assets/img/icon/location-alt.png" alt="img">New York real estate </p>
                  </div>
                  <a class="fav-btn float-right" href="#"><i class="far fa-heart"></i></a>
                </div>
                <div class="product-meta">
                  <span class="price">$ 80,650.00</span>
                  <div class="float-right d-inline-block">
                    <ul>
                      <li><img src="../assets/img/icon/triangle.png" alt="img">2</li>
                      <li><img src="../assets/img/icon/bed.png" alt="img">3</li>
                      <li><img src="../assets/img/icon/wall.png" alt="img">1026 sq ft</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="video-area bg-overlay">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-xl-8 col-lg-10">
            <div class="section-title text-center">
              <h2>The Mordan House Video</h2>
              <p>Lorem ipsum dolor amet, consectetur adipisicing elit Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
              <a class="play-btn" href="https://www.youtube.com/embed/Wimkqo8gDZ0" data-effect="mfp-zoom-in"><i class="fa fa-play"></i></a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="product-area pd-top-118 pd-bottom-90">
      <div class="container">
        <div class="section-title text-center">
          <h6>We are offring the best real estate</h6>
          <h2>Populer Categores</h2>
        </div>
        <div class="row">
          <div class="col-lg-4 col-md-6">
            <div class="single-category-product-wrap">
              <div class="thumb">
                <img src="../assets/img/product/cat-1.png" alt="img">
              </div>
              <div class="single-category-product-details">
                <h4><a href="property-details.html">Orchard</a></h4>
                <a class="btn btn-base" href="property.html">3 Porparties</a>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6">
            <div class="single-category-product-wrap">
              <div class="thumb">
                <img src="../assets/img/product/cat-2.png" alt="img">
              </div>
              <div class="single-category-product-details">
                <h4><a href="property-details.html">Rose Cottage</a></h4>
                <a class="btn btn-base" href="property.html">6 Porparties</a>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6">
            <div class="single-category-product-wrap">
              <div class="thumb">
                <img src="../assets/img/product/cat-3.png" alt="img">
              </div>
              <div class="single-category-product-details">
                <h4><a href="property-details.html">Ong Barn</a></h4>
                <a class="btn btn-base" href="property.html">2 Porparties</a>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6 order-lg-12">
            <div class="single-category-product-wrap">
              <div class="thumb">
                <img src="../assets/img/product/cat-5.png" alt="img">
              </div>
              <div class="single-category-product-details">
                <h4><a href="property-details.html">Family House</a></h4>
                <a class="btn btn-base" href="property.html">1 Porparties</a>
              </div>
            </div>
          </div>
          <div class="col-lg-8 order-lg-1">
            <div class="single-category-product-wrap">
              <div class="thumb">
                <img src="../assets/img/product/cat-4.png" alt="img">
              </div>
              <div class="single-category-product-details">
                <h4><a href="property-details.html">Beach House</a></h4>
                <a class="btn btn-base" href="property.html">7 Porparties</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="testimonial-area pd-top-118 pd-bottom-120 bg-overlay" style="background: url('../assets/img/bg/2.png');">
      <div class="bg-overlay-wrap">
        <div class="section-title style-white text-center">
          <h6>Our Testomonial </h6>
          <h2>What Client Say</h2>
          <p>Lorem ipsum dolor amet, consectetur adipisicing elit Lorem ipsum dolor sit amet, </p>
        </div>
        <div class="container">
          <div class="row justify-content-center">
            <div class="col-lg-10">
              <div class="testimonial-slider-1 owl-carousel">
                <div class="item">
                  <div class="single-testimonial-inner style-two text-center">
                    <div class="thumb main-thumb">
                      <img src="../assets/img/testimonial/1.png" alt="img">
                    </div>
                    <div class="details">
                      <h6 class="name">Sarif Jaya Miprut</h6>
                      <p>“consecte Lorem ipsum dolor sit amet, Lorem ipsum dolor amet, consecte Lorem ipsum dolor sit adipisicing amet, consectetur sed do eiusmod tempor incididunt dolore magna consecrem adipisicing ipsum dolor sit amet, consectetur elit,’’ </p>
                      <div class="rating-inner">
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="far fa-star" aria-hidden="true"></i>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="item">
                  <div class="single-testimonial-inner style-two text-center">
                    <div class="thumb main-thumb">
                      <img src="../assets/img/testimonial/4.png" alt="img">
                    </div>
                    <div class="details">
                      <h6 class="name">Sarif Jaya Miprut</h6>
                      <p>“consecte Lorem ipsum dolor sit amet, Lorem ipsum dolor amet, consecte Lorem ipsum dolor sit adipisicing amet, consectetur sed do eiusmod tempor incididunt dolore magna consecrem adipisicing ipsum dolor sit amet, consectetur elit,’’ </p>
                      <div class="rating-inner">
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="far fa-star" aria-hidden="true"></i>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="propartes-area pd-top-118 pd-bottom-90">
      <div class="container">
        <div class="section-title text-center">
          <h6>Our Propartes</h6>
          <h2>Our Propartes </h2>
        </div>
        <div class="mgd-tab-inner text-center">
          <ul class="nav nav-tabs" id="myTab" role="tablist">
            <li class="nav-item">
              <a class="nav-link active" id="rent1-tab" data-toggle="tab" href="#rent1" role="tab" aria-controls="rent1" aria-selected="true">Rent</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" id="sell1-tab" data-toggle="tab" href="#sell1" role="tab" aria-controls="sell1" aria-selected="false">Sell</a>
            </li>
          </ul>
        </div>
        <div class="tab-content" id="myTabContent">
          <div class="tab-pane fade show active" id="rent1" role="tabpanel" aria-labelledby="rent1-tab">
            <div class="row">
              <div class="col-lg-4 col-md-6">
                <div class="single-product-wrap style-bottom">
                  <div class="thumb">
                    <img src="../assets/img/project/1.png" alt="img">
                    <div class="product-wrap-details">
                      <div class="media">
                        <div class="author">
                          <img src="../assets/img/author/1.png" alt="img">
                        </div>
                        <div class="media-body">
                          <h6><a href="#">Owner Name</a></h6>
                          <p><img src="../assets/img/icon/location-alt.png" alt="img">New York real estate </p>
                        </div>
                        <a class="fav-btn float-right" href="#"><i class="far fa-heart"></i></a>
                      </div>
                    </div>
                  </div>
                  <div class="product-details-inner">
                    <h4><a href="property-details.html">Daily Apartment</a></h4>
                    <ul class="meta-inner">
                      <li><img src="../assets/img/icon/location2.png" alt="img">New York</li>
                      <li><a href="#">For Sell</a></li>
                    </ul>
                    <p>Lorem ipsum dolor consectetur iicing elit, sed do eius Lorem ipsum dolo amet, costur adipisicing eiusmod.</p>
                  </div>
                  <div class="product-meta-bottom">
                    <span class="price">$ 80,650.00</span>
                    <span>For sale</span>
                    <span>1 year ago</span>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6">
                <div class="single-product-wrap style-bottom">
                  <div class="thumb">
                    <img src="../assets/img/project/2.png" alt="img">
                    <div class="product-wrap-details">
                      <div class="media">
                        <div class="author">
                          <img src="../assets/img/author/2.png" alt="img">
                        </div>
                        <div class="media-body">
                          <h6><a href="#">Owner Name</a></h6>
                          <p><img src="../assets/img/icon/location-alt.png" alt="img">New York real estate </p>
                        </div>
                        <a class="fav-btn float-right" href="#"><i class="far fa-heart"></i></a>
                      </div>
                    </div>
                  </div>
                  <div class="product-details-inner">
                    <h4><a href="property-details.html">Gorgeous Villa</a></h4>
                    <ul class="meta-inner">
                      <li><img src="../assets/img/icon/location2.png" alt="img">New York</li>
                      <li><a href="#">For Sell</a></li>
                    </ul>
                    <p>Lorem ipsum dolor consectetur iicing elit, sed do eius Lorem ipsum dolo amet, costur adipisicing eiusmod.</p>
                  </div>
                  <div class="product-meta-bottom">
                    <span class="price">$ 80,650.00</span>
                    <span>For sale</span>
                    <span>1 year ago</span>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6">
                <div class="single-product-wrap style-bottom">
                  <div class="thumb">
                    <img src="../assets/img/project/3.png" alt="img">
                    <div class="product-wrap-details">
                      <div class="media">
                        <div class="author">
                          <img src="../assets/img/author/3.png" alt="img">
                        </div>
                        <div class="media-body">
                          <h6><a href="#">Owner Name</a></h6>
                          <p><img src="../assets/img/icon/location-alt.png" alt="img">New York real estate </p>
                        </div>
                        <a class="fav-btn float-right" href="#"><i class="far fa-heart"></i></a>
                      </div>
                    </div>
                  </div>
                  <div class="product-details-inner">
                    <h4><a href="property-details.html">Daily Property</a></h4>
                    <ul class="meta-inner">
                      <li><img src="../assets/img/icon/location2.png" alt="img">New York</li>
                      <li><a href="#">For Sell</a></li>
                    </ul>
                    <p>Lorem ipsum dolor consectetur iicing elit, sed do eius Lorem ipsum dolo amet, costur adipisicing eiusmod.</p>
                  </div>
                  <div class="product-meta-bottom">
                    <span class="price">$ 80,650.00</span>
                    <span>For sale</span>
                    <span>1 year ago</span>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6">
                <div class="single-product-wrap style-bottom">
                  <div class="thumb">
                    <img src="../assets/img/project/4.png" alt="img">
                    <div class="product-wrap-details">
                      <div class="media">
                        <div class="author">
                          <img src="../assets/img/author/4.png" alt="img">
                        </div>
                        <div class="media-body">
                          <h6><a href="#">Owner Name</a></h6>
                          <p><img src="../assets/img/icon/location-alt.png" alt="img">New York real estate </p>
                        </div>
                        <a class="fav-btn float-right" href="#"><i class="far fa-heart"></i></a>
                      </div>
                    </div>
                  </div>
                  <div class="product-details-inner">
                    <h4><a href="property-details.html">Farm House</a></h4>
                    <ul class="meta-inner">
                      <li><img src="../assets/img/icon/location2.png" alt="img">New York</li>
                      <li><a href="#">For Sell</a></li>
                    </ul>
                    <p>Lorem ipsum dolor consectetur iicing elit, sed do eius Lorem ipsum dolo amet, costur adipisicing eiusmod.</p>
                  </div>
                  <div class="product-meta-bottom">
                    <span class="price">$ 80,650.00</span>
                    <span>For sale</span>
                    <span>1 year ago</span>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6">
                <div class="single-product-wrap style-bottom">
                  <div class="thumb">
                    <img src="../assets/img/project/5.png" alt="img">
                    <div class="product-wrap-details">
                      <div class="media">
                        <div class="author">
                          <img src="../assets/img/author/5.png" alt="img">
                        </div>
                        <div class="media-body">
                          <h6><a href="#">Owner Name</a></h6>
                          <p><img src="../assets/img/icon/location-alt.png" alt="img">New York real estate </p>
                        </div>
                        <a class="fav-btn float-right" href="#"><i class="far fa-heart"></i></a>
                      </div>
                    </div>
                  </div>
                  <div class="product-details-inner">
                    <h4><a href="property-details.html">Beach Side House</a></h4>
                    <ul class="meta-inner">
                      <li><img src="../assets/img/icon/location2.png" alt="img">New York</li>
                      <li><a href="#">For Sell</a></li>
                    </ul>
                    <p>Lorem ipsum dolor consectetur iicing elit, sed do eius Lorem ipsum dolo amet, costur adipisicing eiusmod.</p>
                  </div>
                  <div class="product-meta-bottom">
                    <span class="price">$ 80,650.00</span>
                    <span>For sale</span>
                    <span>1 year ago</span>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6">
                <div class="single-product-wrap style-bottom">
                  <div class="thumb">
                    <img src="../assets/img/project/6.png" alt="img">
                    <div class="product-wrap-details">
                      <div class="media">
                        <div class="author">
                          <img src="../assets/img/author/6.png" alt="img">
                        </div>
                        <div class="media-body">
                          <h6><a href="#">Owner Name</a></h6>
                          <p><img src="../assets/img/icon/location-alt.png" alt="img">New York real estate </p>
                        </div>
                        <a class="fav-btn float-right" href="#"><i class="far fa-heart"></i></a>
                      </div>
                    </div>
                  </div>
                  <div class="product-details-inner">
                    <h4><a href="property-details.html">Gorgeous Hotel</a></h4>
                    <ul class="meta-inner">
                      <li><img src="../assets/img/icon/location2.png" alt="img">New York</li>
                      <li><a href="#">For Sell</a></li>
                    </ul>
                    <p>Lorem ipsum dolor consectetur iicing elit, sed do eius Lorem ipsum dolo amet, costur adipisicing eiusmod.</p>
                  </div>
                  <div class="product-meta-bottom">
                    <span class="price">$ 80,650.00</span>
                    <span>For sale</span>
                    <span>1 year ago</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="tab-pane fade" id="sell1" role="tabpanel" aria-labelledby="sell1-tab">
            <div class="row">
              <div class="col-lg-4 col-md-6">
                <div class="single-product-wrap style-bottom">
                  <div class="thumb">
                    <img src="../assets/img/project/4.png" alt="img">
                    <div class="product-wrap-details">
                      <div class="media">
                        <div class="author">
                          <img src="../assets/img/author/4.png" alt="img">
                        </div>
                        <div class="media-body">
                          <h6><a href="#">Owner Name</a></h6>
                          <p><img src="../assets/img/icon/location-alt.png" alt="img">New York real estate </p>
                        </div>
                        <a class="fav-btn float-right" href="#"><i class="far fa-heart"></i></a>
                      </div>
                    </div>
                  </div>
                  <div class="product-details-inner">
                    <h4><a href="property-details.html">Farm House</a></h4>
                    <ul class="meta-inner">
                      <li><img src="../assets/img/icon/location2.png" alt="img">New York</li>
                      <li><a href="#">For Sell</a></li>
                    </ul>
                    <p>Lorem ipsum dolor consectetur iicing elit, sed do eius Lorem ipsum dolo amet, costur adipisicing eiusmod.</p>
                  </div>
                  <div class="product-meta-bottom">
                    <span class="price">$ 80,650.00</span>
                    <span>For sale</span>
                    <span>1 year ago</span>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6">
                <div class="single-product-wrap style-bottom">
                  <div class="thumb">
                    <img src="../assets/img/project/5.png" alt="img">
                    <div class="product-wrap-details">
                      <div class="media">
                        <div class="author">
                          <img src="../assets/img/author/5.png" alt="img">
                        </div>
                        <div class="media-body">
                          <h6><a href="#">Owner Name</a></h6>
                          <p><img src="../assets/img/icon/location-alt.png" alt="img">New York real estate </p>
                        </div>
                        <a class="fav-btn float-right" href="#"><i class="far fa-heart"></i></a>
                      </div>
                    </div>
                  </div>
                  <div class="product-details-inner">
                    <h4><a href="property-details.html">Beach Side House</a></h4>
                    <ul class="meta-inner">
                      <li><img src="../assets/img/icon/location2.png" alt="img">New York</li>
                      <li><a href="#">For Sell</a></li>
                    </ul>
                    <p>Lorem ipsum dolor consectetur iicing elit, sed do eius Lorem ipsum dolo amet, costur adipisicing eiusmod.</p>
                  </div>
                  <div class="product-meta-bottom">
                    <span class="price">$ 80,650.00</span>
                    <span>For sale</span>
                    <span>1 year ago</span>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6">
                <div class="single-product-wrap style-bottom">
                  <div class="thumb">
                    <img src="../assets/img/project/6.png" alt="img">
                    <div class="product-wrap-details">
                      <div class="media">
                        <div class="author">
                          <img src="../assets/img/author/6.png" alt="img">
                        </div>
                        <div class="media-body">
                          <h6><a href="#">Owner Name</a></h6>
                          <p><img src="../assets/img/icon/location-alt.png" alt="img">New York real estate </p>
                        </div>
                        <a class="fav-btn float-right" href="#"><i class="far fa-heart"></i></a>
                      </div>
                    </div>
                  </div>
                  <div class="product-details-inner">
                    <h4><a href="property-details.html">Gorgeous Hotel</a></h4>
                    <ul class="meta-inner">
                      <li><img src="../assets/img/icon/location2.png" alt="img">New York</li>
                      <li><a href="#">For Sell</a></li>
                    </ul>
                    <p>Lorem ipsum dolor consectetur iicing elit, sed do eius Lorem ipsum dolo amet, costur adipisicing eiusmod.</p>
                  </div>
                  <div class="product-meta-bottom">
                    <span class="price">$ 80,650.00</span>
                    <span>For sale</span>
                    <span>1 year ago</span>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6">
                <div class="single-product-wrap style-bottom">
                  <div class="thumb">
                    <img src="../assets/img/project/1.png" alt="img">
                    <div class="product-wrap-details">
                      <div class="media">
                        <div class="author">
                          <img src="../assets/img/author/1.png" alt="img">
                        </div>
                        <div class="media-body">
                          <h6><a href="#">Owner Name</a></h6>
                          <p><img src="../assets/img/icon/location-alt.png" alt="img">New York real estate </p>
                        </div>
                        <a class="fav-btn float-right" href="#"><i class="far fa-heart"></i></a>
                      </div>
                    </div>
                  </div>
                  <div class="product-details-inner">
                    <h4><a href="property-details.html">Daily Apartment</a></h4>
                    <ul class="meta-inner">
                      <li><img src="../assets/img/icon/location2.png" alt="img">New York</li>
                      <li><a href="#">For Sell</a></li>
                    </ul>
                    <p>Lorem ipsum dolor consectetur iicing elit, sed do eius Lorem ipsum dolo amet, costur adipisicing eiusmod.</p>
                  </div>
                  <div class="product-meta-bottom">
                    <span class="price">$ 80,650.00</span>
                    <span>For sale</span>
                    <span>1 year ago</span>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6">
                <div class="single-product-wrap style-bottom">
                  <div class="thumb">
                    <img src="../assets/img/project/2.png" alt="img">
                    <div class="product-wrap-details">
                      <div class="media">
                        <div class="author">
                          <img src="../assets/img/author/2.png" alt="img">
                        </div>
                        <div class="media-body">
                          <h6><a href="#">Owner Name</a></h6>
                          <p><img src="../assets/img/icon/location-alt.png" alt="img">New York real estate </p>
                        </div>
                        <a class="fav-btn float-right" href="#"><i class="far fa-heart"></i></a>
                      </div>
                    </div>
                  </div>
                  <div class="product-details-inner">
                    <h4><a href="property-details.html">Gorgeous Villa</a></h4>
                    <ul class="meta-inner">
                      <li><img src="../assets/img/icon/location2.png" alt="img">New York</li>
                      <li><a href="#">For Sell</a></li>
                    </ul>
                    <p>Lorem ipsum dolor consectetur iicing elit, sed do eius Lorem ipsum dolo amet, costur adipisicing eiusmod.</p>
                  </div>
                  <div class="product-meta-bottom">
                    <span class="price">$ 80,650.00</span>
                    <span>For sale</span>
                    <span>1 year ago</span>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6">
                <div class="single-product-wrap style-bottom">
                  <div class="thumb">
                    <img src="../assets/img/project/3.png" alt="img">
                    <div class="product-wrap-details">
                      <div class="media">
                        <div class="author">
                          <img src="../assets/img/author/3.png" alt="img">
                        </div>
                        <div class="media-body">
                          <h6><a href="#">Owner Name</a></h6>
                          <p><img src="../assets/img/icon/location-alt.png" alt="img">New York real estate </p>
                        </div>
                        <a class="fav-btn float-right" href="#"><i class="far fa-heart"></i></a>
                      </div>
                    </div>
                  </div>
                  <div class="product-details-inner">
                    <h4><a href="property-details.html">Daily Property</a></h4>
                    <ul class="meta-inner">
                      <li><img src="../assets/img/icon/location2.png" alt="img">New York</li>
                      <li><a href="#">For Sell</a></li>
                    </ul>
                    <p>Lorem ipsum dolor consectetur iicing elit, sed do eius Lorem ipsum dolo amet, costur adipisicing eiusmod.</p>
                  </div>
                  <div class="product-meta-bottom">
                    <span class="price">$ 80,650.00</span>
                    <span>For sale</span>
                    <span>1 year ago</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="cta-area bg-overlay pd-top-118 pd-bottom-120 text-center" style="background: url(assets/img/other/1.png);">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-xl-8 col-lg-10">
            <div class="section-title style-white mb-0">
              <h6>Buy Or Sell</h6>
              <h2>Submit Property</h2>
              <p>consecte Lorem ipsum dolor sit amet, Lorem ipsum dolor amet, consecte Lorem ipsum dolor sit adipisicing amet, consectetur sed do eiusmod tempor incididunt dolore magna consecrem adipisicing ipsum dolor sit amet, consectetur elit,</p>
            </div>
            <div class="btn-wrap mt-4 pt-3">
              <a class="btn btn-base mr-2" href="add-property.html">SUBMIT</a>
              <a class="btn btn-base ml-2" href="property-details.html">BUY NOW</a>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="agent-area text-center pd-top-118 pd-bottom-90">
      <div class="container">
        <div class="section-title text-center">
          <h6>Meet Our Agent</h6>
          <h2>Our Best Agent</h2>
        </div>
        <div class="row justify-content-center">
          <div class="col-lg-4 col-md-6">
            <div class="single-agent-wrap">
              <div class="thumb">
                <img src="../assets/img/agent/1.png" alt="img">
              </div>
              <div class="details">
                <h4>Sandara Mrikon</h4>
                <h6>Estate Agent</h6>
                <ul class="social-area style-2">
                  <li><a href="#"><i class="fab fa-facebook-f" aria-hidden="true"></i></a></li>
                  <li><a href="#"><i class="fab fa-linkedin-in" aria-hidden="true"></i></a></li>
                  <li><a href="#"><i class="fab fa-instagram" aria-hidden="true"></i></a></li>
                  <li><a href="#"><i class="fab fa-twitter" aria-hidden="true"></i></a></li>
                </ul>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6">
            <div class="single-agent-wrap">
              <div class="thumb">
                <img src="../assets/img/agent/2.png" alt="img">
              </div>
              <div class="details">
                <h4>Sarif Jaya Miprut</h4>
                <h6>Area Agent</h6>
                <ul class="social-area style-2">
                  <li><a href="#"><i class="fab fa-facebook-f" aria-hidden="true"></i></a></li>
                  <li><a href="#"><i class="fab fa-linkedin-in" aria-hidden="true"></i></a></li>
                  <li><a href="#"><i class="fab fa-instagram" aria-hidden="true"></i></a></li>
                  <li><a href="#"><i class="fab fa-twitter" aria-hidden="true"></i></a></li>
                </ul>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6">
            <div class="single-agent-wrap">
              <div class="thumb">
                <img src="../assets/img/agent/3.png" alt="img">
              </div>
              <div class="details">
                <h4>Jordan Smith</h4>
                <h6>Expart Agent</h6>
                <ul class="social-area style-2">
                  <li><a href="#"><i class="fab fa-facebook-f" aria-hidden="true"></i></a></li>
                  <li><a href="#"><i class="fab fa-linkedin-in" aria-hidden="true"></i></a></li>
                  <li><a href="#"><i class="fab fa-instagram" aria-hidden="true"></i></a></li>
                  <li><a href="#"><i class="fab fa-twitter" aria-hidden="true"></i></a></li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="client-area client-area-pd bg-overlay pd-top-118" style="background: url(assets/img/other/1.png);">
      <div class="container">
        <div class="row justify-content-center text-lg-left text-center">
          <div class="col-lg-9">
            <div class="section-title style-white mb-0">
              <h6>Buy Or Sell</h6>
              <h2>Find Best Place For Leaving</h2>
              <p>Lorem ipsum dolor amet, consecteLorem ipsum dolor sit amet, consectetur adipisicing sed do eiusmod tempor incididunt dolore magna consecteLorem ipsum dolor sit amet, consectetur adipisicing elit,</p>
            </div>
          </div>
          <div class="col-lg-3 align-self-end text-lg-right mt-4 mt-lg-0">
            <a class="btn btn-base" href="#">SUBMIT</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="client-slider bg-main style-two owl-carousel">
        <div class="item">
          <div class="thumb">
            <img src="../assets/img/client/2.png" alt="img">
          </div>
        </div>
        <div class="item">
          <div class="thumb">
            <img src="../assets/img/client/3.png" alt="img">
          </div>
        </div>
        <div class="item">
          <div class="thumb">
            <img src="../assets/img/client/4.png" alt="img">
          </div>
        </div>
        <div class="item">
          <div class="thumb">
            <img src="../assets/img/client/5.png" alt="img">
          </div>
        </div>
        <div class="item">
          <div class="thumb">
            <img src="../assets/img/client/2.png" alt="img">
          </div>
        </div>
      </div>
    </div>

    <div class="blog-area pd-top-118 pd-bottom-90">
      <div class="container">
        <div class="section-title text-center">
          <h6>Blog & News</h6>
          <h2>News Feads</h2>
        </div>
        <div class="row justify-content-center">
          <div class="col-lg-4 col-md-6">
            <div class="single-product-wrap style-bottom-radius">
              <div class="thumb">
                <img src="../assets/img/project/10.png" alt="img">
              </div>
              <div class="product-details-inner">
                <ul class="meta-inner">
                  <li><i class="fa fa-user"></i>By Admin</li>
                  <li><i class="fa fa-calendar-alt"></i>Marce 9 , 2020</li>
                </ul>
                <h4><a href="blog-details.html">Family House</a></h4>
                <p>House ipsum dolor consectetur adipisicing elit, sed do eius Lorem ipsum dolo ame conse.</p>
                <a class="btn btn-base read-more" href="#"><i class="la la-arrow-right"></i></a>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6">
            <div class="single-product-wrap style-bottom-radius">
              <div class="thumb">
                <img src="../assets/img/project/11.png" alt="img">
              </div>
              <div class="product-details-inner">
                <ul class="meta-inner">
                  <li><i class="fa fa-user"></i>By Admin</li>
                  <li><i class="fa fa-calendar-alt"></i>Marce 9 , 2020</li>
                </ul>
                <h4><a href="blog-details.html">Daily Apartment</a></h4>
                <p>Daily ipsum dolor consectetur adipisicing elit, sed do eius Lorem ipsum dolo ame conse.</p>
                <a class="btn btn-base read-more" href="#"><i class="la la-arrow-right"></i></a>
              </div>
            </div>
          </div>
          <div class="col-lg-4 col-md-6">
            <div class="single-product-wrap style-bottom-radius">
              <div class="thumb">
                <img src="../assets/img/project/12.png" alt="img">
              </div>
              <div class="product-details-inner">
                <ul class="meta-inner">
                  <li><i class="fa fa-user"></i>By Admin</li>
                  <li><i class="fa fa-calendar-alt"></i>Marce 9 , 2020</li>
                </ul>
                <h4><a href="blog-details.html">Hotel Resort</a></h4>
                <p>Resort ipsum dolor consectetur adipisicing elit, sed do eius Lorem ipsum dolo ame conse.</p>
                <a class="btn btn-base read-more" href="#"><i class="la la-arrow-right"></i></a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>



    <div class="back-to-top">
      <span class="back-top"><i class="fa fa-angle-up"></i></span>
    </div>

  </div>
</template>

<style>
.home-select .el-input .el-input__inner{
  height: 50px !important;
  width: inherit;
}
</style>


<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import {request} from "@/network/request";

export default {
  name: 'Home',
  components: {
    HelloWorld
  },
  data() {
    return {
      comms: {},
      poiSearch: {},
      options: [{
          value: '选项1',
          label: '黄金糕'
        }, {
          value: '选项2',
          label: '双皮奶'
        }, {
          value: '选项3',
          label: '蚵仔煎'
        }, {
          value: '选项4',
          label: '龙须面'
        }, {
          value: '选项5',
          label: '北京烤鸭'
        }]
    }
  },
  mounted() {
    // POI查询插件
    AMap.plugin(["AMap.PlaceSearch"], ()=> {
      //构造地点查询类
      this.poiSearch = new AMap.PlaceSearch({
        type: '', // 兴趣点类别
        pageSize: 1, // 单页显示结果条数
        pageIndex: 1, // 页码
        city: "010", // 兴趣点城市
        citylimit: true,        //是否强制限制在设置的城市内搜索
        lang: 'en'
        // map: map, // 展现结果的地图实例
        // autoFitView: true // 是否自动调整地图视野使绘制的 Marker点都处于视口的可见范围
      });
    });
    request({
      url: '/all',
      method: "GET"
    }).then(res => {
      this.comms = res;
      console.log(res);
    }).catch(err => {
      console.log(err);
    });
  },
  methods: {
    search(index) {
      if(index >= this.comms.length){
        this.write();
        return;
      }
      this.poiSearch.search(this.comms[index], (status, result) => {
        // console.log(result.poiList.pois[0]);
        let params = {}
        try{
          params = {
            index: this.comms[index],
            name: result.poiList.pois[0].name,
            address: result.poiList.pois[0].address
          }
        }catch {
          params = {
            index: this.comms[index],
            name: "error",
            address: "error"
          }
        }
        request({
          url: '/write',
          params: params,
          method: "GET"
        }).then(res => {
          // this.comms = res;
          this.search(index + 1);
          console.log(res);
        }).catch(err => {
          console.log(err);
        });

      });
    },
    write() {
      request({
        url: '/write_dict',
        method: "GET"
      })
    },
    test() {
      request({
        url: '/test',
        method: "GET"
      }).then(res => {
        this.comms = res;
        console.log(res);
      }).catch(err => {
        console.log(err);
      });
    }

  }
}
</script>
