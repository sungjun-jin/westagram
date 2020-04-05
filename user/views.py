import json

from django.views import View
from django.http import HttpResponse,JsonResponse
from .models import User,Comment



# 회원가입
class SignUpView(View) :

    def post(self,request) :

        data = json.loads(request.body)        
        
        try : 
            data_email = data['email']

            if User.objects.filter(email = data_email) :
                #회원아이디 중복, 409 conflict response return
                return JsonResponse({'message' : "EMAIL_DUPLICATE"}, status = 409)
            else :            
                                    
                User (

                    email = data['email'],
                    password = data['password'],

                ).save()

                return HttpResponse(status=200)
        except KeyError :
            # key값 누락
            return JsonResponse({'message' : 'KeyError'},status = 400)            

# 로그인
class SignInView(View) :

    def post(self,request) :

        data = json.loads(request.body)
        try : 
            data_email = data['email'] 
            data_password = data['password']
        

            if User.objects.filter(email = data_email) :            
                # 아이디 존재
                user_login = list(User.objects.filter(email = data_email))                       

                if data_password == user_login[0].password :
                    # 비밀번호 일치
                    return HttpResponse(status=200)
                else :
                    # 비밀번호 불일치
                    return JsonResponse({"message" : "INVALID_USER"}, status = 401)      
                
            else :
                # 아이디 없음 -> 401 return
                return JsonResponse({"message" : "NO_MATCHING_EMAIL"}, status = 401)
        except KeyError : 
            # key값 누락
            return JsonResponse({'message' : 'KeyError'},status = 400)          

class CommentView(View) :
    # 댓글 작성
    def post(self,request) :

        data = json.loads(request.body)
        try :
            user_email = data['email']

            if User.objects.filter(email = user_email) : 

                Comment (

                    user_email = User.objects.get(email = user_email),
                    comment = data['comment']

                ).save()

                return JsonResponse({"message" : "SUCCESS"}, status = 200)
            else :
                # 아이디 없음 -> 401 return
                return JsonResponse({"message" : "NO_MATCHING_EMAIL"}, status = 401)

        except KeyError : 
            # key값 누락
            return JsonResponse({'message' : 'KeyError'},status = 400)


    # 댓글 조회
    def get(self,request,id) :                         

        comment_object = Comment.objects.filter(user_email_id = id)
        comment_list = []

        #댓글 모으기
        for object in comment_object :
            comment_list.append(object.comment)

        
        return JsonResponse({"comments" : comment_list}, status = 200)

