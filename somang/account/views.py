from account.models import Team
from django.http import JsonResponse
import hashlib
import json


def user_POST(request):
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        try:
            team_name = body['team_name']
            project_name = body['project_name']
            new_id = body['id']
            new_pw = body['pw']
            hashed_pw = hashlib.sha256(str(new_pw).encode()).hexdigest()
        except:
            return JsonResponse({
                'status': 400,
                'success': False,
                'message': '필요한 값이 전달되지 않았습니다'
            })

        Team.objects.create(team_name=team_name, project_name=project_name,
                            description=' ', account_id=new_id, account_pw=hashed_pw, profile_url=' ')

        return JsonResponse({
            'status': 200,
            'success': True,
            'message': '회원가입 성공'
        })
    except:
        return JsonResponse({
            'status': 500,
            'success': False,
            'message': 'Internal Server Error'
        })


def login_POST(request):
    try:
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        try:
            input_id = body['id']
            input_pw = body['pw']
            hashed_pw = hashlib.sha256(str(input_pw).encode()).hexdigest()
        except:
            return JsonResponse({
                'status': 400,
                'success': False,
                'message': '필요한 값이 전달되지 않았습니다'
            })

        login_team = Team.objects.filter(
            account_id=input_id, account_pw=hashed_pw)

        if (len(login_team) != 1):
            return JsonResponse({
                'status': 400,
                'success': False,
                'message': '아이디 또는 비밀번호가 일치하지 않습니다'
            })

        return JsonResponse({
            'status': 200,
            'success': True,
            'message': '로그인 성공',
            'data': {
                'token': login_team[0].account_id + '/' + login_team[0].account_pw
            }
        })
    except:
        return JsonResponse({
            'status': 500,
            'success': False,
            'message': 'Internal Server Error'
        })
    
    
def mypage_GET(request):
  try:
    try:
      tokens = request.GET['token'].split('/')
    except:
      return JsonResponse({
        'status': 400,
        'success': False,
        'message': '잘못된 접근입니다'
      })

    try:
      login_user = Team.objects.get(
        account_id=tokens[0], account_pw=tokens[1])
    except:
      return JsonResponse({
        'status': 400,
        'success': False,
        'message': '올바르지 않은 token입니다'
      })

    posts = Post.objects.filter(team_id = login_user.team_id).order_by('-uploaded_at')
    dictPosts = []

    for i in range(len(posts)):
      temp = {}
      temp["post_id"] = posts[i].post_id
      temp["img_url"] = posts[i].img_url
      dictPosts.append(temp)

    return JsonResponse({
      "status": 200,
      "success": True,
      "data": {
        "team_id": login_user.team_id,
        "team_name": login_user.team_name,
        "project_name": login_user.project_name,
        "description": login_user.description,
        "profile_url": login_user.profile_url,
        "posts": dictPosts
      }
    })

  except:
    return JsonResponse({
      'status': 500,
      'success': False,
      'message': 'Internal Server Error'
    })
