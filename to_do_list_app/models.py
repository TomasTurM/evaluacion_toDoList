from django.db import models

# Create your models here.

class List_Object(models.Model):
    post_date = models.DateField(verbose_name='Date')

    content = models.CharField(max_length=100, verbose_name='Content')

    archived = models.BooleanField(verbose_name='Archived?')

    def __str__(self):
        return '{} {}'.format(self.post_date, self.content)

    class Meta:
        verbose_name = "Objeto de lista"
        verbose_name_plural = "Objetos de lista"

