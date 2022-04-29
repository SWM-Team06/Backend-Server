# Backend-Server
⭐️ Software Maestro 13th preparatory course project ⭐️

### 🚨 Local Server URL (Server Host) 🚨
```text

```

### 🌸 Overview
|HTTP METHOD|End Point|Description|
|:------:|:---:|:---:|
| POST | /account/user | 회원가입 |
| GET | /post/feed | 피드 조회 |
| GET | /post/mypage | 마이페이지 조회 |
| GET | /post/detail/:post_id | 게시글 상세 페이지 |

---

#### 🧡 회원가입

##### 📌 Request Body
``` json
{
    "team_name": "team07",
    "project_name": "team07-project",
    "id": "team07",
    "pw": "1234"
}
```

##### 📌 Server Response
``` json
{
    "success": 200,
    "message": "회원가입 성공"
}
```

---

#### 💚 피드 조회

##### 📌 Server Response
``` json
{	
  "status": 200,
  "success": true,
  "data": {
    "posts": [
      {
        "post_id": 42,
	"team_name": "...",
        "profile_url": "https://googlecloud.com/...",
        "img_url": "https://googlecloud.com/...",
        "like_count": 31,
        "content": "프로젝트 주제 선정 완료!!!",
	"liked": true,
      },
      {
        "post_id": 38,
	"team_name": "...",
        "profile_url": "https://googlecloud.com/...",
        "img_url": "https://googlecloud.com/…",
        "like_count": 21,
        "content": "비행기 날개 조립 완료~~"
	"liked": false,
      },
      {
        "post_id": 21,
	"team_name": "...",
        "profile_url": "https://googlecloud.com/…",
        "img_url": "https://googlecloud.com/…",
        "like_count": 11,
        "content": "팀빌딩 해버렸당"
	"liked": true,
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
    "profil_url": "https://googlecloud.com/...",
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

