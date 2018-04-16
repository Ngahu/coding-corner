from django.shortcuts import render

# Create your views here.

from django.contrib.auth import get_user_model
User = get_user_model()

from .models import TodoCategory,Todo
from rest_framework import status
from rest_framework.views import APIView
from .serializers import TodoCategoryListSerializer,TodoCategoryCreateSerializer
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



class TodoCategoryCreateAPIVIew(APIView):

    """
    creating of a single todo category
    """

    def post(self,request,format=None):
        title = request.data["title"]
        description = request.data["description"]

        if title is not None:
            if TodoCategory.objects.filter(title=title).exists():
                error = {
                    'error':'Sorry the title must be unique'
                }
                return Response(error,status=status.HTTP_400_BAD_REQUEST)
        else:
            error = {
                'error':'sorry, the title cannot be blank'
            }
        data = {
            "title":request.data["title"],
            "description" :request.data["description"]
        }
        serializer_class = TodoCategoryCreateSerializer(data=data)

        if serializer_class.is_valid():
            serializer_class.save(owner=self.request.user)

            return Response(serializer_class.data,status=status.HTTP_201_CREATED)