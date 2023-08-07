# accounts/views.py
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions

from .models import CustomUser
from .serializers import SignUpSerializer

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils.timezone import now
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

# from .models import User
from .serializers import SignUpSerializer
from .services import create_user

# Create your views here.
from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        pass




class ResetPasswordView(APIView):
    def post(self, request):
        email = request.POST.get('email')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return JsonResponse({'error': 'User with the provided email does not exist.'}, status=404)

        # token_generator = PasswordResetTokenGenerator()
        # new_token = token_generator.make_token(user)
        # user.password_reset_token = new_token
        user.save()
        # Send the password reset email to the user
        send_mail(
            'Password Reset',
            'Please use the following link to reset your password: [reset_link]',
            'from@example.com',
            [email],
            fail_silently=False,
        )

        return JsonResponse({'message': 'Password reset email sent successfully.'}, status=200)

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


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        # Authenticate user using email and password
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # If the user is authenticated, log them in
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            data = {
                'key': token.key,
                'user_type': user.user_type,
                'email': user.email,
            }
            return JsonResponse(data, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

