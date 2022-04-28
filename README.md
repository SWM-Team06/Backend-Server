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
    "message": "Footprint 조회 성공",
    "data": {
        "messages": [
            "Javascript 4차 세미나 홧팅!",
            "안녕하세요~~"
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

