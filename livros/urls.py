from django.urls import path

from .views import LivroAPIView, LivrosAPIView

urlpatterns = [
    path('livros/', LivrosAPIView.as_view(), name='livros'),
    path('livros/<int:pk>/', LivroAPIView.as_view(), name='livro'),
]
