from django.db import models


class Togri(models.Model):
    soz = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.soz}"


class Notogri(models.Model):
    soz = models.CharField(max_length=30)
    t_soz = models.ForeignKey(Togri, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.soz}"
