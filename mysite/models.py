from django.db import models

# Create your models here.
class Posts(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='pics')

    class Meta:
        verbose_name_plural = 'posts'


    def __str__(self):
        return self.name