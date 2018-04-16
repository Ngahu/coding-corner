from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.serializers import ModelSerializer


from .models import TodoCategory,Todo


class TodoCategoryListSerializer(ModelSerializer):
    class Meta:
        model = TodoCategory
        fields = '__all__'
        