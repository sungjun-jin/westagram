import json
import bcrypt
import jwt

from django.views       import View
from django.http        import HttpResponse,JsonResponse
from .models            import User
from westagram.settings import SECRET_KEY

class SignUpView(View):
  def post(self,request):
    data = json.loads(request.body)
    try:
      data_email = data['email']
      if User.objects.filter(email = data_email).exists():
        return JsonResponse({'message' : "USER_ALREADY_EXITS"}, status=400)
      password = data['password'].encode('utf-8')
      hashed_password = bcrypt.hashpw(password,bcrypt.gensalt())
      User (
            email = data['email'],
            password = hashed_password.decode('utf-8')
            ).save()

      return HttpResponse(status=200)
    except KeyError:
      return JsonResponse({'message' : 'INVALID_KEY'}, status=400)

class SignInView(View):
  def post(self,request):
    data = json.loads(request.body)
    try:
      data_email = data['email']
      data_password = data['password']
      if User.objects.filter(email=data_email).exists():
        user =  User.objects.get(email=data_email)
        data_password = data_password.encode('utf-8')
        if bcrypt.checkpw(data_password,user.password.encode('utf-8')):
          access_token = jwt.encode({'user_id' : user.id}, SECRET_KEY, algorithm='HS256')
          return JsonResponse({'access_token': access_token.decode('utf-8')}, status=200)
      return JsonResponse({"message" : "INVALID_USER"}, status=401)
    except KeyError:
      return JsonResponse({'message' : 'INVALID_KEY'}, status=400)

