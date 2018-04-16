from django.shortcuts import render

# Create your views here.

from django.contrib.auth import get_user_model
User = get_user_model()

from .models import TodoCategory,Todo
from rest_framework import status
from rest_framework.views import APIView
from .serializers import TodoCategoryListSerializer
from rest_framework.response import Response


class TodoCategoryListView(APIView):
    """
    List the personal Todo Categories of a single user
    """


    def get(self,request,format=None):
        owner= self.request.user
        queryset = TodoCategory.objects.filter(owner=owner)
        serializer = TodoCategoryListSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)