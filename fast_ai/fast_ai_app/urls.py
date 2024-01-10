from django.urls import path
from .views import forums, detail, posts

urlpatterns = [
    path('', forums, name='forums'),
    path('detail/<slug>/', detail, name='detail'),
    path('posts/<slug>/', posts, name='posts')
]
