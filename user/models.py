from django.db import models

# 사용자
class User(models.Model) :

    email      = models.EmailField(max_length=30)
    password   = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta :

        db_table = 'users'

# 댓글
class Comment(models.Model) :

    user_email = models.ForeignKey(User,on_delete=models.CASCADE)
    comment    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta :
        db_table = 'comments'




