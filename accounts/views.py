from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.conf import settings
from rest_framework import generics, status, viewsets, views
from rest_framework.response import Response
from .models import UserModel
from .serializers import UserModelSerializer, LoginSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect

class UserViewsets(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer

    def post(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        if serializers.is_valid():
            user = serializers.save()

            # Generate token and uid for email verification
            token = default_token_generator.make_token(user.user)  # user.user because UserModel has a OneToOne relation with User
            uid = urlsafe_base64_encode(force_bytes(user.user.pk))

            print(token, uid)
            print("robiul")

            # Build the activation link
            activation_link = f"https://myhotel-owvc.onrender.com/user/active/{uid}/{token}"
            print(activation_link)

            # Send verification email
            email_subject = 'Activate your account'
            email_body = render_to_string('confirm_email.html', {'activation_link' : activation_link, 'user':user})
            email = EmailMultiAlternatives(email_subject , '', to=[user.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

            return Response({'message': 'Check your email for account activation'}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect("registration")
    else:
        return redirect("registration")
    


    
class LoginView(views.APIView):
    def post(self, request):
        serializers = LoginSerializer(data = request.data)
        if serializers.is_valid():
            username = serializers.validated_data['username']
            password = serializers.validated_data['password']

            user = authenticate(username = username, password = password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request, user)
                return Response({'token' : token.key, 'user_id' : user.id})
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializers.errors)
    
class LogoutView(views.APIView):
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated before logging out

    def get(self, request):
        try:
            # Attempt to delete the user's auth token
            request.user.auth_token.delete()
        except Token.DoesNotExist:
            # If the token doesn't exist, return an appropriate response
            return Response({'error': 'Token not found or already deleted.'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Logout the user
        logout(request)
        
        # Redirect to the login page after logging out
        return Response({'message': 'Logged out successfully.'}, status=status.HTTP_200_OK)
