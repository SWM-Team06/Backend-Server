from account.models import Team
from post.models import Post
from post.models import Like
from django.http import JsonResponse


def feed_GET(request):
    try:
        try:
            tokens = request.GET['token'].split('_')
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

        allPost = Post.objects.filter()

        posts = []

        for post in allPost:
            creator = post.team_id
            likes = Like.objects.filter(post_id=post.post_id)
            liked = Like.objects.filter(
                team_id=login_user.team_id, post_id=post.post_id)

            post_obj = {
                'post_id': post.post_id,
                'team_name': creator.team_name,
                'profile_url': creator.profile_url,
                'img_url': post.img_url,
                'like_count': len(likes),
                'content': post.content,
                'liked': True if len(liked) == 1 else False
            }
            posts.append(post_obj)

        return JsonResponse({
            'status': 200,
            'success': True,
            'message': '피드 불러오기 성공',
            'data': {
                'posts': sorted(posts, key=lambda x: x['post_id'], reverse=True)
            }
        })
    except:
        return JsonResponse({
            'status': 500,
            'success': False,
            'message': 'Internal Server Error'
        })


def post_details(request, id):
    try:
        try:
            post = Post.objects.get(post_id=id)
        except:
            return JsonResponse({
                'status': 400,
                'success': False,
                'message': '유효하지 않는 post id 입니다'
            })
        team = post.team_id
        likes = Like.objects.filter(post_id=post.post_id)
        liked = Like.objects.filter(team_id=post.team_id, post_id=post.post_id)

        return JsonResponse({
            'status': 200,
            'success': True,
            'message': '게시글 상세정보 불러오기 성공',
            'data': {
                "post_id": post.post_id,
                "project_name": team.team_id,
                "team_name": team.team_name,
                "img_url": post.img_url,
                "like_count": len(likes),
                "content": post.content,
                "uploded_at": post.uploaded_at,
                "liked": True if len(liked) == 1 else False,
            }
        })

    except Exception as e:
        print(e)
        return JsonResponse({
            'status': 500,
            'success': False,
            'message': 'Internal Server Error'
        })
