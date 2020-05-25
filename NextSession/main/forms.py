from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CharacterMain, BaseStatus


class NewUserform(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserform, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CharacterMainForm(forms.ModelForm):

    class Meta:
        model = CharacterMain
        fields = ["char_name",
                  "char_race",
                  "char_class",
                  "char_alignement",
                  ]


class CharacterAttributesForm(forms.ModelForm):

    class Meta:
        model = BaseStatus
        fields = ["char_str",
                  "char_dex",
                  "char_con",
                  "char_int",
                  "char_wis",
                  "char_cha",
                  ]

