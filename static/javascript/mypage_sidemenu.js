window.onresize = function() {
  const width = window.innerWidth;
  let nav = document.getElementById('nav');
  const text = document.querySelector('text');
  // const height = window.innerHeight;	
  
  console.log(width);
  // console.log(height);
  if (width <= 1023){
    nav.classList.add('active')
  }
  else {
    nav.classList.remove('active')
  }
}

let list = document.querySelectorAll('.list');
function activeLink(){
  list.forEach((item) =>
  item.classList.remove('active'));
  this.classList.add('active');
}
list.forEach((item) =>
item.addEventListener('click', activeLink));

// 탭

const tabList = document.querySelectorAll('.tab_menu .navigation ul li');
const contents = document.querySelectorAll('.tab_menu .info .mypost')
let activeCont = ''; // 현재 활성화 된 컨텐츠 (기본:#tab1 활성화)

console.log(tabList)
console.log(contents)

  for(var i = 0; i < tabList.length; i++){
    tabList[i].querySelector('.btns').addEventListener('click', function(e){
      e.preventDefault();
      for(var j = 0; j < tabList.length; j++){
        // 나머지 버튼 클래스 제거
        tabList[j].classList.remove('active');

        // 나머지 컨텐츠 display:none 처리
        contents[j].style.display = 'none';
      }

      // 버튼 관련 이벤트
      this.parentNode.classList.add('active');

      // 버튼 클릭시 컨텐츠 전환
      activeCont = this.getAttribute('href');
      document.querySelector(activeCont).style.display = 'block';
    });
  }