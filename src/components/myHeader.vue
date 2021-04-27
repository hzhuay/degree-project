<template>
  <div class="navbar-area navbar-area-3">
    <nav class="navbar navbar-expand-lg">
      <div class="container nav-container">
        <div class="responsive-mobile-menu">
          <button class="menu toggle-btn d-block d-lg-none" data-target="#dkt_main_menu" aria-expanded="false" aria-label="Toggle navigation">
            <span class="icon-left"></span>
            <span class="icon-right"></span>
          </button>
        </div>
        <div class="logo">
          <a href="index.html"><img src="assets/img/logo.png" alt="img"></a>
        </div>
        <div class="nav-right-part nav-right-part-mobile">
          <a class="btn btn-base" href="add-property.html">Submit</a>
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
            <li><a class="btn btn-base" href="add-property.html">Submit <i class="fa fa-plus"></i></a></li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "myHeader"
}
</script>

<style scoped>

</style>
