from django.contrib import admin
from .models import CharSheet


# Register your models here.

class CharSheetAdmin(admin.ModelAdmin):
    fields = ["char_name",
              "char_shortbio",
              "char_date"]


admin.site.register(CharSheet, CharSheetAdmin)
