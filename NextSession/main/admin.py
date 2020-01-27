from django.contrib import admin
from .models import CharDescription


# Register your models here.

class CharSheetAdmin(admin.ModelAdmin):
    fields = ["char_name",
              "char_shortbio",
              "char_level",
              "char_race",
              "char_class",
              ]


admin.site.register(CharDescription, CharSheetAdmin)
