from django.db import models

class Telifon(models.Model):
    nomi = models.CharField(max_length=50)
    narx = models.CharField(max_length=50, default="so'm")
    rasim = models.ImageField( upload_to='media')
    vaqt = models.DateField()
    malimot = models.TextField()


    def __str__(self) -> str:
        return self.nomi
    

