from django.db import models


class OtoshimonoInfo(models.Model):
    obj_name = models.CharField(max_length=200)
    place_found = models.CharField(max_length=200, default="")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.obj_name