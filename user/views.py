from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer#, ProfileSerializer
#from .models import Profile
#from .permissions import CustomReadOnly

from django.shortcuts import get_object_or_404
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User
import traceback


# 회원가입
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# 로그인
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token": token.key}, status=status.HTTP_200_OK)

# 이메일 인증
class UserActivateView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, uid, token):
        try:
            real_uid = force_str(urlsafe_base64_decode(uid))
           # print(real_uid)
            user = User.objects.get(pk=real_uid)
            if user is not None:
                access_token = AccessToken.for_user(user)
                """ 토큰 인증 해야함
                payload = jwt_decode_handler(token)
                user_id = jwt_payload_get_user_id_handler(payload)
                print(type(user))
                print(type(user_id))
                if int(real_uid) == int(user_id):
                """
                if access_token == token:
                    user.is_active = True
                    user.save()
                    return Response(user.email + '계정이 활성화 되었습니다', status=status.HTTP_200_OK)
                return Response('인증에 실패하였습니다', status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response('인증에 실패하였습니다', status=status.HTTP_400_BAD_REQUEST)

        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
            #print(traceback.format_exc())
            return Response('인증에 실패하였습니다',status=status.HTTP_400_BAD_REQUEST)