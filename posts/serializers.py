from rest_framework import serializers
from data.models import Declirations

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model =Declirations
        fields ='__all__'
        # ['title','body_text','date']