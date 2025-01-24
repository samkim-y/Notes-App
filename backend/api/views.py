from django.shortcuts import render
from django.contrib.auth.models import User 
from rest_framework import generics , status
from .serializers import UserSerializer 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import  NoteSerializer
from .models import Note

#create class based view which allows us to to implement creating a new user (registration form)
class CreateUserView(generics.CreateAPIView):  #generic view built into django 
    queryset = User.objects.all() 
    #specifies list of all different objects we're going to be looking at when creating a new user, 
    #to ensure we don't create a user that already exists
    serializer_class = UserSerializer #tells the view what kind data we need to accept to create new user (user, pw)
    permission_classes = [AllowAny] #specifies who can call this (anyone, even unauthenticated)s



class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self): #overriding queryset to set filter (author = user)
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self,serializer): #create new note 
        if serializer.is_valid():
            serializer.save(author = self.request.user) #makes new version of note. author must be passed in bc it was set as read_only in serializer
        else: 
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self): #gets valid notes that can be deleted (only user's notes)
        user = self.request.user
        return Note.objects.filter(author=user)
    










