// logo.onmouseover = function(){
//   logo.src = "static/images/logo_green.png";
// }
// logo.onmouseout = function(){
//   logo.src = "static/images/logo_white.png";
// }

window.addEventListener("scroll", function () {
  const nav = document.querySelector("nav");
  nav.classList.toggle("sticky", window.scrollY > 0)
  const logo = document.querySelector("#logo1");

    if (window.scrollY > 0) {
      nav.style.backgroundColor = "white";
      nav.style.height = "4rem";
      // nav.style.cssText = "backdrop-filter: blur(5px); height: 4rem; background-color: rgba(255,255,255,0.6)";
      logo.src = "static/images/logo_black.png";
      // logo.onmouseover = function(){
      //   logo.src = "static/images/logo_green.png";
      // }
      // logo.onmouseout = function(){
      //   logo.src = "static/images/logo_black.png";
      // }
  } else {
      nav.style.backgroundColor = "rgba(0,0,0,0)";
      nav.style.height = "6rem";
      logo.src = "static/images/logo_white.png";
      // logo.onmouseover = function(){
      //   logo.src = "static/images/logo_green.png";
      // }
      // logo.onmouseout = function(){
      //   logo.src = "static/images/logo_white.png";
      // }
  }
})



// window.addEventListener("scroll", function () {
//   const nav = document.querySelector("nav");
//   const navItems = document.querySelector("#navItems > li > a");
//   // const search = document.querySelector("i");
//   const logo = document.querySelector("#logo");
//   // const navCol = document.querySelector("#navbarSupportedContent");

//   if (window.scrollY > 0) {
//       nav.style.backgroundColor = "white";
//       nav.style.height = "4rem";
//       // dropMenu.style.backgroundColor = "white";
//       // navCol.style.backgroundColor = "white";
//       logo.src = "static/images/logo_black.png";
//       navItems.style.color = "black";
//   } else {
//       nav.style.backgroundColor = "rgba(0,0,0,0)";
//       nav.style.height = "6rem";
//       // dropMenu.style.backgroundColor = "#f08724";
//       // navCol.style.backgroundColor = "#f08724";
//       logo.src = "static/images/logo_white.png";
//       navItems.style.color = "white";
//   }
// })