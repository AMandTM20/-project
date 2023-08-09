from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    #image = models.URLField(max_length=100)# ссылка на фото модели
    image = models.CharField(max_length=100)  # описание фото модели?
    release_date = models.DateField( auto_now=False, auto_now_add=False)# время выпуска модели
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=150, unique=True)