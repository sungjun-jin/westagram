from django.urls import path
from .views      import CommentView

urlpatterns = [

   path('',CommentView.as_view()),   
   #path('/<int:user_id>',CommentView.as_view()),
]