from django.conf.urls import url

from .views import (
    TodoCategoryListView,
    TodoCategoryCreateAPIVIew,
    TodoAPIRootView,
    )

urlpatterns = [
    url(r'^todocategory-list/', TodoCategoryListView.as_view(),name='todocategory-listview'),
    url(r'^todocategory-create/', TodoCategoryCreateAPIVIew.as_view(),name='todo_createview'),
    url(r'^todo/v1/', TodoAPIRootView.as_view(),name='todo-v1'),
]
