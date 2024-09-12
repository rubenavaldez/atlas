from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_class = [IsAuthenticated] # only an authenticated user can make a note

    def get_queryset(self): # get query allows acces to user info, override the gerquery set, see django docs
       user = self.request.user
       return Note.objects.filter(author=user) # get notes associated with the user
    
    def perform_create(self,serializer): # overridding the create method, see django docs
        if serializer.is_valid():
            serializer.save(author=self.request.user) #maunally add an author
        else:
            print(serializer.error)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): # get query allows acces to user info, override the gerquery set, see django docs
       user = self.request.user
       return Note.objects.filter(author=user) # get notes associated with the user



class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] # allow non authenticated users to create a new user
