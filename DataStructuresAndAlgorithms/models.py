from django.db import models

# Create your models here.
class Topics(models.Model):
    topic = models.CharField(max_length = 400)

    def __str__(self):
        return self.topic 

class Slides(models.Model):
    slides = models.ForeignKey(Topics, on_delete = models.CASCADE)
    file_type = models.CharField(max_length =10)
    file_name = models.CharField(max_length = 250)

    def __str__(self):
        return self.file_name
    
