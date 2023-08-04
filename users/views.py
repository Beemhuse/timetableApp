# accounts/views.py
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions

from .models import CustomUser
from .serializers import SignUpSerializer

class SignUpView(APIView):
    serializer_class = SignUpSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user_type = serializer.validated_data['user_type']
            is_hod = user_type == 'hod'
            is_exam_officer = user_type == 'exam_officer'
            user = CustomUser.objects.create_user(
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
                is_hod=is_hod,
                is_exam_officer=is_exam_officer,
            )
            data = serializer.data
            token, _ = Token.objects.get_or_create(user=user)
            data['key'] = token.key
            return Response(data=data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
