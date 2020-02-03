from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class CharacterMain(models.Model):
    user_character = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    char_name = models.CharField(max_length=30)
    char_level = models.IntegerField(default=1)
    char_exp = models.IntegerField(default=0)
    char_race = models.CharField(max_length=20)
    char_class = models.CharField(max_length=30)
    char_alignement = models.CharField(max_length=2)
    char_size = models.CharField(max_length=1, default="M")
    char_shortbio = models.TextField(blank=True, null=True)


class BaseStatus(models.Model):
    char_str = models.IntegerField()
    char_dex = models.IntegerField()
    char_con = models.IntegerField()
    char_int = models.IntegerField()
    char_wis = models.IntegerField()
    char_cha = models.IntegerField()


class CombatStatus(models.Model):
    Life_Points = models.IntegerField()
    weapon_one = models.CharField(max_length=15, blank=True, null=True)
    weapon_two = models.CharField(max_length=15, blank=True, null=True)
    weapon_three = models.CharField(max_length=15, blank=True, null=True)
    weapon_four = models.CharField(max_length=15, blank=True, null=True)

    shield = models.CharField(max_length=15, blank=True, null=True)
    armor = models.CharField(max_length=15, blank=True, null=True)
    protection_one = models.CharField(max_length=15, blank=True, null=True)
    protection_two = models.CharField(max_length=15, blank=True, null=True)


class CharSkills(models.Model):
    skill_name = models.CharField(max_length=15)
    skill_mod = models.CharField(max_length=3)
    skill_graduation = models.IntegerField()






