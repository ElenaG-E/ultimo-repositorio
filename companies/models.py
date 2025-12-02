from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
