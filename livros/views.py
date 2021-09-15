from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Livro
from .serializers import LivroSerializer

class LivrosAPIView(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer


class LivroAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer






