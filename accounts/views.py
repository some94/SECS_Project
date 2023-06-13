import json
import bcrypt
import jwt

from django.views.generic import TemplateView
from django.http import JsonResponse
from SECS.settings import SECRET_KEY

from .models import User

# -- Login
class LoginView(TemplateView):
    template_name = 'login.html'
    # post 로 받은 request 데이터를 인자로 받는다
    def post(self, request):
        # data는 request의 데이터 내용을 json 형태로 불러온다
        data = json.loads(request.body)

        try:
            # request로 받아온 email 값이 존재한다면
            if User.objects.filter(email=data['email']).exists():
                # user 객체를 새로 만든다. User 데이터 중 email=data['email']인 데이터를 새로운 객체로 만든다
                user = User.objects.get(email=data['email'])
                user_password = user.password.encode('utf=8')

                # 새로 만든 객체에 담긴 비밀번호와 request로 받은 데이터를 비교한다
                if user.password == data['password']:
                    # 비밀번호를 인코딩 한 값과 현재 DB에 저장된 암호화된 값을 비교한다
                    if bcrypt.checkpw(data['password'.encode('utf=8'), user_password]):
                        # 비밀번호가 맞다면 토큰을 발행하고, 토큰 값에는 email(PK)을 넣어 발행한다
                        token = jwt.encode({'email': user.email}, SECRET_KEY, algorithm="HS256")
                        # return 시 JsonResponse에 Access token을 넣는다
                        return JsonResponse({'Authorization': token, 'message': f'{user.email}님 로그인 성공!'}, status=200)

                    return JsonResponse({'message': '비밀번호가 틀렸습니다.'}, status=401)
                return JsonResponse({'message': 'ID가 존재하지 않습니다.'}, status=400)

        except KeyError as e:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)


# -- SignUp
class SignUpView(TemplateView):
    template_name = 'signUp.html'
    # post 방식으로 요청할 경우 회원가입한다
    def post(self, request):
        # data에 request에 담긴 정보를 넣어준다
        data = json.loads(request.body)
        # 암호화되지 않은 비밀번호를 따로 저장한다
        password_not_hashed = data['password']
        # bcrypt를 사용하여 비밀번호를 암호화한다
        hashed_password = bcrypt.hashpw(password_not_hashed.encode('utf=8'), bcrypt.gensalt())

        try:
            # User 테이블에 저장한다
            User(
                name=data['name'],
                email=data['email'],
                password=hashed_password.decode('utf=8') # 암호화된 비밀번호 저장
            ).save()

            return JsonResponse({'message': '회원 가입 성공'}, status=200)

        except KeyError:
            return JsonResponse({'message': 'INVALID_KEYS'}, status=400)

    # def get(self, request):
    #     user_data = User.objects.values()
    #     return JsonResponse({'users': list(user_data)}, status=200)

class SignUpDoneTV(TemplateView):
    template_name = 'signUp_done.html'