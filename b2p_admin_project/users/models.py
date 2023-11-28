from django.db import models
from django.contrib.auth.models import User

class auth_stb01(models.Model):

    ACCOUNT_TYPE = [
        ( 0, "User"),
        ( 1, "Admin 1"),
        ( 2, "Admin 2")
    ]

    username=models.ForeignKey(User, on_delete=models.CASCADE)
    account_type=models.SmallIntegerField(choices=ACCOUNT_TYPE,default=0)

    def __str__(self):
        return self.username



    
