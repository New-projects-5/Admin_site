from datetime import datetime

from django.db.models import Q
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import UserVerification, User
from users.serializers import SignUpSerializer


class SignUpApiView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = SignUpSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        user = get_object_or_404(User.objects.all(), email=email)
        refresh_token = RefreshToken.for_user(user)
        tokens = {
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token)
        }
        data = serializer.data
        data['tokens'] = tokens
        return Response({
            'data': data,
            'description': "Emailingizga tasdiqlash kodi yuborildi",
            'status': status.HTTP_201_CREATED
        })


class VerifyCodeApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        code = request.data.get('code')
        user = request.user
        verifies = UserVerification.objects.filter(
            Q(user=user) & Q(time_limit__gt=datetime.now()) & Q(is_confirmed=False) & Q(code=code))
        if verifies.exists():
            verify = verifies.first()
            verify.is_confirmed = True
            user.status = 'code'
            user.save()
            refresh = RefreshToken.for_user(user=user)
            return Response(
                {
                    'description': "Kod muvaffaqiyatli tasdiqlandi",
                    'tokens': {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token)
                    },
                    'status': status.HTTP_200_OK,
                }
            )
        return Response(
            {
                'description': "Siz noto'g'ri kod kiritdingiz",
                'status': status.HTTP_400_BAD_REQUEST
            }
        )
