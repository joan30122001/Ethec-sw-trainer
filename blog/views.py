from django.shortcuts import render
from rest_framework import serializers, generics, permissions
from blog.permissions import IsUserOrReadOnly
from .serializers import ArticleSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .models import Article

# Create your views here.


class ArticleList(generics.ListCreatedAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)



class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]