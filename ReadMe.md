



#  포켓몬 장터
***

![img.png](static/image/img.png)

<br>
<br>

###  소개 
***

포켓몬 이미지를 올리기, 판매, 수집 할 수 있는  중고 거래 사이트!

<br>
<br>

### 사용한 기술 
***


<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
<img src="https://img.shields.io/badge/mongoDB-47A248?style=for-the-badge&logo=MongoDB&logoColor=white">
<img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white">

<img src="https://img.shields.io/badge/tensorflow-FF7100?style=for-the-badge&logo=tensorflow&logoColor=white">
<img src="https://img.shields.io/badge/Pyjwt-8EC2F2?style=for-the-badge&logo=pyjwt&logoColor=white">
<img src="https://img.shields.io/badge/request-C5B7AC?style=for-the-badge&logoColor=white">


<br>
<br>


### 프로젝트 세팅
***
* 가상환경 : `Anaconda`

* Packages 
<img src="https://img.shields.io/badge/flask-0.01-blue?style"/>

  - `Flask` `dnspython` `pymongo` `requests` `PyJWT` `Tensorflow`

<br>
<br>


### 프로젝트 기간
***
### 2022 년 1월 13일 ~ 2022년 1월 18일 [약 1주]


<br>
<br>


### 팀 구성 및 역할 
***

<br>

김재성 [![](https://camo.githubusercontent.com/9c1b5db4f4965a22dfac0c853b5cab388c2ee7bc0016c9fbe7eb6e032ad76ebe/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769746875622d3138313731373f7374796c653d666c61742d737175617265266c6f676f3d476974687562266c6f676f436f6c6f723d7768697465)](https://github.com/CureLatte): `팀장` / `공통 백엔드` / `머신러닝`/ `카테고리페이지` /  `글 쓰기 페이지`

김호 님 [![](https://camo.githubusercontent.com/9c1b5db4f4965a22dfac0c853b5cab388c2ee7bc0016c9fbe7eb6e032ad76ebe/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769746875622d3138313731373f7374796c653d666c61742d737175617265266c6f676f3d476974687562266c6f676f436f6c6f723d7768697465)](https://github.com/hopaom):  `백엔드` / `로그인페이지` / `이미지 디자인`

이성오님 [![](https://camo.githubusercontent.com/9c1b5db4f4965a22dfac0c853b5cab388c2ee7bc0016c9fbe7eb6e032ad76ebe/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769746875622d3138313731373f7374796c653d666c61742d737175617265266c6f676f3d476974687562266c6f676f436f6c6f723d7768697465)](https://github.com/seongolee): `프론트` / `회원 가입 페이지`/ `메인 페이지`/ 

문경민님 [![](https://camo.githubusercontent.com/9c1b5db4f4965a22dfac0c853b5cab388c2ee7bc0016c9fbe7eb6e032ad76ebe/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769746875622d3138313731373f7374796c653d666c61742d737175617265266c6f676f3d476974687562266c6f676f436f6c6f723d7768697465)](https://github.com/mgm11063):  `프론트`  / `헤 더` / `상세 페이지` / `파레트`/ `전체적인 CSS  `

정심일 [![](https://camo.githubusercontent.com/9c1b5db4f4965a22dfac0c853b5cab388c2ee7bc0016c9fbe7eb6e032ad76ebe/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769746875622d3138313731373f7374796c653d666c61742d737175617265266c6f676f3d476974687562266c6f676f436f6c6f723d7768697465)](https://github.com/joneheart) : `프론트`  / `푸 터` / `개인 프로필 사진`/

<br>
<br>


### 주요기능
***

* 포켓몬 게시글 올리기
* AI 를 통한 이미지 카테고리 분류
* 댓글 기능
* 카테고리별 페이지

<br>
<br>


### 와이어 프레임
***

[Figma 링크](https://www.figma.com/file/MrPWIagiukBUsmXkD9aqJm?embed_host=share&kind=&viewer=1)

![](static/image/wireframe.png)


<br>
<br>


### AI code
***

* AI 학습은 Colab 에서 진행 
* 예제 코드 활용
* 학습 데이터 = Keggle Pokenmon data + random pokemon Image
* CNN 을 이용
* Optimazier - SGD 사용
* [코드 보기 - 클릭](https://colab.research.google.com/drive/1yTLzyxISHTPDeRQ0qLChB8lVTdfdon8R?usp=sharing) 

<br>
<br>

### DB
***

Collections 

* category 
  * poket_categroy : Array

<br>

* market
  * maket_id : `<string>`
  * user_id : `<string>`
  * content : `"<string>`
  * comment : `Array `
  * category : `<string>`
  * photo : `<string>`
  * desc : `<string>`
  * header : `<string>`
  * date : `<string>`
  * price : `<string>`
  * level : `<string>`
  * like_feed : `<string>`
  * catch_location : `<string>`
  * trade_location : `<string>`
  * like : `<int>`
  * like_list : `Array`

<br>

* users
  * avatar:`<string>`
  * user_id:`<string>`
  * password : `<string>`
  * phone_number :`<string>`
  * gender : `<string>`
  * interest_poket : `<string>`
  * point : `<int>`
  * poket_box : `Array`



<br>
<br>


***
## [포켓몬 Notion 보기!](https://quartz-laborer-e78.notion.site/sparta-4-0b2c834274b6424ba5c727555d6b1952)
*** 