# Backend-Server
β­οΈ Software Maestro 13th preparatory course project β­οΈ

### π¨ Local Server URL (Server Host) π¨
```text
http://127.0.0.1:8000
```

### πΈ Overview
|HTTP METHOD|End Point|Description|
|:------:|:---:|:---:|
| POST | /account/user | νμκ°μ |
| POST | /account/login | λ‘κ·ΈμΈ |
| GET | /post/feed | νΌλ μ‘°ν |
| GET | /account/mypage | λ§μ΄νμ΄μ§ μ‘°ν |
| GET | /post/detail/:post_id | κ²μκΈ μμΈ νμ΄μ§ |

---

#### π§‘ νμκ°μ

##### π Request Body
``` json
{
    "team_name": "team06",
    "project_name": "Flying Object Detector",
    "id": "team06",
    "pw": "1234"
}
```

##### π Server Response
``` json
{
    "status": 200,
    "success": true,
    "message": "νμκ°μ μ±κ³΅"
}
```

---

#### π§‘ λ‘κ·ΈμΈ

##### π Request Body
``` json
{
    "id": "team06",
    "pw": "1234"
}
```

##### π Server Response
``` json
{
    "status": 200,
    "success": true,
    "message": "λ‘κ·ΈμΈ μ±κ³΅",
    "data": {
        "token": "team06/03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"
    }
}
```

---

#### π νΌλ μ‘°ν

##### π Server Response
``` json
{
    "status": 200,
    "success": true,
    "message": "νΌλ λΆλ¬μ€κΈ° μ±κ³΅",
    "data": {
        "posts": [
            {
                "post_id": 1,
                "team_name": "λ²μ΄λ λ",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/flower_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/flower1.jpg",
                "like_count": 4,
                "content": "1μ£Όμ°¨μλλ€. λͺ¨λλ€ νμ΄ν",
                "liked": false
            },
            {
                "post_id": 2,
                "team_name": "λ©λ©κ°",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/dog_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/dog1.jpg",
                "like_count": 1,
                "content": "μ°λ¦¬ νμ κ°κ° μ’μμ ν΅μ­μ νκΈ°λ‘νμ΄μ! ",
                "liked": false
            },
            {
                "post_id": 3,
                "team_name": "μλ μμ",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/airplane_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/airplane1.jpg",
                "like_count": 1,
                "content": "μ’μ νμλΆλ€κ³Ό λΉνκΈ°λ₯Ό λ§λ€κΈ°λ‘νμ΄μ! ",
                "liked": false
            },
            {
                "post_id": 4,
                "team_name": "λ²μ΄λ λ",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/flower_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/flower2.jpg",
                "like_count": 1,
                "content": "κ½μ λν μλ£λ€μ μμ§νκ³ μμ΅λλ€. ",
                "liked": false
            },
            {
                "post_id": 5,
                "team_name": "μλ μμ",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/airplane_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/airplane2.jpg",
                "like_count": 0,
                "content": "λ²μ¨ μ€κ³κ° μΌμΆ λλκ°λλ€. ",
                "liked": false
            },
            {
                "post_id": 6,
                "team_name": "λ²μ΄λ λ",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/flower_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/flower3.jpg",
                "like_count": 0,
                "content": "κ½ μ¬μ§ νμ΅μν€λμ€ ",
                "liked": false
            },
            {
                "post_id": 7,
                "team_name": "μλ μμ",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/airplane_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/airplane3.jpg",
                "like_count": 0,
                "content": "κ΅΄λ¬λ€λλ λΉνκΈ° λͺ¨νμ λ§λ€μ΄λ΄€μ΄μ! ",
                "liked": false
            },
            {
                "post_id": 8,
                "team_name": "λ©λ©κ°",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/dog_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/dog2.jpg",
                "like_count": 0,
                "content": "μ€λλΆν° μ± λ§λ€κΈ° μμν©λλ€ ",
                "liked": false
            },
            {
                "post_id": 9,
                "team_name": "λ²μ΄λ λ",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/flower_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/flower4.jpg",
                "like_count": 0,
                "content": "λ¬΄μ¨λ¬΄μ¨ κΈ°μ μ μ¨μ κ½ μ¬μ§μ μΈλͺ¨μ μ λΆμ¬νλλ° μ±κ³΅νμ΅λλ€. ",
                "liked": false
            },
            {
                "post_id": 10,
                "team_name": "λΆλ©΄μ¦",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/sleep_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/sleep1.jpg",
                "like_count": 2,
                "content": " λ€λ€ κΈ μ΄μ¬νμ°μκΈΈλ νλ¬Έμ₯ μ μ΄λ΄λλ€. λ€κ°μ΄ μλ©΄ν μ°κ΅¬μ€ ",
                "liked": false
            },
            {
                "post_id": 11,
                "team_name": "μλ μμ",
                "profile_url": "https://storage.cloud.google.com/somang_storage_data/profile/airplane_user.jpg",
                "img_url": "https://storage.cloud.google.com/somang_storage_data/img/airplane4.jpg",
                "like_count": 1,
                "content": "λΉνκΈ°κ° λΆμμ Έμ μ΄λ κ²μ λ κ² κ³ μ³€μ΄μ! ",
                "liked": false
            }
        ]
    }
}
```

---

#### π λ§μ΄ νμ΄μ§ μ‘°ν

##### π Server Response
``` json
{	
  "status": 200,
  "success": true,
  "data": {
    "team_id": 6,
    "team_name": "somang",
    "project_name": "νλ‘μ νΈ μ§νμν­ κ³΅μ  νλ«νΌ",
    "description": "μλ§ νλμ κΈ°λ‘ν  μ μλ νλ«νΌ μλλ€~!",
    "profile_url": "https://googlecloud.com/...",
    "posts": [
      {
        "post_id": 38,
        "img_url": "https://googlecloud.com/...",
      },
      {
        "post_id": 21,
        "img_url": "https://googlecloud.com/β¦",
      },
      {
        "post_id": 2,
        "img_url": "https://googlecloud.com/β¦",
      }
    ]
  }
}
```

---

#### π κ²μκΈ μμΈ νμ΄μ§

##### π Server Response
``` json
{
  "status": 200,
  "success": true,
  "data": {
    "detail": {
        "post_id": 42,
        "project_name": "κ±Έμ΄λ€λλ λΉνκΈ°",
        "team_name": "λΉνλΉν",
        "img_url": "https://googlecloud.com/...",
        "like_count": 31,
        "content": "1μ£Όμ°¨μλλΉνκΈ°κ°κ±Έμ΄λ€λμ",
        "uploded_at" : "2022-06-12 08:55:23",
	"liked": true,
    }
  }
}
```

