from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):

    player = models.ForeignKey(User, on_delete=models.CASCADE)
    step = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    time = models.DateTimeField()

    def __str__(self):
        # return str(self.player.username) + str(self.id)
        return f"Пользователь - {str(self.player.username)} шаг - {str(self.step)}"
# Create your models here.
