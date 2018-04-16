from django.contrib import admin

# Register your models here.
from .models import TodoCategory,Todo



admin.site.register(TodoCategory)


admin.site.register(Todo)