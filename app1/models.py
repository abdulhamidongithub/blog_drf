from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=30)
    maqola = models.TextField()

class Rasm(models.Model):
    maqola_id = models.ForeignKey(Maqola, on_delete=models.CASCADE)
    rasm = models.URLField()