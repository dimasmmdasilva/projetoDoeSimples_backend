from django.shortcuts import render
from rest_framework import generics
from .models import Comment
from .serializer import CommentSerializer

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer