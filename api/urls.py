from django.urls import path
from .views import (
    RegisterView, LoginView, LogoutView,
    PostListCreateView, PostDetailView,
    IndexView, LoginPageView, RegisterPageView, PostsPageView
)

urlpatterns = [
    # API
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('api/posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # HTML
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginPageView.as_view(), name='login-page'),
    path('register/', RegisterPageView.as_view(), name='register-page'),
    path('posts/', PostsPageView.as_view(), name='posts-page'),
]