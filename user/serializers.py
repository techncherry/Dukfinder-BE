from django.contrib.auth.models import User  # User 모델
# Django의 기본 패스워드 검증 도구
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.authtoken.models import Token  # Token 모델
from rest_framework.validators import UniqueValidator  # 이메일 중복 방지를 위한 검증 도구

# 이메일 인증
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode
from rest_framework_jwt.settings import api_settings
from rest_framework.authtoken.models import Token

# from .models import Profile


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


# 회원가입 시리얼라이저
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        help_text="이메일(example@duksung.ac.kr)",
        required=True,  # 필수 입력 설정
        validators=[UniqueValidator(queryset=User.objects.all())],  # 이메일 중복 검증
    )

    # 이메일이 @duksung.ac.kr로 끝나는지 확인
    def validate_email(self, value):
        if not value.endswith('@duksung.ac.kr'):
            raise serializers.ValidationError("이메일은 @duksung.ac.kr로 끝나야 합니다.")
        return value

    # 비밀번호 1차 입력
    password = serializers.CharField(
        help_text="비밀번호",
        write_only=True,  # 출력 못하게
        required=True,
        validators=[validate_password],  # 비밀번호 검증
    )

    # 비밀번호 2차 입력
    password2 = serializers.CharField(
        help_text="비밀번호 재입력", write_only=True, required=True, )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    # 비밀번호 일치 여부 확인
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "비밀번호를 다시 입력하세요."})

        return data

        # CREATE 요청에 대해 create 메소드를 오버라이딩, 유저를 생성하고 토큰을 생성하게 함.

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],  # username 필드에 저장
            email=validated_data['email'],  # email 필드에 저장
        )

        user.set_password(validated_data['password'])  # password 필드에 저장
        user.is_active = False  # 인증 전 기본값
        user.save()  # 변경된 사용자 정보 저장

        payload = JWT_PAYLOAD_HANDLER(user)
        jwt_token = JWT_ENCODE_HANDLER(payload)
        message = render_to_string('user/user_activate_email.html', {
            'user': user,
            'domain': 'localhost:8000',
            'uid': force_str(urlsafe_base64_encode(force_bytes(user.pk))),
            'token': jwt_token,
        })
        mail_subject = '[DukFinder] 회원가입 인증 메일입니다'
        to_email = user.email
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

        token = Token.objects.create(user=user)  # 사용자에 대한 새로운 토큰 생성
        return user


# 로그인 시리얼라이저
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error": "잘못된 입력입니다."})


"""
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("nickname", "position", "subjects", "image")
"""