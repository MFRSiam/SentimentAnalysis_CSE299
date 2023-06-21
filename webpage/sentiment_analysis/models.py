from django.db import models

# Create your models here.


class History(models.Model):
    sentence = models.CharField(max_length=100)
    aspect = models.CharField(max_length=50)
    sentiment = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.sentence + " Sentiment: " + self.sentiment + " Aspect: " + self.aspect