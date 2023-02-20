from django.db import models

# Create your models here.
class Students(models.Model):
    DIRECTIONS =(
        ('Backend','Backend'),
        ('Front-end','Front-end'),
        ('fullstack','fullstack'),
        ('UI/UX','UI/UX'),
    )
    GENDER = (
        ('male','male'),
        ('female','female'),

    )
    full_name = models.CharField(max_length=255),
    age = models.IntegerField(),
    direction = models.CharField(max_length=255,choices=DIRECTIONS),
    gender = models.CharField(max_length=255,choices=DIRECTIONS),