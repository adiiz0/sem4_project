from django.urls import path
from . import views

urlpatterns = [
    path('forums/', views.forums, name='forums'),
    path('detail/', views.detail, name='detail'),
    path('posts/', views.posts, name='posts')
]
