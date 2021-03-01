from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class food (models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(_("توضیحات"), max_length=50)
    photo = models.ImageField(upload_to = "foods/")
    rate = models.IntegerField(_("اعتبار") , default=0)


    def __str__(self):
        return self.name

