from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):


    token = serializers.CharField(max_length=100)
    time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Game
        fields = ('x', 'y', 'token', 'time')
