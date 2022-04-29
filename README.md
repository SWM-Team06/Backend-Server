# Backend-Server
⭐️ Software Maestro 13th preparatory course project ⭐️

### 🚨 Local Server URL (Server Host) 🚨
```text
http://127.0.0.1:8000
```

### 🌸 Overview
|HTTP METHOD|End Point|Description|
|:------:|:---:|:---:|
| POST | /account/user | 회원가입 |
| POST | /account/login | 로그인 |
| GET | /post/feed | 피드 조회 |
| GET | /post/mypage | 마이페이지 조회 |
| GET | /post/detail/:post_id | 게시글 상세 페이지 |

---

#### 🧡 회원가입

##### 📌 Request Body
``` json
{
    "team_name": "team06",
    "project_name": "Flying Object Detector",
    "id": "team06",
    "pw": "1234"
}
```

##### 📌 Server Response
``` json
{
    "status": 200,
    "success": true,
    "message": "회원가입 성공"
}
```

---

#### 🧡 로그인

##### 📌 Request Body
``` json
{
    "id": "team06",
    "pw": "1234"
}
```

##### 📌 Server Response
``` json
{
    "status": 200,
    "success": true,
    "message": "로그인 성공",
    "data": {
        "token": "team06/03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"
    }
}
```

---

#### 💚 피드 조회

##### 📌 Server Response
``` json
{
    "status": 200,
    "success": true,
    "message": "피드 불러오기 성공",
    "data": {
        "posts": [
            {
                "post_id": 1,
                "team_name": "벌이될래",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/flower_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/flower1.jpg",
                "like_count": 4,
                "content": "1주차입니다. 모두들 화이팅",
                "liked": false
            },
            {
                "post_id": 2,
                "team_name": "멍멍개",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/dog_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/dog1.jpg",
                "like_count": 1,
                "content": "우리 팀은 개가 좋아서 통역을 하기로했어요! ",
                "liked": false
            },
            {
                "post_id": 3,
                "team_name": "안날아요",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/airplane_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/airplane1.jpg",
                "like_count": 1,
                "content": "좋은 팀원분들과 비행기를 만들기로했어요! ",
                "liked": false
            },
            {
                "post_id": 4,
                "team_name": "벌이될래",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/flower_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/flower2.jpg",
                "like_count": 1,
                "content": "꽃에 대한 자료들을 수집하고있습니다. ",
                "liked": false
            },
            {
                "post_id": 5,
                "team_name": "안날아요",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/airplane_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/airplane2.jpg",
                "like_count": 0,
                "content": "벌써 설계가 얼추 끝나갑니다. ",
                "liked": false
            },
            {
                "post_id": 6,
                "team_name": "벌이될래",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/flower_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/flower3.jpg",
                "like_count": 0,
                "content": "꽃 사진 학습시키는중 ",
                "liked": false
            },
            {
                "post_id": 7,
                "team_name": "안날아요",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/airplane_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/airplane3.jpg",
                "like_count": 0,
                "content": "굴러다니는 비행기 모형을 만들어봤어요! ",
                "liked": false
            },
            {
                "post_id": 8,
                "team_name": "멍멍개",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/dog_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/dog2.jpg",
                "like_count": 0,
                "content": "오늘부터 앱 만들기 시작합니다 ",
                "liked": false
            },
            {
                "post_id": 9,
                "team_name": "벌이될래",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/flower_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/flower4.jpg",
                "like_count": 0,
                "content": "무슨무슨 기술을 써서 꽃 사진에 외모점수 부여하는데 성공했습니다. ",
                "liked": false
            },
            {
                "post_id": 10,
                "team_name": "불면증",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/sleep_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/sleep1.jpg",
                "like_count": 2,
                "content": " 다들 글 열심히쓰시길래 한문장 적어봅니다. 다같이 수면파 연구중 ",
                "liked": false
            },
            {
                "post_id": 11,
                "team_name": "안날아요",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/airplane_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/airplane4.jpg",
                "like_count": 1,
                "content": "비행기가 부서져서 이렇게저렇게 고쳤어요! ",
                "liked": false
            }
        ]
    }
}
```

---

#### 💚 마이 페이지 조회

##### 📌 Server Response
``` json
{	
  "status": 200,
  "success": true,
  "data": {
    "team_id": 6,
    "team_name": "somang",
    "project_name": "프로젝트 진행상항 공유 플랫폼",
    "description": "소마 활동을 기록할 수 있는 플랫폼 입니다~!",
    "profile_url": "https://googlecloud.com/...",
    "posts": [
      {
        "post_id": 38,
        "img_url": "https://googlecloud.com/...",
      },
      {
        "post_id": 21,
        "img_url": "https://googlecloud.com/…",
      },
      {
        "post_id": 2,
        "img_url": "https://googlecloud.com/…",
      }
    ]
  }
}
```

---

#### 💚 게시글 상세 페이지

##### 📌 Server Response
``` json
{
  "status": 200,
  "success": true,
  "data": {
    "detail": {
        "post_id": 42,
        "project_name": "걸어다니는 비행기",
        "team_name": "비행비행",
        "img_url": "https://googlecloud.com/...",
        "like_count": 31,
        "content": "1주차에는비행기가걸어다녀요",
        "uploded_at" : "2022-06-12 08:55:23",
	"liked": true,
    }
  }
}
```

