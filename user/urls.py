from django.urls import path
from .views import SignUpView,SignInView,CommentView

urlpatterns = [

   path('/signUp', SignUpView.as_view()),
   path('/signIn', SignInView.as_view()),
   path('/comment',CommentView.as_view()),
   # 댓글 GET Method
   path('/comment/user_id=<id>',CommentView.as_view()),    
]
