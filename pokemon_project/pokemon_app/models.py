from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=50, blank = True, null = True)
    url = models.URLField(max_length = 200, blank = True, null = True)

    def __str__(self):
        return self.name