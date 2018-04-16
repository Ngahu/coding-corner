from django.conf.urls import url

from .views import (
    TodoCategoryListView,
    TodoCategoryCreateAPIVIew
    )

urlpatterns = [
    url(r'^list/', TodoCategoryListView.as_view(),name='list'),
    url(r'^todo-create/', TodoCategoryCreateAPIVIew.as_view(),name='list'),
]
