# views.py
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User, Contact
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, ContactSerializer, SpamReportSerializer, LoginSerializer

class RegisterUserView(generics.CreateAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [AllowAny] 


class LoginView(APIView):
    permission_classes = [AllowAny] 
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [AllowAny] 
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()  # Deletes the token for the authenticated user
        return Response(status=status.HTTP_204_NO_CONTENT)

class SpamReportView(generics.CreateAPIView):
    permission_classes = [AllowAny] 
    serializer_class = SpamReportSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)

class ContactSearchView(generics.ListAPIView):
    permission_classes = [AllowAny] 
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        if query.isdigit():
            return Contact.objects.filter(phone_number=query)
        else:
            starts_with = Contact.objects.filter(name__istartswith=query)
            contains = Contact.objects.filter(name__icontains=query).exclude(id__in=starts_with.values_list('id', flat=True))
            return starts_with.union(contains)
