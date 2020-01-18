from django.db import models
from datetime import datetime

# Create your models here.
class CharSheet(models.Model):
    char_name = models.CharField(max_length=100)
    char_shortbio = models.TextField()
    char_date = models.DateTimeField("Data de Criação do Personagem", default=datetime.now())

    def __str__(self):
        return self.char_name