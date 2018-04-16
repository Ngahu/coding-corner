from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.serializers import ModelSerializer


from .models import TodoCategory,Todo


class TodoCategoryListSerializer(ModelSerializer):
    class Meta:
        model = TodoCategory
        fields = '__all__'



class TodoCategoryCreateSerializer(ModelSerializer):

    class Meta:
        model = TodoCategory
        fields= (
            'title',
            'description'
        )
    
    # def create(self,validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return TodoCategory.objects.create(**validated_data)


class TodoListSerialzer(ModelSerializer):
    class Meta:
        model = Todo
        fields= (
            'todo_list',
            'title',
            'text',
            'priority',
            'completed',
            'timestamp'
        )