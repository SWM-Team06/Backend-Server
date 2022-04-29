from account.models import Team
from post.models import Post
from django.http import JsonResponse
import hashlib, json

def user_POST(request):
  try:
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    
    try:
      team_name = body['team_name']
      project_name = body['project_name']
      new_id = body['id']
      new_pw = body['pw']
      # hashed_pw = hashlib.sha256(str(new_pw).encode()).hexdigest()
    except:
      return JsonResponse({
        'success': 400,
        'message': '필요한 값이 전달되지 않았습니다'
      })
      
    
    Team.objects.create(team_name=team_name, project_name=project_name, description=' ', account_id=new_id, account_pw=new_pw, profile_url=' ')
    
    return JsonResponse({
      'success': 200,
      'message': '회원가입 성공'
    })
  except:
    return JsonResponse({
      'success': 500,
      'message': 'Internal Server Error'
    })