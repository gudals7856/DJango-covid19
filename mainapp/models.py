from django.db import models

# Create your models here.
class Sequence(models.Model):
    namecode = models.CharField(primary_key=True, max_length=300)
    sequence = models.TextField()

    def __str__(self):
        return str(self.namecode) + "," + str(self.sequence)


class Alignment(models.Model):
    namecode1 = models.CharField(max_length=300)
    namecode2 = models.CharField(max_length=300)
    align_sequence = models.TextField(null=True)
    image = models.TextField(null=True)

    def __str__(self):
        return str(self.namecode1) + "," + str(self.namecode2) + "," + str(self.align_sequence) + "," + str(self.image1) + "," + str(self.image2)