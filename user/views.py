import json

from django.views import View
from django.http  import HttpResponse,JsonResponse
from .models      import User

class SignUpView(View):
    def post(self,request):
        data = json.loads(request.body)             
        try: 
            data_email = data['email']
            if User.objects.filter(email = data_email).exists():                
                return JsonResponse({'message' : "USER_ALREADY_EXITS"},status=400)                                               
            User (
                email = data['email'],
                password = data['password'],
            ).save()
            return HttpResponse(status=200)
        except KeyError:            
            return JsonResponse({'message' : 'INVALID_KEY'},status=400)            

class SignInView(View):
    def post(self,request):
        data = json.loads(request.body)
        try: 
            data_email = data['email'] 
            data_password = data['password']        
            if User.objects.filter(email=data_email).exists():          
                user =  User.objects.get(email=data_email) 
                if data_password == user.password:                   
                    return HttpResponse(status=200)                             
            return JsonResponse({"message" : "INVALID_USER"},status=401)
        except KeyError:            
            return JsonResponse({'message' : 'INVALID_KEY'},status=400)     



