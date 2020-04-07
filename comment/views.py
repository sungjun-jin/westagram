import json

from django.views import View
from django.http  import HttpResponse,JsonResponse

from .models      import Comment
from user.models  import User

class CommentView(View) :    
    def post(self,request) :
        data = json.loads(request.body)
        try:
            user_email = data['email']
            if User.objects.filter(email = user_email).exists(): 
                Comment (                      
                    user = User.objects.get(email = user_email), 
                    comment = data['comment']
                ).save()
                return HttpResponse(status=200)            
            return JsonResponse({'message' : 'INVALID_USER'},status=401)
        except KeyError:             
            return JsonResponse({'message' : 'INVALID_KEY'},status=400)

    def get(self,request):
        # try:
        #     dict_user_comments = {}
        #     user_comment_list = []
        #     user_list = list(User.objects.all())            
        #     for user in user_list :
        #         user_comments = list(Comment.objects.filter(user=user.id))
        #         for each_comment in user_comments :
        #             user_comment_list.append(each_comment.comment)                                    
        #         dict_user_comments[user.email]=user_comment_list
        #         user_comment_list = []                                        
        #     return JsonResponse({'comments' : dict_user_comments},status=200)    
        # except KeyError:
        #     return JsonResponse({'message' : 'INVALID_USER'},status=400)

        try:
            comment_list = list(Comment.objects.values())
            return JsonResponse({"Comments" : comment_list},status=200)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'},status=400)
