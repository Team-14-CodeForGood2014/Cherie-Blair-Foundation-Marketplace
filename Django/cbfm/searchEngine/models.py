from django.db import models

# Create your models here.

class Search(models.Model):
    quantity_text = models.CharField(max_length=20)
    units_text = models.CharField(max_length=10)
    keywords_text = models.CharField(max_length=100)
    region_text = models.CharField(max_length=50)

    def __unicode__(self):              # __str__ on Python 3
        return (self.quantity_text + self.units_text + " of " + self.keywords_text)
    

