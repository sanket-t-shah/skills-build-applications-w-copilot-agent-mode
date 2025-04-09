from django.shortcuts import render
from rest_framework import viewsets
from .models import UserProfile, ActivityLog
from .serializers import UserProfileSerializer, ActivityLogSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ActivityLogViewSet(viewsets.ModelViewSet):
    queryset = ActivityLog.objects.all()
    serializer_class = ActivityLogSerializer

# Create your views here.
