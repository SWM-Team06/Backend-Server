# Backend-Server
⭐️ Software Maestro 13th preparatory course project ⭐️

### 🚨 Local Server URL (Server Host) 🚨
```text

```

### 🌸 Overview
|HTTP METHOD|End Point|Description|
|:------:|---|---|
| GET | /feed | 피드 조회 |
| GET | /mypage | 마이 페이지 조회 |
| GET | /detail/:post_id | 게시글 상세 페이지 |

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
        "content": "프로젝트 주제 선정 완료!!!"
      },
      {
        "post_id": 38,
		"team_name": "...",
        "profile_url": "https://googlecloud.com/...",
        "img_url": "https://googlecloud.com/…",
        "like_count": 21,
        "content": "비행기 날개 조립 완료~~"
      },
      {
        "post_id": 21,
		"team_name": "...",
        "profile_url": "https://googlecloud.com/…",
        "img_url": "https://googlecloud.com/…",
        "like_count": 11,
        "content": "팀빌딩 해버렸당"
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
    "message": "메시지 전송 성공"
}
```

