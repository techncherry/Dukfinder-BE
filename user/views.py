from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, UserinfoSerializer, PasswordSerializer
from .models import Profile
from .permissions import CustomReadOnly
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated

# 로그인
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

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
        token = serializer.validated_data  # validate()의 리턴값인 token을 받아온다.
        return Response({"token": token.key}, status=status.HTTP_200_OK)
    
# 프로필 뷰    
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [CustomReadOnly] # 본인만 프로필 수정 가능하도록

# 유저 이름, 이메일 가져오기/회원탈퇴/로그아웃
class UserinfoView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserinfoSerializer

    def get(self, request):
        user = request.user
        serializer = self.get_serializer(user)
        serialized_data = {'username': serializer.data.get('username', ''),
                           'email': serializer.data.get('email', '')}
        return Response(serialized_data)

    def delete(self, request):
        user = request.user
        if user:
            user.delete()
            return Response({"message": "회원탈퇴 성공"}, status=status.HTTP_200_OK)
        return Response({"message": "회원탈퇴 실패"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        user = request.user
        if user:
            logout(request)
            data = {'success': '로그아웃 성공'}
            return Response(data=data, status=status.HTTP_200_OK)
        data = {'success': '로그아웃 실패'}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

class PasswordView(generics.UpdateAPIView):
    serializer_class = PasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']

            # Check if the old password is correct
            if not user.check_password(old_password):
                return Response({'detail': 'Old password is incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

            # Set the new password and save the user object
            user.set_password(new_password)
            user.save()

            return Response({'detail': 'Password changed successfully.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

