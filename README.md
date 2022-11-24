# YEOLDY 🤟

![yeoldy_design2](README.assets/yeoldy_design2-1669194834112-1.png)

## 🤟 What is YEOLDY?

- 주제 : Django를 활용한 의류 쇼핑몰 개발


- 프로젝트 명 : **YEOLDY**

  > NEOLDY + 우열 = **YEOLDY**

- 프로젝트 기간 : 11월 9일 ~ 11월 22일

<br>

## 🤟 AWS를 통한 배포

> 사이트 바로가기
>
> [YEOLDY](http://yeoldybean-env.eba-ghf297im.ap-northeast-2.elasticbeanstalk.com/)

<br>

## 🤟 프로젝트 참여자들

<a href="https://github.com/w00ye0l/YEOLDY/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=w00ye0l/YEOLDY" />
</a>

`프론트` : 권세빈, 이상욱, 이우열

`백` : 안동우, 여다영, 이수영

<br>

## 🤟 YEOLDY의 주요기능

#### 1. 쇼핑(의류 구매) 기능
👉 사이트 내의 상품들 중 마음에 드는 상품을 찜 또는 장바구니에 담기

👉 장바구니 기능 구현을 통한 원하는 상품 저장 가능

👉 장바구니에 담긴 상품들을 카카오페이로 결제하기

👉 구매 목록 저장 나의 페이지 열람 가능

#### 2. 스타일 공유 기능
👉 자신이 구매한 상품을 입고 사진을 찍고 글을 써, 다른 유저분들과 스타일 공유하기

#### 3. 상품 리뷰 및 문의하기 기능

👉 자신이 구매한 상품에 대한 리뷰나 문의를 할 수 있는 기능

#### 4. 상담사와 실시간으로 소통하는 기능

👉 사이트 내의 관리자와의 채팅 기능으로 관리자와 실시간으로 소통하기

<br>

## 🤟나의 주요 업무 및 상세 역할

- 기획 및 로고 디자인, 브랜드 디자인, 웹 디자인, 애니메이션 등 디자인 총괄
- javascript를 활용한 스크롤 반응형 navigation bar 제작
- 로그인 페이지 제작 및 유효성 검사 기능 구현
- 마이페이지 제작 및 sidebar menu 구현
- 회원가입 페이지 제작
- 스타일 페이지 및 스타일 디테일 페이지 제작

<br>

## 🤟YEOLDY의 디자인

#### [ Main color ]

- `#0DB295`

#### [ Logo ]

![logo_black](README.assets/logo_black.png)

![logo_green](README.assets/logo_green.png)

<br>

#### [ Favicon ]

![yeoldy_favicon](README.assets/yeoldy_favicon.png)

<br>

#### [Design pattern]

![yeoldy_design2](README.assets/yeoldy_design2.png)

<br>

<hr>

<br>

![yeoldy_main_design](README.assets/yeoldy_main_design.png)

<br>

<br>


## 🤟 YEOLDY 사이트 기능 소개

### [ Main page ]

<img src="README.assets/yeoldy_main.gif" alt="yeoldy_main" style="zoom:150%;" />

- 스크롤에 따라 반응하는 네비게이션 바 구현
- 각종 캐러셀 및 호버 효과 구현

<br>

### [ Accounts ]

![로그인_2](README.assets/로그인_2.png)

<br>

<hr>

<br>

![회원가입_2](README.assets/회원가입_2.png)

<br>

<hr>

<br>

![마이페이지](README.assets/마이페이지.png)

<br>

<hr>

<br>

![mypage_2](README.assets/mypage_2.png)


- 기본 회원 가입을 통한 로그인,  회원 정보 수정, 회원 탈퇴 구현
- 회원 가입 후 바로 로그인 기능 구현 
- 카카오와 네이버 소셜로그인을 구현하였지만, 배포 이후의 오류로 네이버만 성공함

- 로그인과 업데이트 폼에 부트스트랩 폼을 썼을 때 처럼 오류메세지 표시 직접 구현 

<br>

### [ Cart ]

<img src="README.assets/ezgif.com-gif-maker-16691869017262.gif" alt="ezgif.com-gif-maker" style="zoom:150%;" />

- 로그인 되었을 때, 해당 유저의 장바구니를 띄움
- Product 별 수량, 색상, 사이즈를 띄우고, 전체 수량 및 개수도 띄움
- 같은 Product여도, 색상 또는 사이즈가 다르면 다른 상품으로 인식하도록 함
- 장바구니에서도 수량이 변경하도록 함
- 카카오페이 테스트 결제 기능과 장바구니를 연동함
- 카카오페이 결제 완료 시, 장바구니에서 삭제 및 결제완료 상품을 따로 데이터베이스에 저장함

<br>

### [ Kakaopay ]

![orderlist](README.assets/orderlist.png)


- 장바구니와 카카오페이 테스트 결제 시스템을 연동함
- 결제 창에 2개 이상의 상품이 들어있는 경우는 '~외 몇 건' 으로 처리
- 배송 완료 건에 대한 데이터베이스(OrderList)를 구축함
- 결제 전, 배송 정보를 입력받고 이를 임시 데이터베이스에 저장

<br>

### [ Chat ]

![chat](README.assets/chat.png)

<br>

<hr>

<br>

![Untitled](README.assets/Untitled.png)

<br>

- 자신이 팔로우한 스타일 작성자와 실시간 채팅 구현을 진행하였으나 배포후 소켓 오류로 기능 구현 실패
- 상담원과의 실시간 채팅 구현(https://www.tawk.to/ 사이트 및 프로그램 이용)

<br>

### [ Community ]

![community_index](README.assets/community_index.png)

<br>

<hr>

<br>

![community_qna](README.assets/community_qna.png)

- QnA 작성/조회/삭제/수정/작성할 때 비밀번호생성/작성자와 관리자만 조회 가능 

  ![community_create](README.assets/community_create.png)

<br>

<hr>

<br>

![community_password](README.assets/community_password.png)

- QnA 생성할 때 관리자가 답변작성

![community_detail](README.assets/community_detail.png)

- 상품review 작성/조회/삭제/수정

![review_index](README.assets/review_index.png)

- 상품 평점 기능

<br>

### [ Products ]

![best](README.assets/best.png)

<br>

<hr>

<br>

![전체태그](README.assets/전체태그.png)

<br>

<hr>

<br>

![상의태그](README.assets/상의태그.png)

<br>

<hr>

<br>

![상품디테일](README.assets/상품디테일.png)

- 상품 인덱스 태그 별 구분(전체, 상의, 하의, 아우터, 신발, 악세사리)
- 상품 디테일 멀티이미지 등록 및 나열
- 상품 가격 할인률 등록 후 할인된 가격 나열 
- 찜하기, 리뷰 & QnA 기능 구현
- 장바구니 기능 구현
- 판매자가 등록한 컬러와 사이즈 구매자가 선택 가능
- 리뷰 평점 평균 계산후 등록 완료

<br>

### [ Style ]

![스타일_인덱스](README.assets/스타일_인덱스.png)

<br>

<hr>

<br>

![스타일_디테일](README.assets/스타일_디테일.png)

![스타일_댓글](README.assets/스타일_댓글.png)

- 스타일 등록시 멀티이미지 등록 및 나열 완료
- 스타일 댓글작성, 삭제(비동기) 구현 완료
- 스타일 인덱스 페이지에서 좋아요 숫자 보기
- (스타일) 좋아요, 스타일 작성자 팔로우 및 저장 기능 구현
- 스타일 작성시 자신이 구매한 상품 목록에서 선택 후 스타일 디테일에서 상품 들 보여주기 및 상품 디테일로 연결 완료

<br>


## 🤟 사용한 기술스택

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=ffffff"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=CSS3&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=Bootstrap&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=ffffff"/><img src="https://img.shields.io/badge/Javascript-F7DF1E?style=flat-square&logo=Javascript&logoColor=ffffff"/> <img src="https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=ffffff"/> <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=ffffff"/>

<br>

## 🤟 프로젝트 후기

**이우열** : YEOLDY 쇼핑몰 개발 프로젝트의 팀장을 맡아 프로젝트를 총괄하면서 느낀건 모든 팀원들이 각자의 역할에 멋진 능력을 보여주어서 너무 만족스러웠습니다. 프론트엔드 파트를 담당하면서 웹 사이트의 전반적인 디자인과 세부 디테일들을 많이 다루었고 팀 내의 발생하는 전반적인 이슈를 해결하는 역할을 했습니다. 이번 프로젝트를 진행하면서 잠을 많이 못잤는데 아마 이번 프로젝트의 팀원들이 너무 좋아서가 아닐까 싶네요ㅎㅎ 좋은 사람과 재밌는 개발이 합쳐지니 잠자는 시간이 아까울 정도였습니다. 다들 의욕이 넘쳐서 많은 기능들을 넣고 싶어 했지만 팀장인 제 능력이 부족한 탓인지 구현하지 못한게 있어 아쉬운 감이 있네요.. 그래도 YEOLDY는 최고👍

**이상욱** : 프론트를 맡아서 진행하면서 프론트에 대해 많이 배우고, 팀원들 모두 자기가 맡은 역할을 열심히 해줘서 만족스러운 결과가 나왔고 재밌었습니다.

**권세빈** : 브랜드 디자인부터 프론트 개발까지 다하면서 힘들지만 정말 즐거웠습니다. 어려운 부분이 있을 때마다 팀원들이 도와주고 소통이 잘되어서 너무 고맙고 의지가 많이 되었습니다.

**여다영** : 장바구니부터 결제기능까지 연동하려고 하니까 여러 난관들을 마주해서 힘들었지만, 팀원들이 열심히 도와주셔가지고 너무너무 좋았다. 다들 너무 수고했고 열디 짱🤍

**안동우** : 배포 후 에러가 많이 생겨서 발표 전날까지 기능 수정하면서 로컬 환경과 실제 배포는 전혀 다르다 것을 알았고 그래도 기능을 수정하면서 에러에 대응하였고 위기를 팀원과 극복하였습니다. 열심히 해준 팀원들 감사합니다

**이수영** : 디테일한 기능들 까지 구현하려고 노력하면서,  잠도 많이 못자고 힘들었지만 그래도 기술적으로 얻어가는게 많은 프로젝트였습니다. 팀원들과 맘이 잘맞아서 재미있게 프로젝트 마무리 할 수 있었습니다.
