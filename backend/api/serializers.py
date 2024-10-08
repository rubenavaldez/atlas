from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username", "password"]
        extra_kwargs = {"password":{"write_only":True}} # password is not returned
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) # parse data
        return User 
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs ={"author":{"read_only": True}}  #author can be seen but not edited 