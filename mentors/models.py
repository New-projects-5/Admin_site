from django.db import models

TOIFA = (
    (1, "Birinchi toifa"),
    (2, "Ikkinchi toifa"),
)
JINS = (
    ('erkak', 'erkak'),
    ('ayol', 'ayol'),
)


class Ustoz(models.Model):
    ism = models.CharField(max_length=31)
    sharif = models.CharField(max_length=31)
    gmail = models.EmailField(unique=True)
    telefon_raqam = models.CharField(max_length=17)
    tugilgan_sana = models.DateTimeField()
    malumot = models.TextField()
    toifa = models.IntegerField(choices=TOIFA)
    jins = models.CharField(choices=JINS, max_length=5)

    def __str__(self):
        return self.ism


class Mijoz(models.Model):
    ism = models.CharField(max_length=31)
    sharif = models.CharField(max_length=31)
    gmail = models.EmailField(unique=True)
    telefon_raqam = models.CharField(max_length=17)
    tugilgan_sana = models.DateTimeField()
    xizmat = models.IntegerField(default=0)
    ustoz = models.ManyToManyField(Ustoz, related_name='mijozlar')

    def __str__(self):
        return self.ism
