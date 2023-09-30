from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    #nickname = models.CharField(max_length=50)

    #foreignkey ile User sinifna eristik.
    #on_delete: eger bullanici sildi[imizde onun attigi tweetlerde silinsin istiyprsak bunu bu sekilde kullanmaliyiz]
    username = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    message = models.CharField(max_length=100)


    def __str__(self):
        # return f"Tweet nick: {self.nickname} message: {self.message}"
        return f"Tweet user: {self.username} message: {self.message}"