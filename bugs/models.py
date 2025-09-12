from django.db import models
from django.contrib.auth.models import User

bug_choices=[
    ('gameplay_or_mechanics','Gameplay & Mechanics'),
    ('graphics_or_performance','Graphics & Performance'),
    (' network_or_multiplayer',' Network & Multiplayer'),
    ('ui_or_game_logic','UI & Game Logic'),
    ('other','Other(Explain in Description)')
]

# Create your models here.
class Bug(models.Model):
    name=models.CharField( max_length=50)
    bug_type=models.CharField(choices=bug_choices)
    description=models.TextField()
    number_of_occurences=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='bugs')

