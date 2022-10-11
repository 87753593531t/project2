from django.db import models


class Laptop(models.Model):
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    age = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Laptop'
        verbose_name_plural ='Laptops'
        ordering = ('id', )


    def __str__(self):
        return self.name
