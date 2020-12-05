 burger = document.querySelector('.burger')
 navbar = document.querySelector('.navbar')
 navList = document.querySelector('.nav-list')
 searchBar_home = document.querySelector('.searchBar-home')
 rightNav = document.querySelector('.rightNav')


 burger.addEventListener('click',()=>{
    navList.classList.toggle('v-class-resp');
    searchBar_home.classList.toggle('v-class-resp');
    navbar.classList.toggle('height-nav-resp');
    rightNav.classList.toggle('v-class-resp');
 })
 