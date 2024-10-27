# views.py
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Count
from .models import User, Contact, SpamReport
from .serializers import UserSerializer, ContactSerializer, SpamReportSerializer

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SpamReportView(generics.CreateAPIView):
    serializer_class = SpamReportSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)

class ContactSearchView(generics.ListAPIView):
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
