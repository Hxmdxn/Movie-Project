from django.db import models

class Cards(models.Model):
    img=models.ImageField(upload_to='images')
    name=models.CharField(max_length=255)
    genre=models.CharField(max_length=255)
    desc=models.TextField(max_length=1000)
    year=models.CharField(max_length=15)
    duration=models.CharField(max_length=15)
    detailed_description=models.TextField(max_length=1000 ,blank=True)
    # lang=models.CharField(max_length=1000 ,blank=True)
    # director=models.CharField(max_length=1000 ,blank=True)
    # rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    # release_date=models.DateField(blank=True)
    # video_url = models.URLField(blank=True, null=True)


    def __str__(self):
        return f"{self.name} - {self.genre}"

class imdb(models.Model):
    img=models.ImageField(upload_to='images')
    name=models.CharField(max_length=255)
    genre=models.CharField(max_length=255)
    desc=models.TextField(max_length=1000)
    year=models.CharField(max_length=15)
    duration=models.CharField(max_length=15)
    detailed_description=models.TextField(max_length=1000 ,blank=True)
    # lang2=models.CharField(max_length=1000 ,blank=True)
    # director2=models.CharField(max_length=1000 ,blank=True)
    # rating2= models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    # release_date2=models.DateField(blank=True)




    def __str__(self):
        return f"{self.name} - {self.genre}"