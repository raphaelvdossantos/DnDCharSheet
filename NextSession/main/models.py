from django.db import models



# Create your models here.
class CharDescription(models.Model):
    char_name = models.CharField(max_length=100)
    char_level = models.IntegerField()
    char_exp = models.IntegerField()
    char_race = models.CharField(max_length=20)
    char_class = models.CharField(max_length=30)
    char_alignement = models.CharField(max_length=2)
    char_size = models.CharField(max_length=1)
    char_shortbio = models.TextField()

    def __str__(self):
        return self.char_name
