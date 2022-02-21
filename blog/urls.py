from django.urls import path
from blog.views import categories_list, post_list

urlpatterns = [
    path('list/', post_list),
    path('categories/list/', categories_list),
]