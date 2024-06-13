from rest_framework import serializers
from store.models import User
from store.models import Productmod

class signup(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email"]
        read_only_fields=["id"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class login(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

class productserializers(serializers.ModelSerializer):
    class Meta:
        model=Productmod
        fields="__all__"
        