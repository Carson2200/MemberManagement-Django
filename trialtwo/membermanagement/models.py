from django.db import models


# Create your models here.
class NewMember(models.Model):
    objects = models.manager
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)

    userName = models.CharField(max_length=20)

    def __str__(self):
        return f'New_member({self.firstName}, {self.lastName}, {self.email},{self.userName}, {self.phone})'
