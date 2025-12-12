from django.db import models

class Programmer(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    experience = models.DecimalField(max_digits=50, decimal_places=2)

    def __str__(self):
        return f"{self.name}: {self.experience}"

    class Meta:
        verbose_name = "Programmer"
        verbose_name_plural = "Programmers"

