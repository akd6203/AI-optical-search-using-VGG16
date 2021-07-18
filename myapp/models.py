from django.db import models

# Create your models here.

class SearchResults(models.Model):
    image = models.FileField(upload_to='images/', null=True)
    title = models.CharField(max_length=250,blank=True)
    url = models.URLField(blank=True, null=True)
    text = models.TextField(blank=True)
    searched_on = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return str(self.id)