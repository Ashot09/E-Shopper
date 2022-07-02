from tabnanny import verbose
from django.db import models


# Create your models here.

class HomeBG(models.Model):
    name1 = models.CharField('BG name1', max_length=30)
    name2 = models.CharField('BG name2', max_length=30)
    about = models.TextField('BG about')
    img = models.ImageField('BG image', upload_to='media', null=True)

    def __str__(self):
        return self.name1 

    class Meta:
        verbose_name = 'HomeBG'
        verbose_name_plural = 'HomesBG'



