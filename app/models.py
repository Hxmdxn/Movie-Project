from django.db import models

class Cards(models.Model):
    img=models.ImageField(upload_to='items')
    name=models.CharField(max_length=255)
    genre=models.CharField(max_length=255)
    desc=models.CharField(max_length=255)
    year=models.CharField(max_length=15)
    duration=models.CharField(max_length=15)
    detailed_description=models.TextField(max_length=1000 ,blank=True)
    lang=models.CharField(max_length=1000 ,blank=True)


    def __str__(self):
        return f"{self.name} - {self.genre}"
