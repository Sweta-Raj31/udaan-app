from rest_framework import serializers
from .models import *

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields=('name','email','subject','message')
        
class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields=('name','email','subject','message')
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Content
        fields=('name','email','type_content','contact','dept','college','content')
        
class CreateContentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Content
        # fields=('name','email','type_content','contact','dept','college','content')
        fields = '__all__'
        
