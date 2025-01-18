from django.contrib.auth.models import User
from rest_framework import serializers 
from .models import Note

#takes python object and converts it to JSON data (and vice-versa) which can be used in the communication with other applications 

class UserSerializer (serializers.ModelSerializer):
    class Meta: 
        model = User #built into django
        fields = ["id", "username", "password"] #fields we want to serialize when accepting and returning new user 
        extra_kwargs = {"password": {"write_only": True}} #write_only tells django we want to accept PW when creating new user, but don't want to return when PW when giving info about a user

    def create(self, validated_data): #to create new user, takes validated_data 
        user = User.objects.create_user(**validated_data) #creates new user, passes validated data. ** splits up keyword arguments 
        return user 
    
class NoteSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Note
        fields = ['id', 'title','content','created_at','author']
        extra_kwargs = {"author": {"read_only": True}} #read_only = cannot set author, only read (automatically set)

