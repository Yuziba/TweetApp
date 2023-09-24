from django.contrib import admin
from . import models
# Register your models here.

    #-------------admin panelini ozellestirme
class TweetAdmin(admin.ModelAdmin):
    pass  
    




    #-------------admin panelini ozellestirme


admin.site.register(models.Tweet, TweetAdmin)