from django.db import models

# Create your models here.

#Home Section

class Home(models.Model):
    title = models.CharField(max_length=100)
    greeting_1 = models.CharField(max_length=5)
    greeting_2 = models.CharField(max_length=5)
    picture = models.ImageField(upload_to='picture/')
    #save time whene modified
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# About Section

class About(models.Model):
    tittle = models.CharField(max_length=50)
    career = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    profile_picture = models.ImageField(upload_to='profile/')

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.career

class profile(models.Model):
    about = models.ForeignKey(About, 
       on_delete=models.CASCADE)
    social_media = models.CharField(max_length=50)
    links = models.URLField(max_length=200)

#Skills Section

class Category(models.Model):
    name = models.CharField(max_length=50)

    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'

    def __str__(self):
        return self.name

class skills(models.Model):
        category = models.ForeignKey(Category, 
           on_delete=models.CASCADE)
        skill_name=models.CharField(max_length=50)    
#Portfolio Section

class Portfolio(models.Model):
    picture = models.ImageField(upload_to='portfolio/')
    link = models.URLField(max_length=200)

    def __self__(self):
        return f'portfolio {self.id}'
