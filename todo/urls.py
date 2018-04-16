from django.conf.urls import url

from .views import TodoCategoryListView

urlpatterns = [
    url(r'^list/', TodoCategoryListView.as_view(),name='list'),
]
