from django.db import models

# Create your models here.
class moviesinfo(models.Model):
    name=models.CharField(max_length=122,default=None, blank=True, null=True)
    image=models.TextField(default=None, blank=True, null=True)
    release_year=models.CharField(max_length=122,default=None, blank=True, null=True)
    imdb=models.CharField(max_length=4,default=None, blank=True, null=True)
    rt=models.CharField(max_length=6,default=None, blank=True, null=True)
    gerne=models.CharField(max_length=122,default=None, blank=True, null=True)
    desc=models.TextField(default=None, blank=True, null=True)
    cast=models.TextField(default=None, blank=True, null=True)
    size480p=models.CharField(max_length=6,default='#', blank=True, null=True)
    size720p=models.CharField(max_length=6,default='#', blank=True, null=True)
    size1080p=models.CharField(max_length=6,default='#', blank=True, null=True)
    link480p=models.TextField(default='#', blank=True, null=True)
    link720p=models.TextField(default='#', blank=True, null=True)
    link1080p=models.TextField(default='#', blank=True, null=True)
    
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    decs = models.TextField(default='#', blank=True, null=True)

    def __str__(self):
        return self.name
    